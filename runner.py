import os
import sys

for j in range(1, 100):  
    filename = str(j * 100) + 'songs.txt'
    filename.strip('\'')
    to_run = "python3.6 music_catalog.py " + filename
    os.system(to_run)
