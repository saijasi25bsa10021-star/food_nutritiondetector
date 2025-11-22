from flask import Flask, render_template, request, jsonify
from lookup import get_nutrition
from detect import detect_food

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_nutrition', methods=['POST'])
def get_food_nutrition():
    food_name = request.json.get('food')
    nutrition = get_nutrition(food_name)
    if nutrition:
        return jsonify(nutrition)
    else:
        return jsonify({"error": "Food not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

