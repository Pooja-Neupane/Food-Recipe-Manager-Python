import json
import os

DATA_FILE = "recipes.json"

# ---------------------- Helper Functions ----------------------

def load_recipes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_recipes(recipes):
    with open(DATA_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

def print_heading(title):
    print("\n" + "="*50)
    print(f"{title.center(50)}")
    print("="*50 + "\n")

def input_list(prompt):
    items = input(prompt).split(',')
    return [item.strip() for item in items if item.strip()]

# ---------------------- Recipe Functions ----------------------

def add_recipe(recipes):
    print_heading("Add New Recipe")
    name = input("Enter the recipe name: ").strip()
    if name in recipes:
        print("⚠️ Recipe already exists! Choose a different name.\n")
        return

    ingredients = input_list("Enter ingredients (comma-separated): ")
    steps = input("Enter preparation steps:\n").strip()

    recipes[name] = {
        "ingredients": ingredients,
        "steps": steps
    }
    save_recipes(recipes)
    print(f"✅ '{name}' recipe added successfully!\n")

def view_recipe(recipes):
    print_heading("View a Recipe")
    name = input("Enter the recipe name: ").strip()
    recipe = recipes.get(name)
    if recipe:
        print(f"\n🍽️  Recipe: {name}")
        print("\n📝 Ingredients:")
        for i, ing in enumerate(recipe['ingredients'], 1):
            print(f"  {i}. {ing}")
        print("\n📋 Steps:")
        print(f"  {recipe['steps']}\n")
    else:
        print("❌ Recipe not found.\n")

def list_all_recipes(recipes):
    print_heading("All Available Recipes")
    if recipes:
        for name in sorted(recipes.keys()):
            print(f" - {name}")
        print()
    else:
        print("❌ No recipes available yet.\n")

def search_by_ingredient(recipes):
    print_heading("Search Recipes by Ingredient")
    search_term = input("Enter an ingredient to search: ").strip().lower()
    matches = [name for name, data in recipes.items()
               if any(search_term in ing.lower() for ing in data['ingredients'])]
    if matches:
        print("\n🍲 Recipes containing that ingredient:")
        for name in matches:
            print(f" - {name}")
        print()
    else:
        print("❌ No recipes found with that ingredient.\n")

# ---------------------- Main Menu ----------------------

def main():
    recipes = load_recipes()
    while True:
        print_heading("FOOD RECIPE MANAGER")
        print("1. ➕ Add New Recipe")
        print("2. 📖 View Recipe")
        print("3. 📋 List All Recipes")
        print("4. 🔍 Search by Ingredient")
        print("5. ❌ Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            add_recipe(recipes)
        elif choice == '2':
            view_recipe(recipes)
        elif choice == '3':
            list_all_recipes(recipes)
        elif choice == '4':
            search_by_ingredient(recipes)
        elif choice == '5':
            print("\n👋 Thank you for using the Recipe Manager. Goodbye!")
            break
        else:
            print("❗Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
