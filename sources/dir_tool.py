import os
import datetime
from datetime import datetime
from file_manager import FileManager

def fileHandler(promt,parameter): 
    if (promt == 'date' ): 
        date_str = ' '
        date_str = date_str.join(parameter)
        print(date_str)
        try:
            new_date = datetime.strptime(date_str,'%Y %m %d')
            manager = FileManager(new_date)
            manager.run()
        except ValueError as e:
            print(e)
    pass

def help(): 
    print('Usage:')
    print('ls \t-To print directories')
    print('file \t-To edit info files and directories')
    pass

while (True): 
    listenner = input('$').split()
    if listenner[0] != None or listenner[0] != '':
        if listenner[0] == 'ls':
            directory = '.'
            if len(listenner) > 1: 
                directory = listenner[1]
            print('\n'.join(os.listdir(directory)))
        elif listenner[0] == 'file': 
            if len(listenner) > 2: 
                fileHandler(listenner[1],listenner[2:])
            else: 
                print('usage -> file [command] [parameter]')
                print('file date [YYYY MM DD] -To change directories and files info')
        elif listenner[0] == 'help':
            help()
        elif listenner[0] ==  'quit':
            break
        else: 
            help()
    else:
        help()
    pass