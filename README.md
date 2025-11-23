# Food nutrition detector

 it is python project that can run offline .This detects food from an image and retrieves nutrition information from dataset csv file

 # Features

 1 it can detect food through image using MobileNetV2
 (detect.detect_food)
 2 it further lookup nutrition fromm csv datasets using lookup.py and food_utils.py

3 we use web UI for image upload and for displaying result using app.py,detect_and_lookup.py,index.html,script.jds,style.css

4 we are loading dataset and inspection through data_loader.py,read.py,food_nutrition.py.

5 In this project  we use two CSV datasets such as daily_food_nutrition_dataset.csv and nutrition_dataset.csv

# Repository Structure

1 app.py - we use this for minimal flask API endpoints using detection & lookup

2 detect.py - we use this for webcam capture and MobileNetV2 inference

3 lookup.py - we use it for CSV based nutrition lookups

4 detect_and_lookup.py - we use this  to flask web app from overlaying nutrition info on images

5 data_loader.py– we use this  to load CSV datasets.

6 food_utils.py – it helpes class for dataset queries.

7 main.py – it captures image, detects food, and prints nutritions

8 read.py / food_nutrition.py – it use to quiqly inspects on scripts

 9 index.html / script.js / style.css – files to develop web UI

10 Datasets:

daily_food_nutrition_dataset.csv

folder_datasets/nutrition_dataset.csv


# Quick Start

1  to Set up Python environment

python -m venv .venv

source .venv/bin/activate 
 
pip install -r requirements.txt



2  to Start web UI

python detect_and_lookup.py
Open: http://127.0.0.1:5000/

3 to Run minimal API

python app.py


*POST /get_nutrition → lookup.get_nutrition

/detect → JavaScript triggers detection in UI

4 to Run CLI demo

python main.py

*Captures image from webcam → detects food → retrieves nutrition info.

# Important Code Entry Points

Detection: detect.detect_food

Lookup: lookup.get_nutrition

Dataset loader: data_loader.load_dataset

Web UI route: detect_and_lookup.index

UI template / JS / CSS: index.html
, script.js
, style.css

Helper class: food_utils.FoodUtil

# Data Notes

Expected dataset locations:

daily_food_nutrition_dataset.csv (root)

folder_datasets/nutrition_dataset.csv

Loader uses on_bad_lines="skip" for malformed CSV rows.

# Usage Patterns

* Web UI: it upload image and then find optional food name  and then return

* CLI: Run main.py → webcam capture → detect food → query nutrition.

# Troubleshooting

Camera issues: Check drivers or try cv2.VideoCapture(1) / 2 if 0 fails.

Dataset loading fails: Ensure CSV files are in correct paths.

MobileNetV2 download: First run requires internet.

Extending the Project

Improve matching in detect_and_lookup.find_candidates.

Normalize datasets better in data_loader.load_dataset.

Use transfer learning or food-specific classifier for higher accuracy.

Save user history (e.g., SQLite DB).

Tests & CI Suggestions

Dataset loader (data_loader.load_dataset
)

Lookup functions (lookup.get_nutrition
, FoodUtil.get_nutrition)

Candidate-finding logic (detect_and_lookup.find_candidates
)