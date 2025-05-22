import os
import whisper
import json

def transcribe_audio(audio_path, output_dir="output"):
    # Cargar el modelo (usa "base", "small", "medium" o "large" para mejor precisión)
    model = whisper.load_model("base")

    # Transcribir el audio con marcas de tiempo
    result = model.transcribe(audio_path, word_timestamps=False)

    # Extraer segmentos de texto con sus tiempos
    transcription_data = [
        {
            "start": round(segment["start"], 2),
            "end": round(segment["end"], 2),
            "text": segment["text"].strip()
        }
        for segment in result["segments"]
    ]

    # Crear el HTML con la transcripción
    audio_filename = os.path.basename(audio_path)
    html_content = f'''
    <div class="audio-center p-5rem">
        <audio id="audioInfo" class="audio-con-transcripcion" controls
            data-transcripcion='{json.dumps(transcription_data, ensure_ascii=False)}'>
            <source src="../assets/audio/{audio_filename}" type="audio/mp3">
        </audio>
        <i class="transcription-toggle fas fa-closed-captioning audio-estilos"></i>
    </div>
    '''

    # Guardar el HTML en la carpeta de salida
    output_filename = os.path.splitext(audio_filename)[0] + ".html"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Transcripción guardada en: {output_path}")

if __name__ == "__main__":
    # Procesar todos los audios en la carpeta /audios
    audio_files = [f for f in os.listdir("audios") if f.endswith(".mp3")]

    if not audio_files:
        print("⚠️ No hay archivos .mp3 en la carpeta /audios")
    else:
        for audio_file in audio_files:
            audio_path = os.path.join("audios", audio_file)
            transcribe_audio(audio_path)