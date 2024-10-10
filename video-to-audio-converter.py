import os
from moviepy.editor import VideoFileClip

def check_mp4_format(file_path):
    return file_path.lower().endswith('.mp4')

def check_audio_track(video_clip):
    return video_clip.audio is not None

def convert_video_to_audio(input_path, output_path=None):
    try:
        # Read video file
        print(f"Reading video file: {input_path}")
        video_clip = VideoFileClip(input_path)
        
        # Check if file is MP4
        if not check_mp4_format(input_path):
            print("Error: File is not in MP4 format")
            video_clip.close()
            return False
        
        # Check for audio track
        if not check_audio_track(video_clip):
            print("Error: No audio track found in the video")
            video_clip.close()
            return False
        
        # Extract audio and write to MP3 file
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.mp3'
        
        print(f"Extracting audio to: {output_path}")
        video_clip.audio.write_audiofile(output_path)
        
        # Close the video clip to free up resources
        video_clip.close()
        
        print("Conversion completed successfully!")
        return True
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    print("Video to Audio Converter")
    print("------------------------")
    
    while True:
        # Get input file path
        input_path = input("\nEnter the path to the video file (or 'q' to quit): ")
        
        if input_path.lower() == 'q':
            break
        
        # Check if file exists
        if not os.path.exists(input_path):
            print("Error: File does not exist")
            continue
        
        # Optional output path
        output_path = input("Enter the output path (press Enter for default): ").strip()
        output_path = output_path if output_path else None
        
        # Perform conversion
        convert_video_to_audio(input_path, output_path)

if __name__ == "__main__":
    main()
