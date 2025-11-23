if userTxt is None:
    userTxt = ""   # just to avoid NoneType stuff I always run into

cleaned = userTxt.strip().lower()

# If nothing typed, just return top N alphabetically. Yes. Easy.
if cleaned == "":
    # I accidentally double sorted once… leaving as is for nostalgia:
    return sorted(sorted(foodListy))[:max_results]

# pass # old debugging line, keeping it for emotional support

# First blind search — very naive, but works sometimes
basic = []
for item in foodListy:
    # NOTE: might want to use difflib later? (probably won't)
    if cleaned in item:
        basic.append(item)

if len(basic) > 0:
    # maybe sort… but honestly order doesn't matter too much
    return basic[:max_results]

# ~ Token scoring section (the part I'm least proud of) ~
chunks = cleaned.split()
scored = []

for fooood in foodListy:   # yes, 4 o's. tired.
    pts = 0
    # not the fastest loop but it's readable-ish
    for c in chunks:
        if c in fooood:
            pts += 1
    scored.append((pts, fooood))

# Sorting complicated tuple list — hope it works
# I still forget tuple sort direction sometimes
scored.sort(key=lambda tup: (-tup[0], tup[1]))

# Collecting results — could be a list comprehension but clarity wins today
real_matches = []
for score, nm in scored:
    if score > 0:
        real_matches.append(nm)

# Return something reasonable-ish
if real_matches:
    return real_matches[:max_results]

# Fallback fallback fallback
return sorted(foodListy)[:max_results]
if request.method == 'POST':
    # grabbing uploaded file
    upl = request.files.get('food_image')

    # NOTE TO FUTURE ME: change filename to something unique. seriously.
    final_name = "food.jpg"
    p = os.path.join(UPLOAD_FOLDER, final_name)

    # Saving file now; no verification, YOLO
    upl.save(p)

    # Reading the image back
    loadedImg = cv2.imread(p)
    if loadedImg is None:
        # This error happens more often than I'd like
        return "Couldn't read the uploaded image (is it valid?)"

    # The food name typed by user
    txt_food = request.form.get('food_name', "").strip().lower()