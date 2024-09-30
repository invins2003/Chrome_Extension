import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()

    def recognize_from_microphone(self):
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source)  # Optional: adjusts to ambient noise
            print("Listening for speech...")
            
            # Listen to the audio from the microphone
            audio = self.recognizer.listen(source)
            
            try:
                # Recognize speech using Google's speech recognition API
                print("Recognizing speech...")
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Google Speech Recognition could not understand the audio."
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition; {e}"

    def recognize_from_file(self, audio_file):
        # Recognize speech from an audio file (e.g., .wav)
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)  # Read the entire audio file
            
            try:
                # Recognize speech using Google's speech recognition API
                print("Recognizing speech from file...")
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Google Speech Recognition could not understand the audio."
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition; {e}"

# Example usage of the SpeechToText class
if __name__ == "__main__":
    stt = SpeechToText()

    # Recognize speech from microphone
    print("Say something:")
    text = stt.recognize_from_microphone()
    print("You said:", text)

    # Optionally, recognize speech from an audio file (like a .wav file)
    # audio_file_path = "path_to_audio_file.wav"
    # text_from_file = stt.recognize_from_file(audio_file_path)
    # print("Transcribed text from file:", text_from_file)
