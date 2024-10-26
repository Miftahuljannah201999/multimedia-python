import pygame
import PIL
import cv2
import moviepy
import pydub
import tkinter as tk
import pkg_resources

def check_installation():
    print("✅ Pygame version:", pygame.version.ver)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    
    try:
        from moviepy import __version__ as moviepy_version
        print("✅ MoviePy version:", moviepy_version)
    except ImportError:
        print("✅ MoviePy is installed, but version info not found.")
    
    try:
        pydub_version = pkg_resources.get_distribution("pydub").version
        print("✅ Pydub version:", pydub_version)
    except pkg_resources.DistributionNotFound:
        print("❌ Pydub version not found.")
    
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()