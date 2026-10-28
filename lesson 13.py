def build_custom_drink( drink_type, *toppings, **customizations):
    print(f"\n--- Order: {drink_type} ---")
    for x in toppings:
        if x == toppings:
            print("toppings:")
        else:
            print("toppings: none")
            for key, value in customizations.items():
                print(f"  - {key}: {value}")
                if customizations:
                    print("customizations:")
                else:
                    print("customizations: stanadard defualt")

build_custom_drink("Iced Mocha", "whipped cream", "chocolate drizzle")
build_custom_drink("Latte", "vanilla syrup", "cinnamon", milk="oat", temperature="extra hot")
build_custom_drink("Espresso")