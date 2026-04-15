from alchemy.grimoire import record_spell, validate_ingredients

print("=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
print(f'validate_ingredients("fire air"): '
      f'{validate_ingredients("fire air")}')
print(f'validate_ingredients("dragon scales"): '
      f'{validate_ingredients("dragon scales")}\n')

print("Testing spell recording with validation:")
print(f'record_spell("Fireball", "fire air"): '
      f'{record_spell("Fireball", "fire air")}')
print(f'record_spell("Dark Magic", "shadow"): '
      f'{record_spell("Dark Magic", "shadow")}\n')

print("Testing late import technique:")
print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
