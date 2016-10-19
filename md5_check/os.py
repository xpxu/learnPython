import os


def test(items_mounted_dir):
    items_mounted_dir = items_mounted_dir \
        if isinstance(items_mounted_dir, str) and \
           os.path.isdir(items_mounted_dir) else None
    print items_mounted_dir


test(None)
test('test')
test('')
test('/scratch/nimbula-work/study-use/learnPython/md5_check')
