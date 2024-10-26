from PIL import Image
from PIL import ImageFilter
from pydub import AudioSegment

# Memuat gambar
image = Image.open('kucing.jpeg')

# Menyimpan gambar
image.save('kucing.jpeg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('kucing.jpeg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('kucing.jpeg')

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('kucing.jpeg')

# Memuat file audio
audio = AudioSegment.from_file('audio1.mp4')

# Menyimpan file audio
audio.export('audio1.mp4', format='mp4')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp4', format='mp4')

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp4', format='mp4')

audio.export('result.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp4', format='mp4')