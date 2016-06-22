# gifsketch

This program does edge detection of every frame of a gif and compiles into a new gif. 

an example of the input and output of this can be found with the files " hawk.gif" and "hawk.gifsketch.gif"

to run the program:

pip install natsort
pip install moviepy

chmod +x sketchgif.py

./sketchgif.py imagename.gif thresholdvalue /path/to/output/folder

#IMPORTANT
you need to create an empty folder in the same directory as sketch.py titled "output" 
the program works primarily in this folder and is necessary for the program to run
without it, the program wont run properly and could:

a) delete images from the folder you may not want deleted  

b) leave you with possibly several hundred images in that folder

Neither of these are fun so please make an empty folder named output in the 
same directory you save sketchgif.py to 

I would also like to thank github user revolunet for the extractGif function they wrote. 
It's super simple and super awesome and does the job perfectly. 


