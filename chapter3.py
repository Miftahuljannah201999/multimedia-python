from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Memuat file video
video = VideoFileClip('video.mp4')

# Menyimpan file video
video.write_videofile('result.mp4')

# Mendapatkan 10 detik pertama dari video
short_video = video.subclip(0, 10)
short_video.write_videofile('short_result.mp4')

# Menggabungkan video asli dengan video pendek
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

# Membalikkan video pendek
reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('reversed_result.mp4')

# Mempercepat video pendek 2x
sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('sped_up_result.mp4')

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Multimedia Application")

# Memuat gambar menggunakan Pillow
image = Image.open('kucing1.JPG')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play Music", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()