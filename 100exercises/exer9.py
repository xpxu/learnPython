lines = []
while True:
    s = raw_input('input >')
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print sentence