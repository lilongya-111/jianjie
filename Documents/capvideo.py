import cv2  
  
def main():  
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
      
    VW = cv2.VideoWriter('./out.mp4',fourcc, 25, (640,480))  
    # 打开相机设备  
    cv2.namedWindow('Video',cv2.WINDOW_NORMAL)  
    cv2.resizeWindow('Video',640,480)  
    cap = cv2.VideoCapture(0,cv2.CAP_V4L2)  
  
    # 检查相机是否成功打开  
    if not cap.isOpened():  
        print("Error: can't open camera through video capture")  
        return  
  
    # 循环读取视频帧  
    while True:  
        ret, frame = cap.read()  
  
        if not ret:  
            break  
  
        # 在窗口中显示视频帧  
        cv2.imshow("Video", frame)  
        VW.write(frame)  
  
        # 按下 'q' 键退出循环  
        if cv2.waitKey(1) == ord('q'):  
            break  
    

    # 释放相机设备和关闭窗口  
    cap.release()  
    VW.release()  
    cv2.destroyAllWindows()  
  
if __name__ == "__main__":  
    main()

