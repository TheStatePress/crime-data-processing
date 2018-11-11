#!/usr/bin/env python3
import csv
import os

dir = '../0-raw-pdf/'

def cleanHeaders(fileName):
  file = open(dir + fileName)
  data = list(csv.reader(file))
  print(data)

for i, fileName in enumerate(os.listdir('../0-raw-pdf/')):
  if i == 0:
    cleanHeaders(fileName)
