import librosa
#pitchtrack.py

def track_pitches(stfts, sr, fmin=50.0, fmax=2000.0):
    pitches_list = []
    for S in stfts:
        pitches, magnitudes = librosa.piptrack(S=S, sr=sr, fmin=fmin, fmax=fmax)
        pitches_list.append(pitches)
    return pitches_list

def extract_dominant_pitches(pitches_list, magnitudes_list):
    dominant_pitches_list = []
    for pitches, magnitudes in zip(pitches_list, magnitudes_list):
        dominant_pitches = []
        for t in range(pitches.shape[1]):  # Iterate over time frames
            index = magnitudes[:, t].argmax()  # Find the index of the max magnitude
            dominant_pitch = pitches[index, t]  # Get the corresponding pitch
            if dominant_pitch > 0:  # Filter out frames with no pitch detected
                dominant_pitches.append(dominant_pitch)
        dominant_pitches_list.append(dominant_pitches)
    return dominant_pitches_list


# Assuming `dominant_pitches_list` is a list of lists,
# where each sublist contains the dominant pitches for a segment

# Function to convert frequency to note name
def frequency_to_note_name(frequency):
    A4 = 440
    C0 = A4 * np.power(2, -4.75)
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    h = np.round(12 * np.log2(frequency / C0))
    n = int(h % 12)
    octave = int(h // 12)

    return note_names[n] + str(octave)

# Loop through each segment's dominant pitches
note_names_segments = []  # This will store the note names for each segment
for segment_pitches in dominant_pitches_list:
    segment_note_names = []  # Store note names for the current segment
    for pitch in segment_pitches:
        # Convert each pitch to a note name and add it to the current segment's list
        if pitch > 0:  # Ensure that the pitch value is valid
            note_name = frequency_to_note_name(pitch)
            segment_note_names.append(note_name)
        else:
            segment_note_names.append(None)  # Handle cases where pitch detection returned 0 or invalid pitch
    # Add the current segment's note names to the main list
    note_names_segments.append(segment_note_names)

    print(note_names_segments)

# `note_names_segments` now contains the note names for each pitch in each segment
