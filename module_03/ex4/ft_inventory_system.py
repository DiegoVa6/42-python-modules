def show_inventory(catalog, players):
    """
    Docstring for show_inventory
    This function will show every item of every player.
    """
    for ply, items in players.items():
        total_items = 0
        inv_value = 0
        categories = {"weapon": 0, "consumable": 0, "armor": 0, "accessory": 0}

        print(f"\n=== {ply}'s Inventory ===")

        for item, qt in items.items():
            if qt <= 0:
                continue
            info = catalog.get(item)
            if info is None:
                continue
            item_type = info.get("type")
            rarity = info.get("rarity")
            value = info.get("value")
            total_items += qt
            inv_value += qt * value
            categories[item_type] = categories.get(item_type, 0) + qt
            print(f"{item} ({item_type}, {rarity}): "
                  f"{qt}x @ {value} gold each = {qt*value} gold")
        print(f"\nInventory value: {inv_value} gold")
        print(f"Item count: {total_items} items")
        print("Categories: ", end='')
        first = True
        for cat, qty in categories.items():
            if qty > 0:
                if not first:
                    print(", ", end="")
                print(f"{cat}({qty})", end="")
                first = False
        print()


def transaction(players, sender, receiver, item, qty):
    """
    Function to make transaction between 2 players
    """
    sender_inv = players.get(sender)
    receiver_inv = players.get(receiver)

    if sender_inv is None or receiver_inv is None:
        return False
    if qty <= 0:
        return False

    available = sender_inv.get(item, 0)
    if available < qty:
        return False

    sender_inv[item] = available - qty
    receiver_inv[item] = receiver_inv.get(item, 0) + qty
    return True


def inventory_value(inv, catalog):
    """
    Calculates inventory value
    """
    total = 0
    for item, qty in inv.items():
        value = catalog.get(item, {}).get("value", 0)
        total += qty * value
    return total


def item_count(inv):
    """
    Counts number of objects in your inventory
    """
    total = 0
    for qty in inv.values():
        total += qty
    return total


def rarest_items_text(catalog):
    """
    Return a comma-separated string of items whose rarity is 'rare'.
    """
    text = ""
    first = True
    for item_name, info in catalog.items():
        if info.get("rarity") == "rare":
            if not first:
                text += ", "
            text += item_name
            first = False
    return text


if __name__ == "__main__":
    print("=== Player Inventory System ===")
    catalog = {
        "sword": {"type": "weapon", "rarity": "rare", "value": 500},
        "potion": {"type": "consumable", "rarity": "common", "value": 50},
        "shield": {"type": "armor", "rarity": "uncommon", "value": 200},
        "magic_ring": {"type": "accessory", "rarity": "rare", "value": 900},
    }
    players = {
        "alice": {"sword": 1, "potion": 5, "shield": 1},
        "bob":   {"magic_ring": 1},
    }
    show_inventory(catalog, players)
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    ok = transaction(players, "alice", "bob", "potion", 2)
    if not ok:
        print("Transaction failed!")
    else:
        print("Transaction successful!")
        print("\n=== Updated Inventories ===")
        print(f"Alice potions: {players['alice'].get('potion', 0)}")
        print(f"Bob potions: {players['bob'].get('potion', 0)}")

    print("\n=== Inventory Analytics ===")

    most_val_name = ""
    most_val = -1

    for name, inv in players.items():
        val = inventory_value(inv, catalog)
        if val > most_val:
            most_val = val
            most_val_name = name

    print(f"Most valuable player: {most_val_name} ({most_val} gold)")

    most_items_name = ""
    most_items = -1

    for name, inv in players.items():
        cnt = item_count(inv)
        if cnt > most_items:
            most_items = cnt
            most_items_name = name

    print(f"Most items: {most_items_name} ({most_items} items)")

    print(f"Rarest items: {rarest_items_text(catalog)}")
