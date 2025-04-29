# Audio Transcriber Backend

Backend para transcripción de audios (.mp3, .m4a, .wav) usando Whisper y FastAPI.

## Endpoints

- `POST /upload/`: Subir un audio.
- `GET /status/{file_id}`: Consultar el estado de la transcripción.
- `GET /download/{file_id}`: Descargar el .txt final.

## Cómo levantarlo

```bash
docker build -t audio-transcriber-backend .
docker run -p 8000:8000 audio-transcriber-backend
