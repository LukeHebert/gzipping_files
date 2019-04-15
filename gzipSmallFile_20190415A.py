'''
Author: Luke Hebert
Date begun: 2019 04 15
Description: takes an input file and compresses its contents to a .gz file
'''

import sys
import gzip

inFile_path = sys.argv[1]
in_list = []

with open(inFile_path, 'r') as in_file:
	for line in in_file:
		in_list.append(line)

outFile_path = inFile_path + '.gz'
with gzip.open(outFile_path, 'w') as out_file:
	for line_str in in_list:
		out_file.write(line_str)
		
