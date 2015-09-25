#! /usr/bin/python
import zipfile
import server
import sys
import random
import count_word

def word_from_file(file_name, word, index):
    z = zipfile.ZipFile(server.zip_file_path(file_name), 'r') 
    internal_name = z.namelist()[0]
    f = z.open(internal_name)
    for line in f:
        tokens = line.split()
        if tokens[0] == word:
            times = int(tokens[3])
            if times >= index:
              return tokens[1]
            else:
              index -= times
	elif count_word.is_word_less_than_candidate(word, tokens[0]):
	    break
    f.close()
    z.close()

def word_for_index(word, index):
  for file_name in server.file_names():
    count = count_word.get_counts_from_file(file_name, word)
    if index <= count:
      return word_from_file(file_name, word, index)
    else:
      index -= count

def main(word, index):
  print word_for_index(word, index)

if __name__ == '__main__':
  main(sys.argv[1], int(sys.argv[2]))
