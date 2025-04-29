from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse
from app.utils import convert_to_wav, save_file_temporarily
from app.whisper_transcriber import transcribe_audio, get_status
import uuid
import os

app = FastAPI()

tasks = {}

@app.post("/upload/")
async def upload_audio(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    temp_input_path = save_file_temporarily(file, file_id)
    wav_path = convert_to_wav(temp_input_path)

    tasks[file_id] = {"status": "processing", "txt_file": None}

    background_tasks.add_task(transcribe_audio, wav_path, file_id, tasks)

    return {"file_id": file_id}

@app.get("/status/{file_id}")
async def check_status(file_id: str):
    return tasks.get(file_id, {"status": "not_found"})

@app.get("/download/{file_id}")
async def download_txt(file_id: str):
    task = tasks.get(file_id)
    if task and task["status"] == "done":
        return FileResponse(task["txt_file"], media_type="text/plain", filename=f"{file_id}.txt")
    else:
        return {"error": "File not ready or not found"}
