import numpy as np
from pyzbar import pyzbar
import cv2


def main():
    cap = cv2.VideoCapture(0)

    # change resolution (960x720)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)

    while True:
        # read frame from webcam
        ret, frame = cap.read()

        for barcode in pyzbar.decode(frame):
            rect = barcode.rect

            # draw rectangle
            cv2.rectangle(
                frame,  #
                (rect.left, rect.top),
                (rect.left + rect.width, rect.top + rect.height),
                (0, 255, 0),
                3)

            # transform polygon
            pts = np.array(  #
                [[pt.x, pt.y] for pt in barcode.polygon]  #
            ).reshape(1, -1, 2)

            # draw polygon
            cv2.polylines(frame, pts, True, (0, 0, 255), 3)

            # put data text
            cv2.putText(
                frame,  #
                barcode.data.decode('utf-8'),
                (rect.left, rect.top - 10),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (255, 0, 0),
                2,
                cv2.LINE_AA)

        cv2.imshow('decode', frame)

        k = cv2.waitKey(1)
        if k == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
