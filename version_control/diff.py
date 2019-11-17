import os
import sys
import time
from datetime import datetime
from difflib import ndiff, unified_diff

def path_time(path):
    time_ch = os.path.getmtime(path)
    time_ch = datetime.fromtimestamp(time_ch).strftime('%Y-%m-%d %H:%M:%S.%f')\
              + time.strftime(' %z', time.localtime(time_ch))
    return time_ch

def udiff(path1, path2):
    with open(path1) as file1, open(path2) as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
    date1, date2 = path_time(path1), path_time(path2) 
    return unified_diff(lines1, lines2, fromfile=path1, tofile=path2,
                       fromfiledate=date1, tofiledate=date2)


if __name__ == '__main__':
	path1 = sys.argv[1]
	path2 = sys.argv[2]
	for line in udiff(path1, path2):
		print(line.strip('\n'))