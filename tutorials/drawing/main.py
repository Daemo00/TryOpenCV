import numpy as np
import cv2 as cv


def line(img):
    # Draw a diagonal blue line with thickness of 5 px
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)


def rectangle(img):
    cv.rectangle(img, (100, 0), (510, 128), (0, 255, 0), 3)


def circle(img):
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)


def ellipse(img):
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)


def polyline(img):
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (0, 255, 255))


def text(img):
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)


def wait_user_action(img):
    k = cv.waitKey(0)
    if k == ord('q'):
        raise StopIteration()
    elif k == ord('s'):
        cv.imwrite("drawing.png", img)


def main():
    drawings = [
        line,
        rectangle,
        circle,
        ellipse,
        polyline,
        text,
    ]

    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)
    cv.imshow("Drawing", img)
    for drawing in drawings:
        wait_user_action(img)
        drawing(img)
        cv.imshow("Drawing", img)
    wait_user_action(img)


if __name__ == '__main__':
    main()
