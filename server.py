#! /user/bin/python
from os import listdir
from os.path import join
from os import listdir

# rename server to the server name
SERVER = 'gpfs1'
PATH = '/gpfs/gpfsfpo/' + SERVER + '/'
COUNT_PATH = '/gpfs/gpfsfpo/' + SERVER + '_counts/'

def file_names():
  return sorted([ f for f in listdir(PATH) ])

def zip_file_path(file_name):
  return join(PATH, file_name)
 
def count_file_path(file_name):
  return join(COUNT_PATH, file_name)
