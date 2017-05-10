# automated-runner-files
to run a bunch of stuff for project 2. here is what each one does, in alphabetical order:

## averager.py
averager.py is a file designed to take a bunch of numbers from various text files and average them out. it then outputs the averages, unformatted, to another text file. note: all result files must be named "results[number].txt" (with number going from 1 to 3) in order for the script to read them. or i guess you could just change the names in the file.

ultimately went unused, as we didn't average anything. was still fun to make though.

to run it: (no arguments required)
> python3 averager.py

## randgen-ulti.py
imagine randgen.py, but stronger. it generates files of lengths from 1000 to 10000 in increments of 100s automatically, and also automatically names them according to the naming scheme: [number]songs.txt

to run it: (no arguments required)
> python3 randgen-ulti.py

## randgen.py
[you've seen this before.](https://github.com/whirlygig/randgen)

## runner.py
automatically runs the music_catalog.py file 100 times with the 100 different files created with randgen-ulti.py. runs on python 3.6 because that's the version that the computer running the tests had installed.

to run it: (no arguments required)
> python3 runner.py
