def suppress_keys(d, hidden):
    output = {}
    for key, value in d.items():
        if key in hidden:
            output[key] = '***'
        elif isinstance(value, dict):
            output[key] = suppress_keys(value, hidden)
        else:
            output[key] = value
    return output


infile = open('config')
my_d = dict(infile.read())
print my_d
infile.close()
result = suppress_keys(my_d,['zfs_password'])
outfile = open('result')
outfile.write(result)
outfile.close()
