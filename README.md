# food_nutritiondetector
Food Nutrient DetectovFood Nutrient Detector

A lightweight Python project that can run completely offline: detects food from an image and retrieves nutrition information from CSV files. Includes both a command-line interface, a simple Flask web user interface, and tools for loading and querying nutrition datasets.

Features
- Image-based food detection using MobileNetV2 ([detect.detect_food](detect.py)).
Nutrition lookup from CSV datasets ([lookup.get_nutrition](lookup.py), [food_utils.FoodUtil](food_utils.py)).
- A simple Flask web UI to upload images and show results: [app.py](app.py), [detect_and_lookup.py](detect_and_lookup.py), [index.html](index.html), [script.js](script.js), [style.css](style.css).
Methods to load and inspect the datasets: [data_loader.load_dataset](data_loader.py), [read.py](read.py), [food_nutrition.py](food_nutrition.py).

CSV datasets included: daily_food_nutrition_dataset.csv and nutrition_dataset.csv, see folder nutrition_dataset.csv/ and folder_datasets/.
## Repository structure
- [app.py](app.py) — Minimal Flask API endpoints using [lookup.get_nutrition](lookup.py) and [detect.detect_food](detect.py).
- [detect.py](detect.py) — Camera capture and MobileNetV2 inference (detect_food).
- [lookup.py](lookup.py) — CSV-based nutrition lookup (get_nutrition).
- [detect_and_lookup.py](detect_and_lookup.py) — Flask web application which overlays nutrition on images and serves the UI via the index route.
- [data_loader.py](data_loader.py) —CSV loader helper (load_dataset).
- [food_utils.py](food_utils.py) — FoodUtil helper class for dataset queries.
- [main.py](main.py) — CLI demo which captures image, detects food, and prints nutrition.
- [read.py](read.py), [food_nutrition.py](food_nutrition.py) - quick dataset inspection scripts.
- [index.html](index.html), [script.js](script.js), [style.css](style.css) — web UI files.
- Datasets :

- daily_food_nutrition_dataset.csv

nutrition_dataset.csv and the folder_datasets/ subfolder.
Quick start
1. Create Python virtual environment and install dependencies:
sh

python -m venv .venv

source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

(If there is no requirements.txt, install: flask opencv-python tensorflow pandas.)

2. Start the web app, simple UI:
sh

python detect_and_lookup.py

Open http://127.0.0.1:5000/
3. Run the minimal API (alternative):

sh

python app.py
- API endpoint: POST /get_nutrition uses [lookup.get_nutrition](lookup.py).
- JavaScript detection trigger calls /detect in the UI flow (script.js).
4. CLI demo:
sh
python main.py
This uses [detect.detect_food](detect.py) to capture an image from the webcam before looking up nutrition with [lookup.get_nutrition](lookup.py).
## Important code entry points (quick links)

- Detection: [detect.detect_food](detect.py) — captures from the webcam and returns the top label.
- Lookup: [lookup.get_nutrition](lookup.py) — reads daily_food_nutrition_dataset.csv.
- Dataset loader: [data_loader.load_dataset](data_loader.py)
- Web UI route: [detect_and_lookup.index](detect_and_lookup.py)

- UI template: [index.html](index.html)
- Client-side script: [script.js](script.js).

- Styling: [style.css](style.css).
- Helper class: [food_utils.FoodUtil](food_utils.py).
Data notes

- Expected dataset file names and locations:
- [daily_food_nutrition_dataset.csv](daily_food_nutrition_dataset.csv) (project root)
- [folder_datasets/nutrition_dataset.csv](folder_datasets/nutrition_dataset.csv)
- Loader [data_loader.load_dataset](data_loader.py) uses on_bad_lines="skip" when dealing with malformed CSV lines.

Usage patterns
Web UI: The user uploads an image and optionally types a food name. The top candidates along with an overlaid result image are returned by [detect_and_lookup.index](detect_and_lookup.py)
CLI: Run [main.py](main.py) to capture from the webcam, detect food, then query nutrition via [lookup.get_nutrition](lookup.py).
## Troubleshooting & tips

These would include checking that the camera drivers are accessible, and the device index is appropriate if cv2.VideoCapture(0) fails-try 1, 2, etc.
- If loading the dataset fails, ensure that daily_food_nutrition_dataset.csv is in your project root, or update paths in either [data_loader.py](data_loader.py) or [lookup.py](lookup.py).

The first time it runs, TensorFlow MobileNetV2 downloads. Be sure you have internet access during this initial download of the model (detect.py).

## Extending the project
- Enhance matching in [detect_and_lookup.find_candidates](detect_and_lookup.py) (for now, token&substring based)
Add better parsing and normalization of datasets in [data_loader.load_dataset](data_loader.py).
- Use a food-specific classifier or transfer learning instead of MobileNetV2 to enhance accuracy in the [detect.py](detect.py) file.
-Save user selections or history (for example, using a small SQLite database).
Tests & CI
- No unit tests are provided. Suggested tests:
- Dataset loader (data_loader.load_dataset)
- lookup functions (lookup.get_nutrition, food_utils.FoodUtil.get_nutrition)
- Candidate-finding logic detect_and_lookup.find_candidates
## License & Contributing
- Add your license file of choice.
Contributions can be made by forking the project, adding tests and features, then opening a pull request.
--- Project files: - [app.py](app.py) - [detect.py](detect.py) - [lookup.py](lookup.py) - [detect_and_lookup.py](detect_and_lookup.py) - [data_loader.py](data_loader.py) - [food_utils.py](food_utils.py) - [main.py](main.py) - [read.py](read.py) - [food_nutrition.py](food_nutrition.py) - [index.html](index.html) - [script.js](script.js) - [style.css](style.css) - [daily_food_nutrition_dataset.csv](daily_food_nutrition_dataset.csv) - [folder_datasets/nutrition_dataset.csv](folder_datasets/nutrition_dataset.csv)r



A lightweight Python project that can run completely offline: detects food from an image anFood Nutrient Detector

A lightweight Python project that can run completely offline: detects food from an image and retrieves nutrition information from CSV files. Includes both a command-line interface, a simple Flask web user interface, and tools for loading and querying nutrition datasets.

Features
- Image-based food detection using MobileNetV2 ([detect.detect_food](detect.py)).
Nutrition lookup from CSV datasets ([lookup.get_nutrition](lookup.py), [food_utils.FoodUtil](food_utils.py)).
- A simple Flask web UI to upload images and show results: [app.py](app.py), [detect_and_lookup.py](detect_and_lookup.py), [index.html](index.html), [script.js](script.js), [style.css](style.css).
Methods to load and inspect the datasets: [data_loader.load_dataset](data_loader.py), [read.py](read.py), [food_nutrition.py](food_nutrition.py).

CSV datasets included: daily_food_nutrition_dataset.csv and nutrition_dataset.csv, see folder nutrition_dataset.csv/ and folder_datasets/.
## Repository structure
- [app.py](app.py) — Minimal Flask API endpoints using [lookup.get_nutrition](lookup.py) and [detect.detect_food](detect.py).
- [detect.py](detect.py) — Camera capture and MobileNetV2 inference (detect_food).
- [lookup.py](lookup.py) — CSV-based nutrition lookup (get_nutrition).
- [detect_and_lookup.py](detect_and_lookup.py) — Flask web application which overlays nutrition on images and serves the UI via the index route.
- [data_loader.py](data_loader.py) —CSV loader helper (load_dataset).
- [food_utils.py](food_utils.py) — FoodUtil helper class for dataset queries.
- [main.py](main.py) — CLI demo which captures image, detects food, and prints nutrition.
- [read.py](read.py), [food_nutrition.py](food_nutrition.py) - quick dataset inspection scripts.
- [index.html](index.html), [script.js](script.js), [style.css](style.css) — web UI files.
- Datasets :

- daily_food_nutrition_dataset.csv

nutrition_dataset.csv and the folder_datasets/ subfolder.
Quick start
1. Create Python virtual environment and install dependencies:
sh

python -m venv .venv

source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

(If there is no requirements.txt, install: flask opencv-python tensorflow pandas.)

2. Start the web app, simple UI:
sh

python detect_and_lookup.py

Open http://127.0.0.1:5000/
3. Run the minimal API (alternative):

sh

python app.py
- API endpoint: POST /get_nutrition uses [lookup.get_nutrition](lookup.py).
- JavaScript detection trigger calls /detect in the UI flow (script.js).
4. CLI demo:
sh
python main.py
This uses [detect.detect_food](detect.py) to capture an image from the webcam before looking up nutrition with [lookup.get_nutrition](lookup.py).
## Important code entry points (quick links)

- Detection: [detect.detect_food](detect.py) — captures from the webcam and returns the top label.
- Lookup: [lookup.get_nutrition](lookup.py) — reads daily_food_nutrition_dataset.csv.
- Dataset loader: [data_loader.load_dataset](data_loader.py)
- Web UI route: [detect_and_lookup.index](detect_and_lookup.py)

- UI template: [index.html](index.html)
- Client-side script: [script.js](script.js).

- Styling: [style.css](style.css).
- Helper class: [food_utils.FoodUtil](food_utils.py).
Data notes

- Expected dataset file names and locations:
- [daily_food_nutrition_dataset.csv](daily_food_nutrition_dataset.csv) (project root)
- [folder_datasets/nutrition_dataset.csv](folder_datasets/nutrition_dataset.csv)
- Loader [data_loader.load_dataset](data_loader.py) uses on_bad_lines="skip" when dealing with malformed CSV lines.

Usage patterns
Web UI: The user uploads an image and optionally types a food name. The top candidates along with an overlaid result image are returned by [detect_and_lookup.index](detect_and_lookup.py)
CLI: Run [main.py](main.py) to capture from the webcam, detect food, then query nutrition via [lookup.get_nutrition](lookup.py).
## Troubleshooting & tips

These would include checking that the camera drivers are accessible, and the device index is appropriate if cv2.VideoCapture(0) fails-try 1, 2, etc.
- If loading the dataset fails, ensure that daily_food_nutrition_dataset.csv is in your project root, or update paths in either [data_loader.py](data_loader.py) or [lookup.py](lookup.py).

The first time it runs, TensorFlow MobileNetV2 downloads. Be sure you have internet access during this initial download of the model (detect.py).

## Extending the project
- Enhance matching in [detect_and_lookup.find_candidates](detect_and_lookup.py) (for now, token&substring based)
Add better parsing and normalization of datasets in [data_loader.load_dataset](data_loader.py).
- Use a food-specific classifier or transfer learning instead of MobileNetV2 to enhance accuracy in the [detect.py](detect.py) file.
-Save user selections or history (for example, using a small SQLite database).
Tests & CI
- No unit tests are provided. Suggested tests:
- Dataset loader (data_loader.load_dataset)
- lookup functions (lookup.get_nutrition, food_utils.FoodUtil.get_nutrition)
- Candidate-finding logic detect_and_lookup.find_candidates
## License & Contributing
- Add your license file of choice.
Contributions can be made by forking the project, adding tests and features, then opening a pull request.
--- Project files: - [app.py](app.py) - [detect.py](detect.py) - [lookup.py](lookup.py) - [detect_and_lookup.py](detect_and_lookup.py) - [data_loader.py](data_loader.py) - [food_utils.py](food_utils.py) - [main.py](main.py) - [read.py](read.py) - [food_nutrition.py](food_nutrition.py) - [index.html](index.html) - [script.js](script.js) - [style.css](style.css) - [daily_food_nutrition_dataset.csv](daily_food_nutrition_dataset.csv) - [folder_datasets/nutrition_dataset.csv](folder_datasets/nutrition_dataset.csv)d retrieves nutrition information from CSV files. Includes both a command-line interface, a simple Flask web user interface, and tools for loading and querying nutrition datasets.



Features

- Image-based food detection using MobileNetV2 ([detect.detect_food](detect.py)).

Nutrition lookup from CSV datasets ([lookup.get_nutrition](lookup.py), [food_utils.FoodUtil](food_utils.py)).

- A simple Flask web UI to upload images and show results: [app.py](app.py), [detect_and_lookup.py](detect_and_lookup.py), [index.html](index.html), [script.js](script.js), [style.css](style.css).

Methods to load and inspect the datasets: [data_loader.load_dataset](data_loader.py), [read.py](read.py), [food_nutrition.py](food_nutrition.py).



CSV datasets included: daily_food_nutrition_dataset.csv and nutrition_dataset.csv, see folder nutrition_dataset.csv/ and folder_datasets/.

## Repository structure

- [app.py](app.py) — Minimal Flask API endpoints using [lookup.get_nutrition](lookup.py) and [detect.detect_food](detect.py).

- [detect.py](detect.py) — Camera capture and MobileNetV2 inference (detect_food).

- [lookup.py](lookup.py) — CSV-based nutrition lookup (get_nutrition).

- [detect_and_lookup.py](detect_and_lookup.py) — Flask web application which overlays nutrition on images and serves the UI via the index route.

- [data_loader.py](data_loader.py) —CSV loader helper (load_dataset).

- [food_utils.py](food_utils.py) — FoodUtil helper class for dataset queries.

- [main.py](main.py) — CLI demo which captures image, detects food, and prints nutrition.

- [read.py](read.py), [food_nutrition.py](food_nutrition.py) - quick dataset inspection scripts.

- [index.html](index.html), [script.js](script.js), [style.css](style.css) — web UI files.

- Datasets :



- daily_food_nutrition_dataset.csv



nutrition_dataset.csv and the folder_datasets/ subfolder.

Quick start

1. Create Python virtual environment and install dependencies:

sh



python -m venv .venv



source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt



(If there is no requirements.txt, install: flask OpenCV-python tensorflow pandas.)



2. Start the web app, simple UI:

sh



python detect_and_lookup.py



Open http://127.0.0.1:5000/

3. Run the minimal API (alternative):



sh



python app.py

- API endpoint: POST /get_nutrition uses [lookup.get_nutrition](lookup.py).

- JavaScript detection trigger calls /detect in the UI flow (script.js).

4. CLI demo:

sh

python main.py

This uses [detect.detect_food](detect.py) to capture an image from the webcam before looking up nutrition with [lookup.get_nutrition](lookup.py).

## Important code entry points (quick links)



- Detection: [detect.detect_food](detect.py) — captures from the webcam and returns the top label.

- Lookup: [lookup.get_nutrition](lookup.py) — reads daily_food_nutrition_dataset.csv.

- Dataset loader: [data_loader.load_dataset](data_loader.py)

- Web UI route: [detect_and_lookup.index](detect_and_lookup.py)



- UI template: [index.html](index.html)

- Client-side script: [script.js](script.js).



- Styling: [style.css](style.css).

- Helper class: [food_utils.FoodUtil](food_utils.py).

Data notes



- Expected dataset file names and locations:

- [daily_food_nutrition_dataset.csv](daily_food_nutrition_dataset.csv) (project root)

- [folder_datasets/nutrition_dataset.csv](folder_datasets/nutrition_dataset.csv)

- Loader [data_loader.load_dataset](data_loader.py) uses on_bad_lines="skip" when dealing with malformed CSV lines.



Usage patterns

Web UI: The user uploads an image and optionally types a food name. The top candidates along with an overlaid result image are returned by [detect_and_lookup.index](detect_and_lookup.py)

CLI: Run [main.py](main.py) to capture from the webcam, detect food, then query nutrition via [lookup.get_nutrition](lookup.py).

## Troubleshooting & tips



These would include checking that the camera drivers are accessible, and the device index is appropriate if cv2.VideoCapture(0) fails-try 1, 2, etc.

- If loading the dataset fails, ensure that daily_food_nutrition_dataset.csv is in your project root, or update paths in either [data_loader.py](data_loader.py) or [lookup.py](lookup.py).



The first time it runs, TensorFlow MobileNetV2 downloads. Be sure you have internet access during this initial download of the model (detect.py).



## Extending the project

- Enhance matching in [detect_and_lookup.find_candidates](detect_and_lookup.py) (for now, token&substring based)

Add better parsing and normalization of datasets in [data_loader.load_dataset](data_loader.py).

- Use a food-specific classifier or transfer learning instead of MobileNetV2 to enhance accuracy in the [detect.py](detect.py) file.

-Save user selections or history (for example, using a small SQLite database).

Tests & CI

- No unit tests are provided. Suggested tests:

- Dataset loader (data_loader.load_dataset)

- lookup functions (lookup.get_nutrition, food_utils.FoodUtil.get_nutrition)

- Candidate-finding logic detect_and_lookup.find_candidates

## License & Contributing

- Add your license file of choice.

Contributions can be made by forking the project, adding tests and features, then opening a pull request.

--- Project files: - [app.py](app.py) - [detect.py](detect.py) - [lookup.py](lookup.py) - [detect_and_lookup.py](detect_and_lookup.py) - [data_loader.py](data_loader.py) - [food_utils.py](food_utils.py) - [main.py](main.py) - [read.py](read.py) - [food_nutrition.py](food_nutrition.py) - [index.html](index.html) - [script.js](script.js) - [style.css](style.css) - [daily_food_nutrition_dataset.csv](daily_food_nutrition_dataset.csv) - [folder_datasets/nutrition_dataset.csv](folder_datasets/nutrition_dataset.csv)

