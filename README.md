# gifsketch

This program does edge detection of every frame of a gif and compiles into a newgif. 

an example of the input and output of this can be found with the files " hawk.gif" and "hawk.gifsketch.gif"

to run the program:

chmod +x sketchgif.py

./sketchgif.py imagename.gif thresholdvalue /path/to/output/folder

#IMPORTANT
you need to create an empty folder in the same directory as sketch.py titled "output" 
the program works primarily in this folder and is necessary for the program to run
without it, the program wont run properly and could either a) delete images from the folder you may not want deleted or b) leave you with
possibly several hundred images in that folder. neither of these are fun so please make an empty folder named output in the 
same directory you save sketchgif.py to 
