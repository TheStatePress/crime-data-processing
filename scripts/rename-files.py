#!/usr/bin/env python3
import csv
import os

dir = '../0-raw-pdf/'

for fileName in os.listdir(dir):
  nameArray = fileName.split(' ')
  if len(nameArray) == 2: # if there's a space in the name
    newName = nameArray[0] + nameArray[1]
    os.rename(dir + fileName, dir + newName)