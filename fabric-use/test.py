#!/usr/bin/env python

from fabric.api import local, cd, run, env
env.password = 'Dzdz1234'
env.hosts=['xpxu@slc09wqi.us.oracle.com']

def update_setting_remote():
    print "remote update"
    with cd('~/tools'):   
        run('ls -l | wc -l')  
