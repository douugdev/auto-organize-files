#!/usr/bin/python3

from .wdog import FileHandler
from shutil import move
import os
import time

class IterHandler(FileHandler):
    def iter_folder(self):
        _dir = os.listdir(self.tracked_folder)
        tmp_dir = _dir
        for file in tmp_dir:
            # Checks if the file is a directory and then removes it from the file list
            if os.path.isdir(f'{self.tracked_folder}\\{file}'):
                print('found a folder')
                _dir.remove(file)

        for file in _dir:
            time.sleep(0.3)
            for key in self.file_extensions.keys():      
                if key in file:
                    extension = self.file_extensions[key]
                    _dest = f'{self.tracked_folder}\\{extension}\\{file}'
                    move(f'{self.tracked_folder}\\{file}', _dest)
                    print('Still itering... Moving file {} to folder {}'.format(file, _dest.split('\\')[-2]))


def initialize_iter():
    handler = IterHandler(r'YOUR FOLDER HERE')
    handler.iter_folder()
