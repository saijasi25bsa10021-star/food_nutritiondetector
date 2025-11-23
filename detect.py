# NOTE: Maybe check if camera exists? whatever, we'll see if it crashes
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera didn't open?? idk why")
    return None

print("Press SPACE to snap a picture. (Or ESC if you regret everything)")

the_frame_i_guess = None

# loopy loop; could be cleaner but this feels more 'handmade'
while True:
    ok, frame = cam.read()

    # Sometimes the cam lags—no idea why. Just retry.
    if not ok:
        # leaving print commented out because it's annoying
        # print("bad frame?")
        continue

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == 32:   # space bar = snapshot
        # copy the frame just in case it changes (old habit)
        the_frame_i_guess = frame.copy()
        break

    if key == 27:   # ESC
        cam.release()
        cv2.destroyAllWindows()
        # returning None because I don't feel like raising exceptions
        return None

# cleanup
cam.release()
cv2.destroyAllWindows()

# resizing — MobileNet needs 224x224… I always forget that number
try:
    resized = cv2.resize(the_frame_i_guess, (224, 224))
except Exception as e:
    print("weird resize error:", e)
    return None

# extra conversion that’s sort of unnecessary but I like doing it
resized = resized.astype(np.float32)

# now preprocess — I always forget if it wants RGB or BGR
# TODO: check if converting cv2 BGR to RGB improves predictions
arr = preprocess(resized)
arr = np.expand_dims(arr, axis=0)

# prediction time
# NOTE: predicting on CPU is slow but oh well
preds = model.predict(arr)

# decode top prediction — this indexing is confusing but it works…
top_label = decode(preds, top=1)[0][0][1]

# I should probably print the confidence too but meh
return top_label
