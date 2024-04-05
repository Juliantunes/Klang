#normalization.py
import librosa
import soundfile as sf

def normalize_audio(file_path):
    y, sr = librosa.load(file_path, sr=None, mono=True)
    y_normalized = librosa.util.normalize(y)
    sf.write(file_path, y_normalized, sr)  # Overwrites the original file with normalized audio

if __name__ == "__main__":
    normalize_audio("recordings/myrecording.wav")
