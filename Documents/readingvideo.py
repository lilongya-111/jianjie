import cv2


def main():
    # 打开相机设备
    cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video',1980,1080)
    cap = cv2.VideoCapture("/home/longyali/Videos/dance.mp4")

    

    # 检查相机是否成功打开
    if not cap.isOpened():
        print("Error: can't open camera through video capture")
        return

    # 循环读取视频帧
    while True:
        ret, frame = cap.read()

        if ret:
            # 在窗口中显示视频帧
            cv2.imshow("Video", frame)

        # 按下 'q' 键退出循环
        if cv2.waitKey(42) == ord('q'):
            break

    # 释放相机设备和关闭窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
