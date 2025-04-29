import os
from pydub import AudioSegment

def save_file_temporarily(upload_file, file_id):
    temp_path = f"/tmp/{file_id}_{upload_file.filename}"
    with open(temp_path, "wb") as buffer:
        buffer.write(upload_file.file.read())
    return temp_path

def convert_to_wav(input_path):
    output_path = input_path.rsplit(".", 1)[0] + ".wav"
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path
