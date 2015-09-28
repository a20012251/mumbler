#! /usr/bin/python
import zipfile
import sys
import server
from os import listdir
from os.path import join

def append_word_to_file(output_file, word, count):
  if count > 0:
    output_file.write(word + "\t" + str(count) + "\n")

def append_word_to_short_file(output_file, word1, word2, count):
  if count > 0:
    output_file.write(word1  + ' ' + word2 + ' ' + str(count) + "\n")

def preprocess_file(file_name):
    sf = open(server.short_file_path(file_name), 'w')
    output_file = open(server.count_file_path(file_name), 'w')
    z = zipfile.ZipFile(server.zip_file_path(file_name), 'r')
    internal_name = z.namelist()[0]
    f = z.open(internal_name)

    word = ''
    word2 = ''
    count = 0
    count_pair = 0

    for line in f:
      tokens = line.split()
      if tokens[0] != word:
        append_word_to_file(output_file, word, count)
        append_word_to_short_file(sf, word, word2, count_pair)
        count = 0
        word = tokens[0]
        word2 = tokens[1]
        count_pair = 0
      elif tokens[1] != word2:
        append_word_to_short_file(sf, word, word2, count_pair)
        word2 = tokens[1]
        count_pair = 0
      count += int(tokens[3])
      count_pair += int(tokens[3])

    append_word_to_file(output_file, word, count)
    append_word_to_short_file(sf, word, word2, count_pair)
          
    f.close()
    sf.close()
    z.close()
    output_file.close()

def create_big_map():
  for file_name in server.file_names():
    preprocess_file(file_name)
    
def main():
  create_big_map()

if __name__ == '__main__':
  main()
