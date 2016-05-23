from io import BytesIO

memory = BytesIO()
a = 'hello, world'
memory.write(a.encode('utf8'))
print (memory.getvalue())
memory.seek(0)
memory.read()
