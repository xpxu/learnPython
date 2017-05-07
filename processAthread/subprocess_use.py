def run_command(cmd):
    print 'I am in %s' % cmd
    child = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = child.communicate()
    rc = child.returncode
    print 'I am out %s' % cmd
    return cmd, out, err, rc


run_command(['ls -l'])