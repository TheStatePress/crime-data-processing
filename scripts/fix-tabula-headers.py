#!/usr/bin/env python3
import csv
import os

def cleanHeaders(fileName):
  file = open('../0-raw-pdf/' + fileName)
  data = list(csv.reader(file))
  print(data)

for fileName in os.listdir('../0-raw-pdf/'):
  print(fileName)
