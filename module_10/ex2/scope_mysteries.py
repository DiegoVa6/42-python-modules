def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def more_power(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return more_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> dict[str, callable]:
    memory: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    a = mage_counter()
    print("Call 1:", a())
    print("Call 2:", a())
    print("Call 3:", a())

    print("\nTesting spell accumulator...")
    a = spell_accumulator(10)
    print(a(5))   # 15
    print(a(3))   # 18
    print(a(-2))  # 16

    print("\nTesting enchantment factory...")
    a = enchantment_factory("Flaming")
    print(a("Sword"))
    print(a("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Storing key: fireball")
    vault["store"]("key", "fireball")
    print("Recall from key")
    print(vault["recall"]("key"))


if __name__ == "__main__":
    main()
