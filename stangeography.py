import wave

def extract_data(audio_file):

    audio = wave.open(audio_file, mode='rb')
    
    frames = audio.readframes(audio.getnframes())
    
    # Close the audio file
    audio.close()
    
    # Extract LSBs from audio frames
    extracted_bits = []
    for byte in frames:
        extracted_bits.append(byte & 1)  # Get the LSB of each byte
    
    byte_array = []
    for i in range(0, len(extracted_bits), 8):
        byte = 0
        for bit in extracted_bits[i:i+8]:
            byte = (byte << 1) | bit
        byte_array.append(byte)
    
    # Convert byte array to string (assuming ASCII encoding for hidden data)
    hidden_data = bytearray(byte_array).decode('utf-8', errors='ignore')
    
    return hidden_data

# Example usages
audio_file = 'secret_comm.wav'  # Replace with your actual audio file path
hidden_message = extract_data(audio_file)
print("Extracted Hidden Message: ", hidden_message)
