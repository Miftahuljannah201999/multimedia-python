import pygame
import sys
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os



# Inisialisasi Pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("miftah")

# Memuat gambar
try:
    image = pygame.image.load('kucing2.jpeg')
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# Memuat dan memutar suara
try:
    pygame.mixer.music.load('result.wav')
    pygame.mixer.music.play(-1)  # Memutar suara berulang kali
except pygame.error as e:
    print(f"Error loading or playing sound: {e}")

# Variabel posisi untuk animasi
x = 0

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi untuk animasi
    x += 5
    if x > 800:
        x = 0

    # Menghapus layar dan menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()
    pygame.time.delay(30)

# Menghentikan musik dan keluar dari Pygame
pygame.mixer.music.stop()
pygame.quit()


# Mengatur direktori sementara untuk Pydub agar tidak terjadi kesalahan izin
temp_dir = tempfile.mkdtemp()
os.environ['TEMP'] = temp_dir
os.environ['TMP'] = temp_dir

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Music Player")

# Mendefinisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        audio = AudioSegment.from_file(file_path)
        try:
            play(audio)
        except PermissionError as e:
            print(f"Permission error: {e}")

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()

# Membersihkan direktori sementara setelah penggunaan
import shutil
shutil.rmtree(temp_dir)