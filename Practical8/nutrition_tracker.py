class FoodItem:
    """Class to represent a food item with nutritional information"""
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat


def calculate_daily_nutrition(food_list):
    """
    Calculate total nutrition intake from a list of FoodItem objects in 24 hours
    Show warnings if calorie or fat intake exceeds limits
    :param food_list: List of FoodItem instances
    :return: Total calories, protein, carbs, fat
    """
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    # Sum all nutrients
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    # Display summary
    print("\n===== 24-Hour Nutrition Summary =====")
    print(f"Total calories: {total_calories} kcal")
    print(f"Total protein: {total_protein} g")
    print(f"Total carbohydrates: {total_carbs} g")
    print(f"Total fat: {total_fat} g")

    # Warnings for excess intake
    if total_calories > 2500:
        print("=== Warning: Calorie intake exceeds 2500 kcal")
    if total_fat > 90:
        print("=== Warning: Fat intake exceeds 90 g")

    return total_calories, total_protein, total_carbs, total_fat

# Create food items
apple = FoodItem("Apple", 60, 0.3, 15, 0.5)
rice = FoodItem("Rice", 130, 2.7, 28, 0.3)
chicken = FoodItem("Chicken breast", 165, 31, 0, 3.6)

# Daily food list
daily_food = [apple, rice, chicken, rice, chicken]

# Calculate and display nutrition
calculate_daily_nutrition(daily_food)