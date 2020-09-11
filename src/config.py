import os
VIP_WEIGHT = 100
if os.path.basename(os.getcwd()) == 'src':
	DATA_DIR = '../data'
	OUT_DIR = '../data/output'
else:
	DATA_DIR = 'data'
	OUT_DIR = 'data/output'