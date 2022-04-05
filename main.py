import frames
import os
import numpy as np
from PIL import Image
import time
#from playsound import playsound
from threading import Thread

print("From Jazzy <3... \n give it a sec to start \n the anticipation is worth it")


CLIP_FRAMES = 5300
CLIP_LENGTH = 219.0666
WIDTH = 72 * 2

ASCII_CHARS = [' ', '.',':',';','!','+','*','e','$','8','@']      
ASCII_CHARS.reverse()
ASCII_CHARS = ASCII_CHARS[::-1]

def resize(image, new_width=WIDTH):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width)/2)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=WIDTH):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+int(new_width)] for index in range(0, len_pixels, int(new_width))]

    return '\n'.join(new_image)

def runner(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
        return
    image = do(image)

    return image

frames = []

for i in range(0, int(CLIP_FRAMES/4)+1):
    path = "C:\\Users\\danie\\Desktop\\Coding\\who asked\\cmd\\frames\\frame"+str(i*4)+".jpg" 
    frames.append(runner(path))

def main():
    for i in range(CLIP_FRAMES):
        print(frames[int(i)])
        time.sleep(0.15)

t1 = Thread(target=main)
t1.start()
#t2 = Thread(target=sound) amount of time spent trying to figure out playsound: 7
#t2.start()

os.system("mode con cols=144 lines=39")
input('ENTER to exit')