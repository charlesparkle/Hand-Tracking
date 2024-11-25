import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
double_click_threshold = 0.4
last_click_time = 0
gesture_delay = 0.5
last_gesture_time = 0

def perform_gesture(action):
    global last_gesture_time
    current_time = time.time()
    if current_time - last_gesture_time >= gesture_delay:
        pyautogui.press(action)
        last_gesture_time = current_time

def perform_double_click():
    global last_gesture_time
    current_time = time.time()
    if current_time - last_gesture_time >= gesture_delay:
        pyautogui.click(clicks=2)
        last_gesture_time = current_time

def detect_two_fingers(hand_landmarks, width, height):
    index_finger_tip = hand_landmarks.landmark[8]
    middle_finger_tip = hand_landmarks.landmark[12]
    index_finger_dip = hand_landmarks.landmark[7]
    middle_finger_dip = hand_landmarks.landmark[11]
    index_tip_y = index_finger_tip.y * height
    middle_tip_y = middle_finger_tip.y * height
    index_dip_y = index_finger_dip.y * height
    middle_dip_y = middle_finger_dip.y * height
    return index_tip_y < index_dip_y and middle_tip_y < middle_dip_y

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

            h, w, c = frame.shape

            index_finger = hand_landmark.landmark[8]
            cx, cy = int(index_finger.x * w), int(index_finger.y * h)

            if detect_two_fingers(hand_landmark, w, h):
                perform_double_click()

            if prev_x != 0 and prev_y != 0:
                diff_x = cx - prev_x
                diff_y = cy - prev_y

                if diff_y < -50:
                    perform_gesture('up')
                elif diff_y > 50:
                    perform_gesture('down')

                if diff_x > 50:
                    perform_gesture('right')
                elif diff_x < -50:
                    perform_gesture('left')

            prev_x, prev_y = cx, cy
            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Hand Tracking Control: Lompat, Bergulir, Kiri, Kanan, Double Click", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
