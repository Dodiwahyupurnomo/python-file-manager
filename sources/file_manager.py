import os
import os.path
import datetime
import sys

class FileManager: 
    _date = datetime.date
    def __init__(self,date):
        self.date = date
        pass

    @property 
    def __date__(self): 
        return self._date

    @__date__.setter
    def __date__(self, value): 
        self._date = value
        pass
    
    def run(self): 
        print('Change files and directories info for date')
        walk_dir = os.getcwd()

        for root, subdirs, files in os.walk(walk_dir): 
            self.changeDir(root)

            for subdir in subdirs: 
                self.changeDir(subdir)
            
            for filename in files: 
                self.change(filename)
        pass
    
    def change(self, filename ):
        if os.path.exists(filename): 
            explode_path = filename.split()
            file_str = '\\ '.join(explode_path)
            date = datetime.datetime.fromtimestamp(os.path.getctime(filename))
            new_date = date.replace(year=self.date.year,month=self.date.month,day=self.date.day)
            # set the file creation date with the "-d" switch
            creation_updater = 'SetFile -d "{}" {}'.format(new_date.strftime('%m/%d/%Y %H:%M:%S'), file_str)
            os.system(creation_updater)

            # set the file modification date with the "-m" switch
            modification_updater = 'SetFile -m "{}" {}'.format(new_date.strftime('%m/%d/%Y %H:%M:%S'), file_str)
            os.system(modification_updater)
        pass
    
    def changeDir(self,path): 
        if os.path.isdir(path): 
            #subdir_str = '' + path
            explode_dir = path.split()
            subdir_str = '\\ '.join(explode_dir)
            date = datetime.datetime.fromtimestamp(os.path.getctime(path))
            new_date = date.replace(year=self.date.year,month=self.date.month,day=self.date.day)
            # set the directory creation date with the "-t" switch
            os.system('touch -t "{}" {}'.format(new_date.strftime('%Y%m%d%H%M'), subdir_str))
	        # set the directory modification date with the "-mt" switch
            os.system('touch -mt "{}" {}'.format(new_date.strftime('%Y%m%d%H%M'), subdir_str))
        pass
