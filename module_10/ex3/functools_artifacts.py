import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)
    raise ValueError("Invalid operation")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant":
        functools.partial(base_enchantment, power=50, element="fire"),
        "ice_enchant":
        functools.partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant":
        functools.partial(base_enchantment, power=50, element="lightning")
    }


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment with power {power} on {target}"


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n in {0, 1}:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast_spell(value) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(value: int) -> str:
        return f"Damage spell cast with power {value}"

    @cast_spell.register
    def _(value: str) -> str:
        return f"Enchantment spell cast on {value}"

    @cast_spell.register
    def _(value: list) -> str:
        return f"Multi-cast spell with {len(value)} spells"

    return cast_spell


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
