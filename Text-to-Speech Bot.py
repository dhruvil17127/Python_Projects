from gtts import gTTS
import pygame
import os
import tempfile

def speak(text, language='en'):
    """Convert text to speech and play it immediately"""
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio:
        temp_filename = temp_audio.name
    
    try:
        # Convert text to speech
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(temp_filename)
        
        # Initialize pygame mixer and play the audio
        pygame.mixer.init()
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    finally:
        # Clean up the temporary file
        pygame.mixer.quit()
        try:
            os.remove(temp_filename)
        except:
            pass

def main():
    print("Shepich Text-to-Speech Bot (Press Ctrl+C to exit)")
    print("Enter the text you want me to speak:")
    
    while True:
        try:
            text = input("> ")
            if text.lower() in ['exit', 'quit']:
                break
            if text.strip():
                speak(text)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Initialize pygame (needed for audio)
    pygame.init()
    main()
    pygame.quit()
