#!/usr/bin/python3

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import move
import os
import time

class FileHandler(FileSystemEventHandler):

    file_extensions = {
        '.jpg'  : 'photos',
        '.png'  : 'photos',
        '.bmp'  : 'photos',
        '.gif'  : 'photos',
        '.txt'  : 'text',
        '.docx' : 'documents',
        '.pdf'  : 'documents',
        '.odt'  : 'documents',
        '.exe'  : 'programs',
        '.bat'  : 'programs',
        '.msi'  : 'programs',
        '.zip'  : 'compressed',
        '.rar'  : 'compressed',
        '.mp4'  : 'videos',
        '.avi'  : 'videos',
        '.webm' : 'videos',
        '.mp3'  : 'music',
        '.WAV'  : 'music',
        '.mid'  : 'midi',
        '.psd'  : 'photoshop_projects',
        '.ai'   : 'illustrator_projects',
        '.jar'  : 'java_files',
        '.html' : 'html_files'
    }

    def __init__(self, tracked_folder):
        self.tracked_folder = tracked_folder
        for value in self.file_extensions.values():
            if not os.path.isdir(f'{self.tracked_folder}\\{value}\\'):
                os.mkdir(f'{self.tracked_folder}\\{value}\\')

        print('Initialized')

    def on_created(self, event):
        time.sleep(1)
        for key in self.file_extensions.keys():      
            if key in event.src_path:
                extension = self.file_extensions[key]
                _name = '_'.join(time.asctime().replace(':', '.').split(' ')) + key
                _dest = f'{self.tracked_folder}\\{extension}\\{_name}'
                move(event.src_path, _dest)
                print('Change detected! Moving file {} to folder {}'.format(event.src_path.split('\\')[-1], _dest.split('\\')[-2]))

    def add_file_extensions(self, extension, folder):
        self.file_extensions[extension] = folder

def initialize_watching():
    handler = FileHandler(r'C:\Users\DOUGLASEDUARDOREISSI\Downloads')
    observer = Observer()
    observer.schedule(handler, handler.tracked_folder, recursive=True)
    observer.start()

    while True:
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()
            break