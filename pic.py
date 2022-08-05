import cv2
import os

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    # base_path = os.path.join(dir_path)
    paths = ["", "", "", "", ""]
    for num in range(5):
        paths[num] = os.path.join(dir_path, "pose"+str(num+1))
        os.makedirs(paths[num], exist_ok=True)

    n = 0
    count = [0, 0, 0, 0, 0]
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('1'):
            cv2.imwrite('{}_{}.{}'.format(paths[0], count[0], ext), frame)
            count[0] += 1
        if key == ord('2'):
            cv2.imwrite('{}_{}.{}'.format(paths[1], count[1], ext), frame)
            count[1] += 1
        if key == ord('3'):
            cv2.imwrite('{}_{}.{}'.format(paths[2], count[2], ext), frame)
            count[2] += 1
        if key == ord('4'):
            cv2.imwrite('{}_{}.{}'.format(paths[3], count[3], ext), frame)
            count[3] += 1
        if key == ord('5'):
            cv2.imwrite('{}_{}.{}'.format(paths[4], count[4], ext), frame)
            count[4] += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'picture', 'pose')