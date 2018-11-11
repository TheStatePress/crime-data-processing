#!/usr/bin/env python3
import csv
import os

inputDir = '../1-tabula-output/'
outputDir = '../2-separated-output/'
cleanSubDir = 'clean/'
dirtySubDir = 'dirty/'

def isRowClean(row):
  return row

def separateRowsOfFile(fileName):
  return fileName

for i, fileName in enumerate(os.listdir(inputDir)):
  separateRowsOfFile(fileName)
