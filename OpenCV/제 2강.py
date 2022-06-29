import cv2

capture = cv2.VideoCapture(0)   # 0번 카메라 출력
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 640X480
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:  # 33밀리초 동안 키 입력 없을경우 반복 
    ret, frame = capture.read() # ret = 카메라 상태, frame = 현재 시점의 프레임
    cv2.imshow("VideoFrame", frame) # 특정 윈도우 창에 이미지 띄우기

capture.release() # 카메라 장치에서 받아온 메모리 해제
cv2.destroyAllWindows # 모든 윈도우 창 제거