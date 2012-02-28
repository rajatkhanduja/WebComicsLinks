#!/usr/bin/python
# Author : Rajat Khanduja
# Date : 25/12/2011
# This is a script to download images from a website, such as a comic website. The input gives the 'folder' which contains the html files of the entire
# website (that is relevant). Using those files, we can generate a list of image files that need to be downloaded.
#
#
# Usage :-
# download_images_site.py source_folder
#
#
# Exit status :-
# 0 -> successful
# 1 -> Incorrect number of arguments
# 2 -> Source folder does not exist

import sys
import os
from BeautifulSoup import BeautifulSoup
import re

def usage (name) :
  print "Usage :"
  print "\t" + name + "source_folder"
  return

def images_in_file (path):

  fp = open(path,'r')

  soup = BeautifulSoup(fp)
  img_list = soup.findAll('img')

  links = []
  for img in img_list :
    links.append (unicode(img['src']))

  return links

def main (args) :
  
  if len(args) != 2 :
    print "Incorrect usage"
    usage (args[0])
    sys.exit (1)
    
  # Check if the source folder exists
  if not os.path.isdir(args[1]) : 
    print "Folder does not exist"
    sys.exit (2)

  folder = args[1]

  # list all files 
  dir_list = os.listdir(folder)

  images = dict ()

  for file in dir_list :
    path = folder + "/" + file

    if os.path.isdir(file):
      continue
    else :
      images_temp = images_in_file(path)
      
      for image in images_temp:
        images[image] = 1
  
  for image in images :
    print image


if __name__ == "__main__" :
  main(sys.argv)
