import os
import wave
import json
import audioop
from vosk import Model, KaldiRecognizer

def transcribe_audio(model_path, audio_file, target_rate=16000):
    """
    Transcribe an audio file to text using Vosk.
    Automatically converts stereo to mono and resamples to target_rate if needed.
    """
    print("--- Debug Info ---")
    print("CWD:", os.getcwd())
    print(f"Model path exists? {os.path.exists(model_path)} -> {model_path}")
    print(f"Audio file exists? {os.path.exists(audio_file)} -> {audio_file}")
    print("Absolute audio path:", os.path.abspath(audio_file))
    print("------------------")

    if not os.path.exists(model_path):
        print(f"Model not found at: {model_path}")
        return None
    if not os.path.exists(audio_file):
        print(f"Audio file not found at: {audio_file}")
        return None

    model = Model(model_path)
    rec = KaldiRecognizer(model, target_rate)

    full_text = []
    with wave.open(audio_file, 'rb') as wf:
        orig_rate = wf.getframerate()
        channels = wf.getnchannels()
        width = wf.getsampwidth()
        print(f"Input audio: {orig_rate} Hz, {channels} channel(s), sample width {width}")

        while True:
            data = wf.readframes(4000)
            if not data:
                break

            if channels > 1:
                data = audioop.tomono(data, width, 1, 1)

            if orig_rate != target_rate:
                data, _ = audioop.ratecv(data, width, 1, orig_rate, target_rate, None)

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if text:
                    full_text.append(text)

    final_result = json.loads(rec.FinalResult())
    final_text = final_result.get("text", "").strip()
    if final_text:
        full_text.append(final_text)

    return " ".join(full_text)


def save_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Transcribed text has been saved to {filename}")


if __name__ == "__main__":
    model_path = r"your model path"
    audio_file = r"your voice path"

    transcription = transcribe_audio(model_path, audio_file)
    if transcription:
        save_to_file(transcription, "transcription.txt")
    else:
        print("Transcription failed or produced no text.")
