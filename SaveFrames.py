import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

videopath = input()
cap = cv2.VideoCapture(videopath)

print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

cnt = 1

# 비디오 매 프레임 처리
while True: # 무한 루프
    success, frame = cap.read() # 두 개의 값을 반환하므로 두 변수 지정

    if not success: # 새로운 프레임을 못받아 왔을 때 braek
        break
    
    cv2.imwrite("Frame" + str(cnt) + ".jpg", frame)
    cnt += 1

    cv2.imshow('Frame', frame)

    # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
    if cv2.waitKey(1) == ord("q"):
        break

cap.release() # 사용한 자원 해제
cv2.destroyAllWindows()