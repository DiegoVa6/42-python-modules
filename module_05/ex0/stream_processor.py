from typing import Any, List


class DataProcessor:
    """
    Main class to process data
    """
    def process(self, data: Any) -> str:
        """
        process information, calling validate and format_output
        """
        try:
            print(f"Processing data: {data}")
            self.validate(data)
            return self.format_output(data)
        except Exception as exc:
            return f"Error processing data: {exc}"

    def validate(self, data: Any) -> None:
        """
        default validate, accepts anything
        """
        return None

    def format_output(self, data: Any) -> str:
        """
        default format_output returns anything passed as data
        """
        return f"Output: {data}"


class NumericProcessor(DataProcessor):
    """
    DataProcessor child to process numeric lists
    """
    def validate(self, data: Any) -> None:
        """
        checks that data is a list and all elements are int/float (or castable)
        """
        try:
            total_elements = len(data)
            if total_elements == 0:
                raise ValueError("List cannot be empty")
            sum(data)
        except TypeError as exc:
            message = "NumericProcessor expects a list of numbers"
            raise TypeError(message) from exc

    def format_output(self, data: List) -> str:
        """
        returns the correct format of the searched format_output
        """
        return (f"Output: Processed {len(data)} numeric values, "
                f"sum={sum(data)}, avg={sum(data)/len(data)}")


class TextProcessor(DataProcessor):
    """
    Docstring for TextProcessor, DataProcessor's child, process strings
    """
    def validate(self, data: str) -> None:
        """
        TextProcessor validation of data, 1 string
        """
        try:
            data.split(" ")
        except Exception as exc:
            raise TypeError("TextProcessor expects a string") from exc
        print("Validation: Text data verified")

    def format_output(self, data: str) -> str:
        """
        TextProcessor correct format for the output
        """
        words = len(data.split(" "))
        return f"Output: Processed text: {len(data)} characters, {words} words"


class LogProcessor(DataProcessor):
    """
    DataProcessor child to process log entries like 'LEVEL: message'
    """
    def validate(self, data: Any) -> None:
        """
        LogProcessor validate, 1 string with : in between
        """
        try:
            parts = data.split(":", 1)
        except Exception as exc:
            message = "LogProcessor expects a string like 'LEVEL: message'"
            raise TypeError(message) from exc

        if len(parts) != 2:
            raise ValueError("Log entry must contain ':' separator")

        if parts[0] == "" or parts[1] == "":
            int("abc")
        print("Validation: Log entry verified")

    def format_output(self, data: Any) -> str:
        """
        LogProcessor correct format for the output
        """
        parts = data.split(":", 1)
        return f"Output: [{parts[0]}] {parts[0]} level detected:{parts[1]}"


def main() -> None:
    """
    Function that tries different possibilities for the exercise
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    dp = NumericProcessor()
    lst = [1, 2, 3, 4, 5]
    print(dp.process(lst), "\n")

    print("Initializing Text Processor...")
    tp = TextProcessor()
    text = "Hola mundo desde 42"
    print(tp.process(text), "\n")

    print("Initializing Log Processor...")
    lp = LogProcessor()
    log = "ERROR: something went wrong"
    print(lp.process(log), "\n")

    print("=== Error cases ===")
    print(dp.process(["1", "2", "x"]))
    print(tp.process(123))
    print(lp.process("INFO no colon here"), "\n")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    inputs: List[Any] = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    idx = 1
    for proc, item in zip(processors, inputs):
        result = proc.process(item)
        print(f"Result {idx}: {result}")
        idx += 1


if __name__ == "__main__":
    main()
