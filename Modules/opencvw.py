import cv2


# ============================================================
# 1. READ / LOAD IMAGE
# ============================================================

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Image loaded successfully")


# ============================================================
# 2. IMAGE INFORMATION
# ============================================================

print("\nIMAGE INFORMATION")

print("Shape:", image.shape)
print("Height:", image.shape[0])
print("Width:", image.shape[1])
print("Channels:", image.shape[2])

print("Total pixels:", image.size)
print("Data type:", image.dtype)


# ============================================================
# 3. DISPLAY IMAGE
# ============================================================

cv2.imshow("Original Image", image)


# ============================================================
# 4. RESIZE IMAGE
# ============================================================

resized = cv2.resize(image, (800, 600))

cv2.imshow("Resized Image", resized)


# ============================================================
# 5. GRAYSCALE
# ============================================================

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray)


# ============================================================
# 6. BGR → RGB
# ============================================================

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# OpenCV uses BGR by default.
# RGB is commonly used by other Python image libraries.


# ============================================================
# 7. DRAW LINE
# ============================================================

line_image = image.copy()

cv2.line(
    line_image,
    (50, 50),       # starting point
    (400, 50),      # ending point
    (255, 0, 0),    # BGR color
    3               # thickness
)

cv2.imshow("Line", line_image)


# ============================================================
# 8. DRAW RECTANGLE
# ============================================================

rectangle_image = image.copy()

cv2.rectangle(
    rectangle_image,
    (100, 100),
    (400, 300),
    (0, 255, 0),
    3
)

cv2.imshow("Rectangle", rectangle_image)


# ============================================================
# 9. DRAW CIRCLE
# ============================================================

circle_image = image.copy()

cv2.circle(
    circle_image,
    (300, 250),     # center
    100,            # radius
    (0, 0, 255),
    3
)

cv2.imshow("Circle", circle_image)


# ============================================================
# 10. PUT TEXT ON IMAGE
# ============================================================

text_image = image.copy()

cv2.putText(
    text_image,
    "OpenCV",
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (255, 255, 255),
    3
)

cv2.imshow("Text", text_image)


# ============================================================
# 11. CANNY EDGE DETECTION
# ============================================================

edges = cv2.Canny(
    gray,
    100,
    200
)

cv2.imshow("Edges", edges)


# ============================================================
# 12. THRESHOLDING
# ============================================================

_, threshold = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Threshold", threshold)


# ============================================================
# 13. BLUR
# ============================================================

blurred = cv2.GaussianBlur(
    image,
    (5, 5),
    0
)

cv2.imshow("Blurred", blurred)


# ============================================================
# 14. SAVE IMAGE
# ============================================================

cv2.imwrite(
    "output.jpg",
    resized
)

print("\nImage saved as output.jpg")


# ============================================================
# 15. WAIT FOR KEY
# ============================================================

key = cv2.waitKey(0)

print("Key pressed:", key)


# ============================================================
# 16. CLOSE ALL WINDOWS
# ============================================================

cv2.destroyAllWindows()


# ============================================================
# 17. WEBCAM
# ============================================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

print("\nWebcam started")
print("Press Q to quit")


while True:

    # Read one frame
    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    # Show webcam frame
    cv2.imshow("Webcam", frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ============================================================
# 18. RELEASE WEBCAM
# ============================================================

cap.release()

cv2.destroyAllWindows()

print("Webcam stopped")