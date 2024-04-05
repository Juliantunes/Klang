#segmentation.py


import librosa
import numpy as np

def segment_and_compute_stft(file_path, segment_length=1, n_fft=2048, hop_length=None):
    # Load the audio file
    y, sr = librosa.load(file_path, sr=None, mono=True)

    # Determine the number of samples per segment
    frames_per_segment = int(segment_length * sr)

    # Initialize a list to hold the STFTs of each segment
    stfts = []

    # Loop through the audio in segments
    for start in range(0, len(y), frames_per_segment):
        end = start + frames_per_segment
        segment = y[start:end]

        # Only process segments that are the full segment length
        if len(segment) == frames_per_segment:
            # Compute the STFT for the current segment
            S = np.abs(librosa.stft(segment, n_fft=n_fft, hop_length=hop_length))
            
            # Add the computed STFT to the list
            stfts.append(S)

    # Further processing can be done here with the list of STFTs
    # For example, you could apply pitch tracking to each STFT

    # Print the number of fully-processed segments
    print(f"Total full-length segments processed: {len(stfts)}")

    return stfts

if __name__ == "__main__":
    stfts = segment_and_compute_stft("recordings/myrecording_normalized.wav")
