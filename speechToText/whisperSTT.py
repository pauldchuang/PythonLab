import whisper
import os
from datetime import datetime

# Initialize the Whisper model
model = whisper.load_model("base")

def convert_m4a_to_txt(input_folder, output_folder):
    # Create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of all .m4a files in the input folder
    m4a_files = [f for f in os.listdir(input_folder) if f.endswith(".m4a")]

    for m4a_file in m4a_files:
        # Print conversion start message
        print(f"Converting {m4a_file} to text...")

        # Check if the file exists
        m4a_file_path = os.path.join(input_folder, m4a_file)
        if not os.path.exists(m4a_file_path):
            print(f"File {m4a_file} does not exist.")
            continue

        # Transcribe audio to text
        result = model.transcribe(m4a_file_path)
        transcribed_text = result["text"]

        # Get current timestamp
        timestamp = datetime.now().strftime("%b_%d_%H_%M_%S")

        # Save the transcription to a .txt file with the same name as the .m4a file and timestamp
        txt_filename = f"{os.path.splitext(m4a_file)[0]}_{timestamp}.txt"
        txt_file_path = os.path.join(output_folder, txt_filename)
        
        with open(txt_file_path, "w") as f:
            f.write(transcribed_text)
        
        # Print conversion done message
        print(f"Conversion of {m4a_file} to text is done. Saved to {txt_file_path}")

# Provide the input and output folder paths
input_folder = "input"
output_folder = "output"

convert_m4a_to_txt(input_folder, output_folder)