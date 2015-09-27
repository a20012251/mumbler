#! /user/bin/python
from os import listdir
from os.path import join
from os import listdir

# rename server to the server name
SERVER = 'gpfs1'
BASE_PATH = '/gpfs/gpfsfpo/' 
PATH = BASE_PATH + SERVER + '/'
COUNT_PATH = BASE_PATH + SERVER + '_counts/'
SHORT_PATH = BASE_PATH + SERVER + '_short/'

def file_names():
  return sorted([ f for f in listdir(PATH) ])

def zip_file_path(file_name):
  return join(PATH, file_name)
 
def count_file_path(file_name):
  return join(COUNT_PATH, file_name)

def short_file_path(file_name):
  return join(SHORT_PATH, file_name)
