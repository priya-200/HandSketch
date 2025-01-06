import cv2
import mediapipe as mp
import  numpy as np

mpHand = mp.solutions.hands
hands = mpHand.Hands(
    min_detection_confidence = 0.7,
    min_tracking_confidence=0.7
)
mpDraw = mp.solutions.drawing_utils

canvas_height,canvas_width = 480, 640
drawing_canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8)

drawing_color = (255, 255, 255)
line_thickness = 5

is_drawing = False
last_index_position = None

def detect_fist(hand_landmarks, frame_dims):
    """
    Detects the fist gesture with the help of distance between the thumb and the index
    :param hand_landmarks: The landmarks of the 21 points in our hand through mediapipe
    :param frame_dims: The dimensions of our camera screen for calculating the distance between the tips of the fingers
    :return: Boolean values if the fist is detected or not
    """

    height,width = frame_dims
    index_tip = hand_landmarks.landmark[8]
    thumb_tip = hand_landmarks.landmark[4]

    index_x, index_y = int(index_tip.x * width),int(index_tip.y * height)
    thumb_x, thumb_y = int(thumb_tip.x * width),int(thumb_tip.y * height)

    distance = np.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)

    return distance < 30

def detect_open_hand(hand_landmarks):
    """
    This function is used for detecting if the hands are open or not by checking if the tips of the hands are above the
    metacarpophalangeal (MCP) points
    :param hand_landmarks: The landmarks of the hands which is generated by the mediapipe library
    :return: Boolean value if the hands is open or not.
    """

    tips = [
        hand_landmarks.landmark[4],
        hand_landmarks.landmark[8],
        hand_landmarks.landmark[12],
        hand_landmarks.landmark[16],
        hand_landmarks.landmark[20]
    ]

    mcps = [
        hand_landmarks.landmark[1],
        hand_landmarks.landmark[5],
        hand_landmarks.landmark[9],
        hand_landmarks.landmark[13],
        hand_landmarks.landmark[17]
    ]

    return all(tip.y < mcp.y for tip, mcp in zip(tips, mcps))

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    frame = cv2.flip(img , 1)
    frame_height,frame_width,_ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand_landmarks,mpHand.HAND_CONNECTIONS)

            # Detecting the gestures

            if detect_open_hand(hand_landmarks):
                # Clear the canvas.
                drawing_canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8)
                is_drawing = False

            elif detect_fist(hand_landmarks,(frame_height, frame_width)):
                # Stop drawing
                is_drawing = False
            else:
                index_tip = hand_landmarks.landmark[8]
                index_x ,index_y = int(index_tip.x * frame_width), int(index_tip.y * frame_height)

                cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)

                if is_drawing and last_index_position:
                    cv2.line(drawing_canvas,last_index_position, (index_x,index_y), drawing_color,line_thickness)

                last_index_position = (index_x,index_y)
                is_drawing = True
    cv2.imshow("Drawing Canvas",drawing_canvas)
    cv2.imshow("Hand Tracking",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        # Release resources
cap.release()
cv2.destroyAllWindows()
