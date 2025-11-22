from detect import detect_food
from lookup import get_nutrition

food = detect_food()

if food is None:
    print("No food detected.")
    exit()

print(f"Detected Food: {food}")

nutrition = get_nutrition(food)

if nutrition:
    print("\nNutrition Info:")
    for k, v in nutrition.items():
        print(f"{k}: {v}")
else:
    print("Food not found in nutrition dataset.")
