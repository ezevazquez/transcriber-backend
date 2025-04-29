import whisper
import os

model = whisper.load_model("medium")

def transcribe_audio(wav_path, file_id, tasks):
    try:
        result = model.transcribe(wav_path, word_timestamps=True)
        speakers = simple_speaker_segmentation(result)

        output_txt = f"/tmp/{file_id}.txt"
        with open(output_txt, "w", encoding="utf-8") as f:
            for speaker, text in speakers:
                f.write(f"{speaker}: {text}\n")
        
        tasks[file_id]["status"] = "done"
        tasks[file_id]["txt_file"] = output_txt
    except Exception as e:
        tasks[file_id]["status"] = f"error: {str(e)}"

def simple_speaker_segmentation(transcription):
    segments = []
    current_speaker = 1
    last_end = 0

    for segment in transcription['segments']:
        if segment['start'] - last_end > 5:
            current_speaker += 1
        segments.append((f"Speaker {current_speaker}", segment['text'].strip()))
        last_end = segment['end']

    return segments

def get_status(file_id, tasks):
    return tasks.get(file_id, {"status": "not_found"})
