import mediapipe as mp
import cv2

photo = cv2.imread("LEBRON_FACE.PNG")
model_path = "face_landmarker.task"
print(model_path)


#------------------------------------
BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions

options = FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path=model_path), num_faces =1)
detector = FaceLandmarker.create_from_options(options)
print("Face Landmarker initialized successfully")
#------------------------------------

image = mp.Image.create_from_file("LEBRON_FACE.PNG")
print(image.width , image.height)

#-------------------------------------

result = detector.detect(image)

print("Number of detected face", len(result.face_landmarks))

if len(result.face_landmarks) >0:
    print("Number of facial landmarks detected: ",len(result.face_landmarks[0]))

#---------------------------------------

if len(result.face_landmarks) > 0:
    forehead = result.face_landmarks[0][10]
    left_cheek = result.face_landmarks[0][205]
    right_cheek = result.face_landmarks[0][425]

    pixel_x = int(forehead.x * image.width)
    pixel_y = int(forehead.y * image.height)

    left_x = int(left_cheek.x * image.width)
    left_y = int(left_cheek.y * image.height)

    right_x = int(right_cheek.x * image.width)
    right_y = int(right_cheek.y * image.height)

    # Read original skin colours BEFORE drawing
    pixel_left_cheek = photo[left_y, left_x]
    pixel_right_cheek = photo[right_y, right_x]
    pixel_forehead = photo[pixel_y, pixel_x]

    print(f"Left cheek BGR: {pixel_left_cheek}")
    print(f"Right cheek BGR: {pixel_right_cheek}")
    print(f"Forehead BGR: {pixel_forehead}")

    # Draw landmark dots
    cv2.circle(photo, (left_x, left_y), 5, (0, 0, 255), -1)
    cv2.circle(photo, (right_x, right_y), 5, (0, 0, 255), -1)
    cv2.circle(photo, (pixel_x, pixel_y), 5, (0, 255, 0), -1)

    # Display image
    cv2.imshow("Forehead and Cheek Detection", photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




#---------------------------------------







