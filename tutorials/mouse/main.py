import numpy as np
import cv2 as cv


def draw_circle(event, x, y, flags, params):
    img = params['img']
    drawing = params['drawing']
    mode = params['mode']
    ix = params['ix']
    iy = params['iy']
    if event == cv.EVENT_LBUTTONDOWN:
        params['drawing'] = True
        params['ix'], params['iy'] = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        params['drawing'] = False
        if mode :
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


def main():
    events = [i for i in dir(cv) if 'EVENT' in i]
    print(events)
    # Create a black image, a window and bind the function to window
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    params = {
        'ix': 0,
        'iy': 0,
        'drawing': False,
        'mode': False,
        'img': img,
    }
    cv.setMouseCallback('image', draw_circle, params)
    while True:
        cv.imshow('image', params['img'])
        k = cv.waitKey(1)
        if k == ord('m'):
            params['mode'] = not params['mode']
        elif k == ord('q'):
            break
        elif k == ord("s"):
            cv.imwrite("mouse.png", img)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
