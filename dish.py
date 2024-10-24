# Ingredients
ingredients = {
    "fish": "500 grams",
    "salt": "1 tsp",
    "ginger_garlic_paste": "1 tbsp",
    "chili_powder": "1 tbsp",
    "oil": "for frying"
}

# Cooking steps
def fish_fry():
    print("Fish Fry Recipe")
    print("-----------------")
    print("Ingredients:")
    for item, amount in ingredients.items():
        print(f"{item}: {amount}")

    print("\nCooking Steps:")
    print("1. Clean and cut the fish into desired pieces.")
    print("2. In a bowl, mix salt, ginger garlic paste, and chili powder.")
    print("3. Marinate the fish with the spice mixture for at least 30 minutes.")
    print("4. Heat oil in a pan over medium heat.")
    print("5. Once the oil is hot, carefully place the marinated fish in the pan.")
    print("6. Fry until golden brown on both sides, about 5-7 minutes per side.")
    print("7. Remove the fish and drain on paper towels.")
    print("8. Serve hot with lemon wedges and your choice of side.")

# Run the recipe
fish_fry()
