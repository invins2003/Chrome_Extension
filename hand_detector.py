# hand_detector.py
import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, detection_confidence=0.7, tracking_confidence=0.7):
        # Initialize Mediapipe hands and drawing utils
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(min_detection_confidence=detection_confidence,
                                         min_tracking_confidence=tracking_confidence)
    
    def detect_hands(self, frame):
        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Process the frame and detect hands
        result = self.hands.process(rgb_frame)
        return result
    
    def draw_landmarks(self, frame, hand_landmarks):
        # Draw landmarks on the frame
        self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

    def release(self):
        # Close the hands model
        self.hands.close()
