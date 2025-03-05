import cv2
import os
import numpy as np  # Needed to concatenate images

### STEP 1: CHECK CAMERA AVAILABILITY AND INDEX ###

# Check available video devices on terminal using: ls /dev/video*
# Example Output: /dev/video0  /dev/video2  /dev/video4 (where video4 is the laptop's webcam)

# Check available camera indices
for i in range(5):  # Check up to 5 possible camera indices
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"\nCamera {i} is available -->")

        # Get supported resolutions
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        print(f"Default Resolution: {int(width)}x{int(height)}")

        # Set resolution to maximum available
        # Setting 9999 forces OpenCV to find the highest available resolution.
        # Useful when you don’t know the max resolution beforehand.
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 9999)  # Use a high number
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 9999)

        # Read actual resolution after setting
        max_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        max_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        print(f"Max Resolution: {int(max_width)}x{int(max_height)}")

        cap.release()
    else:
        print(f"\nCamera {i} is NOT available")

# Based on results, external webcams are at index 2 and 4
# Default resolution for all the cameras are 640x480
# Maximum resolution for 1 external cameras is 1280x720 but for others it is 640x480
# We will set resolution to 640x480 for consistency

### STEP 2: OPEN BOTH CAMERAS AND DISPLAY SIDE-BY-SIDE OUTPUT ###

# Open the two external cameras
cap_left = cv2.VideoCapture(2)  # First webcam
cap_right = cv2.VideoCapture(4)  # Second webcam

# Set resolution (optional but recommended for consistency)
cap_left.set(3, 640)  # Width
cap_left.set(4, 480)  # Height
cap_right.set(3, 640)
cap_right.set(4, 480)

# Ensure cameras are opened successfully
if not cap_left.isOpened() or not cap_right.isOpened():
    print("Error: Could not open one or both cameras.")
    exit()

# Create directories for saving images
os.makedirs("left", exist_ok=True)
os.makedirs("right", exist_ok=True)

img_count = 0  # Counter for saved images

while True:
    # Capture frames from both cameras
    retL, frameL = cap_left.read()
    retR, frameR = cap_right.read()

    if not retL or not retR:
        print("Error: Could not read frames.")
        break

    # Concatenate left and right images side by side
    combined_frame = np.hstack((frameL, frameR))  # Horizontally stack images

    # Display the combined frame
    cv2.imshow("Stereo Camera Output (Left | Right)", combined_frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Press 's' to save images
        cv2.imwrite(f"left/left_{img_count}.jpg", frameL)
        cv2.imwrite(f"right/right_{img_count}.jpg", frameR)
        print(f"Saved left_{img_count}.jpg and right_{img_count}.jpg")
        img_count += 1  # Increment counter

    elif key == ord('q'):  # Press 'q' to exit
        break

# Release the cameras and close windows
cap_left.release()
cap_right.release()
cv2.destroyAllWindows()


# Measurements
# Right Cam to Robot = 107 cm 
# Left Cam to Robot = 103 cm
# Distance between the two cameras = 18 cm