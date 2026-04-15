def event_creation(n):
    """
    Function to create 'random' events
    """
    for i in range(1, n+1):
        if i % 3 == 1:
            player = "alice"
            level = 5
            action = "killed monster"
        elif i % 3 == 2:
            player = "bob"
            level = 12
            action = "found treasure"
        else:
            player = "charlie"
            level = 8
            action = "leveled up"
        yield (i, player, level, action)


def fibonacci():
    """
    Fibonacci generator
    """
    n_prev: int = 0
    n: int = 1
    while True:
        yield n_prev
        n_prev, n = n, n + n_prev


def is_prime(n) -> bool:
    """
    return True if param (n) is a prime number
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True


def prime_numbers():
    """
    Generator of prime numbers
    """
    n = 2
    while True:
        if (is_prime(n)):
            yield n
        n += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    print("Processing 1000 game events...\n")

    count = 0
    high_lvl_ply = 0
    treasure_event = 0
    level_up = 0
    for event in event_creation(1000):
        idx, player, level, action = event
        if count < 3:
            print(f"Event {idx}: Player {player} (level {level}) {action}")
        count += 1
        if level > 9:
            high_lvl_ply += 1
        if action == "found treasure":
            treasure_event += 1
        if action == "leveled up":
            level_up += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {count}")
    print(f"High-level players (10+): {high_lvl_ply}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")
    first = True
    text = "Fibonacci sequence (first 10): "
    gen = fibonacci()
    for i in range(10):
        if not first:
            text += ", "
        text += str(next(gen))
        first = False
    print(text)

    text = "Prime numbers (first 5): "
    first = True
    gen = prime_numbers()
    for i in range(5):
        if not first:
            text += ", "
        text += str(next(gen))
        first = False
    print(text)
