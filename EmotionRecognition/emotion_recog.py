from fer import FER
import matplotlib.pyplot as plt 
import cv2

# --- 1. Capture the image ---
# initialize the camera
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error, show result
if result:
	# OFF - showing result, it take frame name and image output
	# imshow("GeeksForGeeks", image)

	# saving image in local storage
	cv2.imwrite("content/image_out.jpg", image)

	# OFF - If keyboard interrupt occurs, destroy image window
	# waitKey(0)
	# destroyWindow("GeeksForGeeks")
else:
	print("Error - No image detected")

# close the already opened camera
cam.release()

# --- 2. Load the image ---

image_in = plt.imread("content/image_out.jpg")
emo_detector = FER(mtcnn=True)

# --- 3. Capture all the emotions on the image ---
captured_emotions = emo_detector.detect_emotions(image_in)

# OFF - Print all captured emotions with the image
# print(captured_emotions)
# plt.imshow(test_image_one)

# Use the top_emotion() function to find the dominant emotion in the image
dominant_emotion, emotion_score = emo_detector.top_emotion(image_in)
print(dominant_emotion, emotion_score)

#-----------------------