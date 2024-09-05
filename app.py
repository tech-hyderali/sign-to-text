import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Define gestures
gestures = {
    'open_palm': 'Hello',
    'closed_fist': 'Goodbye',
    'thumbs_up': 'Yes',
    'thumbs_down': 'No'
}

def detect_gesture(landmarks):
    # Improved gesture detection
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]

    # Check if all fingertips are extended (open palm / hello)
    if all(tip.y < wrist.y for tip in [index_tip, middle_tip, ring_tip, pinky_tip]) and thumb_tip.x > landmarks[3].x:
        return 'open_palm'
    
    # Check for thumbs up
    elif thumb_tip.y < index_tip.y and all(landmarks[i].y > landmarks[i-3].y for i in [8, 12, 16, 20]):
        return 'thumbs_up'
    
    # Check for thumbs down
    elif thumb_tip.y > index_tip.y and all(landmarks[i].y > landmarks[i-3].y for i in [8, 12, 16, 20]):
        return 'thumbs_down'
    
    # If fingers are curled in, it's a closed fist
    elif all(landmarks[i].y > landmarks[i-3].y for i in [8, 12, 16, 20]):
        return 'closed_fist'
    
    else:
        return 'unknown'

# Initialize the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and find hands
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get hand gesture
            landmarks = hand_landmarks.landmark
            gesture = detect_gesture(landmarks)
            
            # Convert gesture to text
            text = gestures.get(gesture, "Unknown")
            
            # Display the text
            cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Sign Language to Text', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()