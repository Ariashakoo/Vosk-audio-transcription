````markdown
# Audio Transcription with Vosk

A simple Python script to transcribe audio files into text using the Vosk speech recognition toolkit. This repository provides utilities to automatically convert stereo audio to mono, resample audio to your target rate, and save the transcribed text to a file.

## Features

- **Automatic Mono Conversion**: Converts multi-channel audio to mono for compatibility.
- **Resampling**: Resamples audio to a target rate (default 16 kHz) if needed.
- **Streaming Recognition**: Processes audio in chunks to handle large files without excessive memory usage.
- **Portable**: Works on Windows, macOS, and Linux.

## Prerequisites

- Python 3.7 or higher
- [Vosk API](https://github.com/alphacep/vosk-api)
- A Vosk language model (e.g., for English or other supported languages)

## Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/Ariashakoo/Vosk-audio-transcription
   cd vosk-audio-transcriber
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\\Scripts\\activate
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download a Vosk model**

   Visit the [Vosk models page](https://alphacephei.com/vosk/models) and download a model suitable for your language. Unzip it somewhere on your disk.

## Usage

1. **Set the model path and audio file** in the `__main__` section of `transcribe.py`:

   ```python
   if __name__ == "__main__":
       # Update these paths
       model_path = r"path/to/vosk-model"
       audio_file = r"path/to/audio.wav"
       # Transcription
       transcription = transcribe_audio(model_path, audio_file)
       if transcription:
           save_to_file(transcription, "transcription.txt")
       else:
           print("Transcription failed or produced no text.")
   ```

2. **Run the script**

   ```bash
   python transcribe.py
   ```

   The transcribed text will be saved to `transcription.txt` in the current directory.

## Configuration

* **`target_rate`**: Change the default sample rate (16 kHz) by passing a different value to `transcribe_audio(model_path, audio_file, target_rate=8000)`.
* **Chunk size**: Adjust the buffer size by changing the `wf.readframes(4000)` value in the code for larger or smaller frame blocks.

## Troubleshooting

* **Model Not Found**: Ensure the `model_path` points to the directory containing `am` subfolder and `model.conf`.
* **Audio File Error**: Confirm the audio file exists and is a valid WAV file. Use `ffmpeg` or `sox` to convert other formats.
* **Low Accuracy**: Try a different Vosk model or improve audio quality (noise reduction).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for:

* Support for more audio formats
* Enhanced logging and progress indicators
* Integration with JSON or CSV output formats

## License

This project is licensed under the [MIT License](LICENSE).

---

*This README was generated to help you quickly set up and use the Vosk-based audio transcription script.*

```
```
