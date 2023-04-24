import cv2 as cv
import sys


def main():
    img = cv.imread(cv.samples.findFile("starry_night.jpg"))
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("starry_night.png", img)


if __name__ == '__main__':
    cv.samples.addSamplesDataSearchPath('opencv-python/opencv/samples/data')
    main()

