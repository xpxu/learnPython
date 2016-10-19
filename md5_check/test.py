import hashlib



def check_md5(filepath, md5_filepath):
    # md5_result = md5_expect = ''
    with open(filepath) as f_to_check:
        data = f_to_check.read()
        md5_result = hashlib.md5(data).hexdigest()
    with open(md5_filepath) as f:
        md5_expect = f.read()
    return True if md5_result == md5_expect else False

    

print check_md5('nimbula-patch-bundle-16.2.6-20160819-001800.tar.gz',
    'nimbula-patch-bundle-16.2.6-20160819-001800.tar.gz.md')
