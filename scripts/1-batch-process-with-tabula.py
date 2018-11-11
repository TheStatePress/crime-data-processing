#!/usr/bin/env python3
import tabula
import os

inputDir = '../0-raw-pdf/'
outputDir = '../1-tabula-output/'

def convert():
  print('Batching with tabula. This takes literally like half an hour on my laptop')
  tabula.convert_into_by_batch(inputDir, output_format='csv', pages='all')

def move():
  print('Batching done, moving files to correct location')
  for fileName in os.listdir(inputDir):
    if(fileName.endswith('.csv')):
      os.rename(inputDir + fileName, outputDir + fileName)

convert()
move()
print('done!')