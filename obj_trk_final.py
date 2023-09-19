import cv2
import numpy as np

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture('footvolleyball.mp4') 

# Define the tracker type, you can choose from various trackers available in OpenCV
tracker = cv2.TrackerCSRT_create()

# Initialize variables for trajectory
trajectory = []

# Function to draw a bounding box around the object
def drawBox(img, bbox):
    x, y, w, h = map(int, bbox)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Function to track the object and plot the trajectory
def goal_track(img, bbox):
    x, y, w, h = map(int, bbox)
    x_center = x + w // 2
    y_center = y + h // 2

    # Append the center of the object to the trajectory list
    trajectory.append((x_center, y_center))

    # Plot the trajectory
    for point in trajectory:
        cv2.circle(img, point, 3, (0, 0, 255), -1)

while True:
    success, img = cap.read()

    if not success:
        print("Video ended or not found.")
        break

    # Update the tracker with the current frame
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "LOST", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    goal_track(img, bbox)

    cv2.imshow("Object Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
