'''
Python to process a big file, like 10G
'''


BUFSIZE = 1024  # 4
lines = f.readlines(BUFSIZE)
while lines:
    for line in lines:
        process(line)
    lines = readlines(BUFSIZE)