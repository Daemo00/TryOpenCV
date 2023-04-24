import numpy as np
import cv2 as cv


def draw_circle(event, x, y, flags, img):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


def main():
    events = [i for i in dir(cv) if 'EVENT' in i]
    print(events)
    # Create a black image, a window and bind the function to window
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle, img)
    while True:
        cv.imshow('image', img)
        if ord('q') == cv.waitKey(20):
            break
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
