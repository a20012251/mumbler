#! /usr/bin/python
import zipfile
import sys
import server
from collections import defaultdict
from os import listdir
from os.path import join

def append_word_to_file(output_file, word, count):
    if count > 0:
        output_file.write(word + "\t" + str(count) + "\n")

def get_counts_form_file(file_name, output_file):
    z = zipfile.ZipFile(server.zip_file_path(file_name), 'r')
    internal_name = z.namelist()[0]
    f = z.open(internal_name)

    word = ''
    count = 0
    for line in f:
        tokens = line.split()
        if tokens[0] != word:
	    append_word_to_file(output_file, word, count)
            count = 0
            word = tokens[0]
        count += int(tokens[3])
    append_word_to_file(output_file, word, count)
          
    f.close()
    z.close()

def create_big_map():
  for file_name in server.file_names():
    f = open(server.count_file_path(file_name), 'w')
    get_counts_form_file(file_name, f)
    f.close()
    
def main():
  create_big_map()

if __name__ == '__main__':
  main()
