'''
Author: Luke Hebert
Date begun: 2019 04 15
Description: takes an input file and compresses its contents to a .gz file
'''

import sys
import gzip

inFile_path = sys.argv[1]
outFile_path = inFile_path + '.gz'

with open(inFile_path, 'r') as in_file:
	for line in in_file:
		with gzip.open(outFile_path, 'a') as out_file:
			out_file.write(line)
