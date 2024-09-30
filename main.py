# main.py
import cv2
from hand_detector import HandDetector

def main():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    # Create an instance of the HandDetector class
    hand_detector = HandDetector(detection_confidence=0.7, tracking_confidence=0.7)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Detect hands in the frame
        result = hand_detector.detect_hands(frame)

        # If hands are detected, draw landmarks
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                hand_detector.draw_landmarks(frame, hand_landmarks)

        # Display the resulting frame
        cv2.imshow("Hand Detection", frame)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    hand_detector.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
