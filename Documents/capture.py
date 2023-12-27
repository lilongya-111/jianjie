import cv2
import numpy as np
import pandas as pd

def main():
    # 打开相机设备
    cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Camera', 640, 480)
    cap = cv2.VideoCapture(0)

    # 检查相机是否成功打开
    if not cap.isOpened():
        print("Error: can't open camera through video capture")
        return

    # 循环读取视频帧
    while True:
        ret, frame = cap.read()

        if ret:
            # 在窗口中显示视频帧
            cv2.imshow("Camera", frame)

        # 按下 'q' 键退出循环
        if cv2.waitKey(1) == ord('q'):
            break

    # 释放相机设备和关闭窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
