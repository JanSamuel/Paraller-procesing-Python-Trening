# Paraller-procesing-Python-Trening
Code snipet from traning with task parallering in python

it outputs image in .pgm format can be run just be redirecting output to file and duble cliking on file or by using command py *.py | convert - sixel:-

Benchmarked just with:
time *.py > /dev/null

Reference avg time 0,5506
Multithreded avg time 0,3868s
Multiprocessed avg time 0,1994s

Diffrence between Reference and Multithreaded is independent from number of threads and is result of code optymatyzation
