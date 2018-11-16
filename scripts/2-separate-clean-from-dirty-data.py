#!/usr/bin/env python3
import csv
import os

inputDir = '../1-tabula-output/'
outputDir = '../2-separated-output/'
cleanSubDir = 'clean/'
dirtySubDir = 'dirty/'

dirty = 0
clean = 0
empty = 0

def isRowClean(row):
  for value in row:
    if value == '':
      return False
  return True

def isRowEmpty(row):
  for value in row:
    if value != '':
      return False
  return True

def separateRowsOfFile(fileName):
  global dirty
  global clean
  global empty

  file = open(inputDir + fileName)
  reader = csv.reader(file)
  data = list(reader)
  for i, row in enumerate(data):
    if isRowEmpty(row):
      empty += 1
    elif not isRowClean(row):
      dirty += 1
    else:
      clean += 1


for i, fileName in enumerate(os.listdir(inputDir)):
  separateRowsOfFile(fileName)

print('empty rows: ' + str(empty))
print('dirty rows: ' + str(dirty))
print('clean rows: ' + str(clean))
