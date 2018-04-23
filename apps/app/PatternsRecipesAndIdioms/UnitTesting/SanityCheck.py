import glob
import os

# Do not include the following in the automatic tests:
exclude = ("SanityCheck.py", "BoxObserver.py")


def visitor(arg, dirname, names):
    # Return a string representing the current working directory.
    dir = os.getcwd()
    print("dir:", dir)
    # Change the current working directory to path.
    # This function can support specifying a file descriptor.
    # The descriptor must refer to an opened directory, not an open file.
    os.chdir(dirname)
    try:
        # glob.glob Return a possibly-empty list of path names that match pathname,
        # which must be a string containing a path specification.
        pyprgos = [p for p in glob.glob('*.py') if p not in exclude]
        if not pyprgos:
            return
        print('[' + os.getcwd() + ']')
        for program in pyprgos:
            print('\t', program)
            # os: OS routines for NT or Posix depending on
            # what system we're on.
            os.system('python %s > tmp' % program)
            file = open('tmp').read()
            output = open('tmp').read()
            # Append program output if it's not already there:
            if file.find("output = '''") == -1 and len(output) > 0:
                divider = '#' * 50 + '\n'
                file = file.replace('#' + ':~', '#<hr>\n')
                file += "output = '''\n" + open('tmp').read() + "'''\n"
                open(program, 'w').write(file)
    finally:
        os.chdir(dir)


if __name__ == "__main__":
    # Calls the function visit with arguments (arg, dirname, names)
    # for each directory in the directory tree rooted at path.
    os.walk('.', visitor, None)
