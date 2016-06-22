#!/usr/bin/env python
from PIL import Image, ImageSequence
from natsort import natsorted
from moviepy.editor import *
import sys,os

def natsort(tobesort):
	return natsorted(tobesort)

def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    os.chdir(pathToOutput)
    while frame:
        #frame.save( '%s/%s-%s.png' % (outFolder, os.path.basename(inGif), nframes ) , 'PNG')
        frame.save( 'image%s.png' % ( nframes ) , 'PNG')
        #os.system("cd ~")
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    os.system("cd ~")
    return True

if len(sys.argv) > 3:
	gif = sys.argv[1]
	threshold = int(sys.argv[2])
	pathToOutput = sys.argv[3]
	
else:
	gif = raw_input("enter the name of the image file you would like to sketch: ")
	threshold = int(input("enter the threshold level: "))
	pathToOutput = raw_input("enter the path to the output folder: ")

gim = Image.open(gif)
duration = []

for frames in ImageSequence.Iterator(gim):
	duration.append(frames.info['duration'])

extractFrames(gif, 'output')


a = os.listdir(os.getcwd())
image_list = natsorted(a)

for z in range(0,len(image_list)):
	print "converting image "  + str(z + 1) +  " out of "  + str(len(image_list))
	im = Image.open(image_list[z])
	imrgb=im.convert("RGB")
	picture = imrgb.load()
	width = im.size[0]
	height = im.size[1]
	for y in range(1,height):
		for x in range(1,width):
			if abs(sum(picture[x,y]) - sum(picture[x-1,y-1])) >= threshold:
				imrgb.putpixel((x-1,y-1), (0,0,0))
			elif abs(sum(picture[x,y]) - sum(picture[x-1,y])) >= threshold:
				imrgb.putpixel((x-1,y-1), (0,0,0))
			elif abs(sum(picture[x,y]) - sum(picture[x,y-1])) >= threshold:
				imrgb.putpixel((x-1,y-1), (0,0,0))
			else:
				imrgb.putpixel((x-1,y-1),(255,255,255))
	imrgb.save(image_list[z])

os.system("cd " + pathToOutput)
os.system("cd ..")
os.system("rm -rf " + gif + "sketch.gif")
os.system("cd " + pathToOutput)
print os.getcwd()
my_clip = ImageSequenceClip(image_list, fps= (len(image_list)/(sum(duration)/1000)) )
my_clip.write_gif( gif + "sketch.gif")
os.system("rm -rf *.png")
os.system("mv " + gif + "sketch.gif " + "../")
