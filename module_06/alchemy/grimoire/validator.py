def validate_ingredients(ingredients: str) -> str:
    """
    Docstring for validate_ingredients
    """
    for ing in ingredients.split():
        if ing not in ["fire", "water", "earth", "air"]:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
