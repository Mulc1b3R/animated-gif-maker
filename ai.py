from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageClip, AudioFileClip

def create_video_from_gif_and_audio(gif_file, audio_file, output_file):
    # Load the GIF and MP3 files
    clip_gif = VideoFileClip(gif_file, audio=False)  # Load GIF as a video without audio
    clip_audio = AudioFileClip(audio_file)

    # Set the audio for the GIF clip
    clip_gif = clip_gif.set_audio(clip_audio)

    # Write the final clip as an MP4 video file
    clip_gif.write_videofile(output_file, codec='libx264', fps=24)

    print(f"Video created and saved as '{output_file}'")

# Path to the input GIF file
input_gif = "input.gif"

# Path to the input MP3 file
input_mp3 = "input.mp3"

# Path to the output MP4 video file
output_video = "output.mp4"

create_video_from_gif_and_audio(input_gif, input_mp3, output_video)