#! /usr/bin/python
import sys
import server

def is_word_less_than_candidate(word, candidate_word):
  return not candidate_word.startswith('"') and candidate_word > word

def get_counts_from_file(file_name, word):
  file = open(server.count_file_path(file_name), 'r')
  count = 0
  for line in file:
    (candidate_word, candidate_count) = line.split()
    if candidate_word == word:
      count += int(candidate_count)
    elif is_word_less_than_candidate(word, candidate_word):
      break
  file.close()
  return count

def main(word):
  count = 0
  for file_name in server.file_names():
    count += get_counts_from_file(file_name, word)
  print count

if __name__ == '__main__':
  main(sys.argv[1])
