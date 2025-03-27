import whisper
import os

# Initialize the Whisper model
model = whisper.load_model("base")

def convert_m4a_to_txt(m4a_file):
    # Check if the file exists
    if not os.path.exists(m4a_file):
        print(f"File {m4a_file} does not exist.")
        return

    # Transcribe audio to text
    result = model.transcribe(m4a_file)
    transcribed_text = result["text"]

    # Save the transcription to a .txt file with the same name as the .m4a file
    txt_filename = os.path.splitext(m4a_file)[0] + ".txt"
    
    with open(txt_filename, "w") as f:
        f.write(transcribed_text)
    
    print(f"Transcription saved to {txt_filename}")

# Provide the .m4a file path
m4a_file = "KCLEE.m4a"
convert_m4a_to_txt(m4a_file)