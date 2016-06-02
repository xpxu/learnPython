# vim: tabstop=4 shiftwidth=4 softtabstop=4
	
	print 'hello'

tmp_dirs_for_nimbula_api= (
    '/tmp/workdir/.local/share/nimbula', 
    '/tmp/workdir/.config/nimbula', 
    '/tmp/workdir/.cache/nimbula', 
    '/tmp/nimbula', 
)

for dir in tmp_dirs_for_nimbula_api:
	print dir
