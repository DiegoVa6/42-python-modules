def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combination(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combination


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplification(*args, **kwargs) -> int | float | str:
        return (base_spell(*args, **kwargs) * multiplier)
    return amplification


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cond(*args, **kwargs) -> str:
        if (condition(*args, **kwargs) is True):
            return (spell(*args, **kwargs))
        return ("Spell fizzled")
    return (cond)


def spell_sequence(spells: list[callable]) -> callable:
    def spell_cast(*args, **kwargs) -> list:
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return (results)
    return (spell_cast)


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def base_damage(x: int) -> int:
    return x


def enough_mana(mana: int) -> bool:
    return mana >= 10


def lightning(target: str) -> str:
    return f"Lightning strikes {target}"


def ice(target: str) -> str:
    return f"Ice freezes {target}"


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon")
    print(f"Combined spell result: {result1}, {result2}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(base_damage, 3)
    original = base_damage(10)
    amplified_result = amplified(10)
    print(f"Original: {original}, Amplified: {amplified_result}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(enough_mana, fireball)
    print(safe_fireball(15))
    print(safe_fireball(5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning, ice])
    print(sequence("Dragon"))


if __name__ == "__main__":
    main()
