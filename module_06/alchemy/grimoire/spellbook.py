def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Docstring for record_spell
    """
    from .validator import validate_ingredients
    validation: str = validate_ingredients(ingredients)
    if "INVALID" in validation.split():
        return f"Spell rejected: {spell_name} ({validation})"
    return f"Spell recorded: {spell_name} ({validation})"
