# Test file in purpouse of testing and analysing Google Vision output

import io
import os

from PIL import Image

from detect_text import Procedure


class FileManager:
    def __init__ (self, procedure, limit = 10):
        self.proc = procedure
        self.file_name = self.proc.td.image_path.split('\\')[-1][:-4]
        self.text_lines = self.proc.td.get_all_lines(limit)
        self.image =  Image.open(io.BytesIO(self.proc.td.content))
        self.cwd = os.getcwd()
        self.folder_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)),self.file_name)
        self.image_name = self.file_name+f'limit_{limit}'+'.jpg'
        self.text_file = os.path.join(self.folder_path,self.file_name+f'limit_{limit}'+'.txt')

    def create_folder(self):
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

    def save_text_file(self):
        with open(os.path.join(self.text_file), 'w+', encoding = 'UTF-8') as file:
            [file.writelines(line+'\n') for line in self.text_lines]

def main(credentials, img_path, limit):
    fm = FileManager(Procedure(credentials, img_path), limit)
    fm.create_folder()
    fm.save_text_file()
