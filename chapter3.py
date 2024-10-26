from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from pydub import AudioSegment
from pydub.playback import play
import os

# Video processing
video = VideoFileClip('video.mp4')

# Save the full video
video.write_videofile('result.mp4')

# Get the first 10 seconds of the video
short_video = video.subclip(0, 10)
short_video.write_videofile('short_result.mp4')

# Combine the original video with the shortened version
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

# Reverse the shortened video
reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('reversed_result.mp4')

# Speed up the shortened video by 2x
sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('sped_up_result.mp4')

# Check for a display environment
if os.environ.get("DISPLAY"):
    import tkinter as tk
    from PIL import Image, ImageTk
    from tkinter import filedialog

    # Create main Tkinter window
    root = tk.Tk()
    root.title("Multimedia Application")

    # Load image using Pillow
    image = Image.open('kucing1.JPG')
    photo = ImageTk.PhotoImage(image)

    # Label to display image
    label = tk.Label(root, image=photo)
    label.pack()

    # Define function to play music
    def play_music():
        file_path = filedialog.askopenfilename()
        if file_path:
            audio = AudioSegment.from_file(file_path)
            play(audio)

    # Button to play music
    play_button = tk.Button(root, text="Play Music", command=play_music)
    play_button.pack()

    # Run the Tkinter main loop
    root.mainloop()
else:
    print("Tkinter GUI is not supported in this environment.")
