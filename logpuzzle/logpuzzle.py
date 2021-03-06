#!/usr/bin/python

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

def sort_urls(url_list):
    """Returns a list sorted by the second word if there is a second word,
    otherwise simply sorted"""

    url_dict = {}
    for url in url_list:
        match_word = re.search(r'-(\w+)-(\w+).jpg', url)
        if match_word:
            dict_key = match_word.group(2)
            url_dict[dict_key] = url
        else:
            pass

    if url_dict:
        sorted_urls = []
        url_keys = sorted(url_dict.keys())
        print url_keys
        for key in url_keys:
            sorted_urls.append(url_dict[key])

        print sorted_urls
        return sorted_urls

    else:
        return sorted(url_list)


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    log_file = open(filename, 'rU')
    text = log_file.read()
    tmp_url_list = re.findall(r'GET\s/edu/\S+\.jpg\s', text)
    url_list = []
    for tmp_url in tmp_url_list:
        url = tmp_url.replace('GET ', 'http://code.google.com')
        if url not in url_list:
            url_list.append(url)

    return sort_urls(url_list)


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.isdir(dest_dir):
        print "Directory", dest_dir, 'does not exist'
        print "Creating", dest_dir, '...'
        os.mkdir(dest_dir)

    os.chdir(dest_dir)
    print "Working directory", os.path.abspath(os.curdir)

    index_file = open('index.html', 'w')
    index_file.write('<verbatim>\n')
    index_file.write('<html>\n')
    index_file.write('<body>\n')

    for i in range(len(img_urls)):
        print 'Retrieving img%s' %i
        urllib.urlretrieve(img_urls[i], 'img'+str(i))
        index_file.write('<img src=\"img%s\">' %i)

    index_file.write('\n')
    index_file.write('</body>\n')
    index_file.write('</html>')
    index_file.close()

    os.chdir('../')


def main():
    """This is the main function"""

    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)

if __name__ == '__main__':
    main()
