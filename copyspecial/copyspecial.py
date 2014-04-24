#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
def is_special(filename):
    special_variable = re.search(r'__\w+__', filename)
    if special_variable:
        return True
    else:
        return False

# Write functions and modify main() to call them
def get_special_paths(directory):
    """Given a directory, it returns a list with all the files with special
    names in it. Absolute path of each file is given"""

    filenames = os.listdir(directory)
    files_list = []
    for filename in filenames:
        if is_special(filename):
            full_path = os.path.join(directory, filename)
            files_list.append(os.path.abspath(full_path))
    return files_list


def copy_to(paths, directory):
    """Given a list of paths and a destination directory, it copies all
    the files into the given directory"""

    if not os.path.isdir(directory):
        os.mkdir(directory)
    for path in paths:
        print 'copying', path, 'into', directory
        shutil.copy(path, directory)


def main():
    """This basic command line argument parsing code is provided.
    Add code to call your functions below."""

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
        special_paths = get_special_paths(args[0])
        copy_to(special_paths, todir)

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
        special_paths = get_special_paths(args[0])
        cmd = 'zip -j ' + tozip + ' ' + ' '.join(special_paths)
        print 'Command I\'m goint to do:' + cmd
        (status, output) = commands.getstatusoutput(cmd)
        print output

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    if not todir and not tozip:
        files_list = get_special_paths(args[0])
        for special_file in files_list:
            print special_file


if __name__ == "__main__":
    main()
