import cv2

# Read the image
image = cv2.imread('hello.png')

# # ⁡⁢⁣⁢Display the image in a window⁡
# cv2.imshow('abc', image)

# # ⁡⁢⁣⁢Save the image to disk⁡
# cv2.imwrite('world.png', image)

# ⁡⁢⁣⁢convert image color⁡
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow("abc", gray_image)

# ⁡⁢⁣⁢resizing image⁡
# resized = cv2.resize(image, (800, 600))
# cv2.imshow("an0", resized)

# ⁡⁢⁣⁢draw a rectangle⁡
# cv2.rectangle(image, (50,50), (200,200), (0, 255, 0), 3)
# cv2.circle(image, (100,250), 50, (255,0,0), 2)
# cv2.putText(image, "Hello World", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255,0), 2)
# cv2.imshow("abc", image)

# ⁡⁢⁣⁢blur image⁡
# blur = cv2.blur(image, (5, 5))
# cv2.imshow("blur image", blur)

#video play
# Load the video file
cap = cv2.VideoCapture("video.mp4")

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was read successfully
    if not ret:
        break

    # Display the frame
    cv2.imshow("Video Playback", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()


