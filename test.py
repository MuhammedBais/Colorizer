import cv2
prototxt = r"D:\Colorizer-master\models\models_colorization_deploy_v2.prototxt"
model = r"D:\Colorizer-master\models\colorization_release_v2.caffemodel"

try:
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    print("Model loaded successfully!")
except cv2.error as e:
    print("Error loading model:", e)
