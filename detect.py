import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.applications.MobileNetV2(weights="imagenet")

decode = tf.keras.applications.mobilenet_v2.decode_predictions
preprocess = tf.keras.applications.mobilenet_v2.preprocess_input

def detect_food():
    cap = cv2.VideoCapture(0)
    print("Press SPACE to capture")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)
        if key == 32:  # space
            img = frame
            break
        if key == 27:  # ESC
            cap.release()
            cv2.destroyAllWindows()
            return None

    cap.release()
    cv2.destroyAllWindows()

    img_resized = cv2.resize(img, (224,224))
    arr = preprocess(img_resized.astype(np.float32))
    arr = np.expand_dims(arr, 0)

    preds = model.predict(arr)
    label = decode(preds, top=1)[0][0][1]  # top-1 label

    return label

