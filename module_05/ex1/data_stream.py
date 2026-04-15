from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union


class DataStream(ABC):
    """
    Abstract base class for streaming data sources.

    A DataStream defines a common, polymorphic interface to handle different
    kinds of streaming batches (sensor, transactions, events, etc.) following
    a fixed pipeline:

        stream() -> clean_batch() -> process() -> analysis()

    Subclasses must implement the abstract methods to provide stream-specific
    behavior.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a stream instance with a unique identifier.

        Args:
            stream_id: Unique identifier for the stream.

        Raises:
            TypeError: If stream_id is not a string.
        """
        if not isinstance(stream_id, str):
            raise TypeError("Bad type (str)")
        self.stream_id: str = stream_id

    def process_batch(self, batch: List[Any]) -> None:
        """
        Execute the full batch pipeline for this stream.

        The base class enforces the same processing flow for all streams:
        1) Identify the stream (stream)
        2) Validate/transform/filter the input data (clean_batch)
        3) Process the cleaned batch (process)
        4) Produce an analysis/summary (analysis)

        Args:
            batch: Raw batch payload received by the stream.

        Raises:
            TypeError: If batch is not a list.
        """
        if not isinstance(batch, list):
            raise ValueError("Batch must be a list")

        self.stream()

        clean = self.clean_batch(batch)

        self.process(clean)
        self.analysis(clean)

    @abstractmethod
    def stream(self) -> None:
        """
        Print or expose basic stream metadata.

        This method is used to identify the
        stream type and ID before processing.
        Subclasses typically print a header like:
            "Stream ID: <id>, Type: <type>"
        """
        raise NotImplementedError

    @abstractmethod
    def clean_batch(self, batch: List[Any]) -> List[Any]:
        """
        Validate, transform, and filter the raw batch into a clean batch.

        This method is responsible for handling corrupted/malformed inputs
        without crashing the stream:
        - Drop invalid records
        - Normalize formats (e.g., casting numbers, trimming strings)
        - Enforce basic constraints and ranges

        Args:
            batch: Raw input batch.

        Returns:
            A cleaned batch containing only valid, normalized records
        """
        raise NotImplementedError

    @abstractmethod
    def process(self, batch: List[Any]) -> None:
        """
         Process the cleaned batch.

        This is where the stream performs its main logic once data is already
        sanitized (e.g., storing records, printing structured output, etc.).

        Args:
            batch: Cleaned batch produced by clean_batch().
        """
        raise NotImplementedError

    @abstractmethod
    def analysis(self, batch: List[Any]) -> None:
        """
        Produce a summary/analysis for the cleaned batch.

        Examples:
        - SensorStream: average temperature
        - TransactionStream: net flow (buys - sells)
        - EventStream: number of "error" events

        Args:
            batch: Cleaned batch produced by clean_batch().
        """
        raise NotImplementedError


class SensorStream(DataStream):
    """
    Stream for environmental sensor readings (temp, hum, press)
    """
    def stream(self) -> None:
        """
        Print stream identifier and sensor type
        """
        print(f"Stream ID: {self.stream_id} (SENSOR)")

    def clean_batch(self, batch: List[Any]) -> List[Any]:
        """
        Filter and normalize raw readings.

        Keeps only dict records with temp/hum/press, castable to float
        and within safe ranges.
        """
        cleaned: List[Dict[str, float]] = []

        for r in batch:
            if not isinstance(r, dict):
                continue
            if "temp" not in r or "hum" not in r or "press" not in r:
                continue

            try:
                temp = float(r["temp"])
                hum = float(r["hum"])
                press = float(r["press"])
            except (TypeError, ValueError, KeyError):
                continue

            if temp < -100 or temp > 100:
                continue
            if hum < 0 or hum > 100:
                continue
            if press < 1 or press > 7000:
                continue

            cleaned.append({"temp": temp, "hum": hum, "press": press})

        return cleaned

    def process(self, batch: List[Any]) -> None:
        """
        Process the cleaned sensor batch
        """
        print(f"Processing sensor batch: {batch}")

    def analysis(self, batch: List[Any]) -> None:
        """
        Print basic stats (count and average temperature)
        """
        avg = sum(r["temp"] for r in batch) / len(batch)
        print(f"Sensor analysis: {len(batch)} "
              f"readings processed, avg temp: {avg:.1f}°C")


class TransactionStream(DataStream):
    """
    Stream for financial transactions (buy/sell) with net flow analysis
    """
    def stream(self) -> None:
        """
        Print stream identifier and transaction type
        """
        print(f"Stream ID: {self.stream_id} (TRANSACTION)")

    def clean_batch(self, batch: List[Any]) -> List[Any]:
        """
        Normalize raw transactions.

        Accepts dicts with an 'amount' field, converts to float, and maps
        sign to operation type (buy/sell).
        """
        cleaned: List[Dict[str, Union[str, float]]] = []

        for tx in batch:
            if not isinstance(tx, dict):
                continue
            if "amount" not in tx:
                continue

            try:
                amount = float(tx["amount"])
            except (TypeError, ValueError):
                continue

            # Determine transaction type
            tx_type = "sell" if amount > 0 else "buy"
            cleaned.append({"amount": abs(amount), "type": tx_type})

        return cleaned

    def process(self, batch: List[Any]) -> None:
        """
        Process the cleaned transaction batch
        """
        print(f"Processing transaction batch: {batch}")

    def analysis(self, batch: List[Any]) -> None:
        """
        Print net flow and counts of buy vs sell operations
        """
        if not batch:
            print("Transaction analysis: No valid transactions")
            return

        total = 0
        for tx in batch:
            if tx["type"] == "sell":
                total -= tx["amount"]
            else:
                total += tx["amount"]
        buys = sum(1 for tx in batch if tx["type"] == "buy")
        sells = sum(1 for tx in batch if tx["type"] == "sell")

        print(f"Transaction analysis: {len(batch)} operations, "
              f"net flow: {total:.1f} units ({buys} buys, {sells} sells)")


class EventStream(DataStream):
    """
    Stream for text events (normalized strings) with error counting
    """
    def stream(self) -> None:
        """
        Print stream identifier and event type
        """
        print(f"Stream ID: {self.stream_id} (EVENT)")

    def clean_batch(self, batch: List[Any]) -> List[Any]:
        """
        Keep only non-empty strings, stripped and lowercased
        """
        cleaned: List[str] = []

        for ev in batch:
            if isinstance(ev, str):
                s = ev.strip().lower()
                if s:
                    cleaned.append(s)

        return cleaned

    def process(self, batch: List[Any]) -> None:
        """
        Process the cleaned event batch
        """
        print(f"Processing event batch: {batch}")

    def analysis(self, batch: List[Any]) -> None:
        """
        Print total events and how many are equal to 'error'.
        """
        errors = sum(1 for ev in batch if ev == "error")
        print(f"Event analysis: {len(batch)} events, {errors} error detected")


class StreamProcessor:
    """
    Registry and runner for multiple DataStream instances
    """
    def __init__(self) -> None:
        """
        Initialize an empty stream registry
        """
        self.streams: Dict[str, DataStream] = {}

    def add_stream(self, stream: DataStream) -> None:
        """
        Register a new stream by its stream_id.

        Raises:
            ValueError: If the stream_id already exists
        """
        if not isinstance(stream, DataStream):
            raise TypeError("Stream must be a DataStream instance")
        if stream.stream_id in self.streams:
            raise ValueError("This id already exists")
        self.streams[stream.stream_id] = stream

    def run_stream(self, stream_id: str, batch: List[Any]) -> None:
        """
        Run a batch through the selected stream.

        Raises:
            KeyError: If stream_id is not registered.
        """
        if stream_id not in self.streams:
            raise KeyError(f"Unknown stream id: {stream_id}")

        stream = self.streams[stream_id]
        try:
            stream.process_batch(batch)
        except Exception as exc:
            print(f"Stream error ({stream_id}): {exc}")

    def filter_high_priority(self,
                             stream_id: str,
                             batch: List[Any],
                             ) -> List[Any]:
        """
        Filter batch for high-priority data based on stream type
        Demonstrates stream-specific filtering
        """
        if stream_id not in self.streams:
            return []

        stream = self.streams[stream_id]

        if isinstance(stream, SensorStream):
            return [r for r in batch
                    if isinstance(r, dict) and
                    ("temp" in r and (r["temp"] > 50 or r["temp"] < -20))]

        elif isinstance(stream, TransactionStream):
            return [t for t in batch
                    if isinstance(t, dict) and
                    "amount" in t and abs(float(t["amount"])) >= 1000]

        elif isinstance(stream, EventStream):
            return [e for e in batch
                    if isinstance(e, str) and "error" in e.lower()]

        return batch


def main() -> None:
    """
    Function that tries different possibilities for the exercise
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sp = StreamProcessor()

    ss = SensorStream("SENSOR_001")
    ts = TransactionStream("TRANS_001")
    es = EventStream("EVENT_001")

    sp.add_stream(ss)
    sp.add_stream(ts)
    sp.add_stream(es)

    print("Initializing Sensor Stream...")
    sensor_data = [
        {"temp": 22.5, "hum": 65, "press": 1013},
        {"temp": 999, "hum": 50, "press": 1000},  # Invalid temp
        {"temp": 23.0, "hum": 70, "press": 1015}
    ]
    sp.run_stream("SENSOR_001", sensor_data)

    print("\nInitializing Transaction Stream...")
    transaction_data = [
        {"amount": 100},
        {"amount": -150},
        {"amount": "75.5"},
        {}  # Invalid
    ]
    sp.run_stream("TRANS_001", transaction_data)

    print("\nInitializing Event Stream...")
    event_data = ["login", "error", "logout", "", 123]
    sp.run_stream("EVENT_001", event_data)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    sensor_batch = [
        {"temp": 20, "hum": 50, "press": 1000},
        {"temp": 21, "hum": 55, "press": 1001}
    ]
    tx_batch = [
        {"amount": 100},
        {"amount": 200},
        {"amount": -50},
        {"amount": 75}
    ]
    event_batch = ["login", "error", "logout"]

    print("Batch 1 Results:")
    sp.run_stream("SENSOR_001", sensor_batch)
    sp.run_stream("TRANS_001", tx_batch)
    sp.run_stream("EVENT_001", event_batch)

    # Demonstrate filtering
    print("\nStream filtering active: High-priority data only")
    critical_sensors = sp.filter_high_priority("SENSOR_001", sensor_data)
    large_transactions = sp.filter_high_priority("TRANS_001", transaction_data)

    print(f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
          f"{len(large_transactions)} large transactions")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
