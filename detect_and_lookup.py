import os
import cv2
from flask import Flask, render_template, request
from data_loader import load_metadata

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Default metadata folder
METADATA_FOLDER = os.path.join("folder_datasets", "FINAL FOOD DATASET", "METADATA")

# Load metadata
df, lookup, food_col = load_metadata(METADATA_FOLDER)
food_names = sorted(list(lookup.keys()))

def find_candidates(food_names, query, max_results=10):
    q = query.strip().lower()
    if not q:
        return sorted(food_names)[:max_results]
    matches = [n for n in food_names if q in n]
    if matches:
        return matches[:max_results]
    q_tokens = q.split()
    scored = []
    for n in food_names:
        score = sum(1 for t in q_tokens if t in n)
        scored.append((score, n))
    scored = sorted(scored, key=lambda x: (-x[0], x[1]))
    results = [n for s, n in scored if s>0]
    if results:
        return results[:max_results]
    return sorted(food_names)[:max_results]

def overlay_text(img, lines, x=10, y=30, line_height=24):
    for i, line in enumerate(lines):
        cv2.putText(img, line, (x, y + i*line_height),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2, cv2.LINE_AA)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_img_url = None
    nutrition_info = None
    candidates = None

    if request.method == 'POST':
        file = request.files['food_image']
        filename = 'food.jpg'
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Read uploaded image
        img = cv2.imread(file_path)
        if img is None:
            return "Error: Could not read uploaded image."

        # Get food name input from form
        query = request.form.get('food_name', '').strip().lower()
        candidates = find_candidates(food_names, query, max_results=10)

        if candidates:
            selected = candidates[0]  # pick first candidate by default
            info = lookup.get(selected, {})
            nutrition_info = { 
                'food': selected,
                'calories': info.get('caloric_value', 'N/A'),
                'carbs': info.get('carbohydrates', 'N/A'),
                'fat': info.get('fat', 'N/A'),
                'protein': info.get('protein', 'N/A'),
                'fiber': info.get('dietary_fiber', 'N/A')
            }

            # Overlay nutrition info on image
            lines = [f"Food: {selected.upper()}"]
            for key, val in nutrition_info.items():
                if key != 'food':
                    lines.append(f"{key.capitalize()}: {val}")
            overlay_text(img, lines, x=10, y=30, line_height=26)

            # Save result image
            result_path = os.path.join(UPLOAD_FOLDER, 'result.jpg')
            cv2.imwrite(result_path, img)
            result_img_url = result_path

    return render_template('index.html', img_url=result_img_url, nutrition=nutrition_info, candidates=candidates)
    
if __name__ == "__main__":
    app.run(debug=True)
