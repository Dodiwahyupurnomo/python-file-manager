import os.path
import os
import datetime
import sys


def change( filename ):
    # extract old date:
    date = datetime.datetime.fromtimestamp(os.path.getctime(filename))
    # create a new date with the same time
    new_date = datetime.datetime('2019',  '4', '06', date.hour, date.minute, date.second)
    # set the file creation date with the "-d" switch
    #os.system('SetFile -d "{}" {}'.format(new_date.strftime('%m/%d/%Y %H:%M'), filename))
    os.system('touch -t "{}" {}'.format(new_date.strftime('%Y%m%d%H%M.%S'), filename))
    # set the file modification date with the "-m" switch
    os.system('SetFile -m "{}" {}'.format(new_date.strftime('%m/%d/%Y %H:%M'), filename))
    return

def changeDir(path):
	# check is a directory
	if os.path.isdir(path): 
		# extract old date:
	    date = datetime.datetime.fromtimestamp(os.path.getctime(path))
	    # create a new date with the same time
	    new_date = datetime.datetime('2019',  '4', '06', date.hour, date.minute, date.second)
	    # set the directory creation date with the "-t" switch
	    os.system('touch -t "{}" {}'.format(new_date.strftime('%Y%m%d%H%M.%S'), path))
	    # set the directory modification date with the "-mt" switch
	    os.system('touch -mt "{}" {}'.format(new_date.strftime('%Y%m%d%H%M.%S'), path))

#current working directory
walk_dir = os.getcwd()

print('walk_dir = ' + walk_dir)

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    changeDir(root)
   
    for subdir in subdirs:
        print('\t- subdirectory ' + subdir)
        changeDir(subdir)

    for filename in files:
        file_path = os.path.join(root, filename)

        print('\t- file %s (full path: %s)' % (filename, file_path))
        change(file_path)