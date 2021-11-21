from preprocess_script import Procedure
from PIL import Image
import os
import io

class FileManager:
    def __init__ (self, procedure):
        self.proc = procedure
        self.file_name = self.proc.td.image_path.split('\\')[-1][:-4]
        self.text_lines = self.proc.td.get_all_lines()
        self.image_bytes = self.proc.td.content
        self.image =  Image.open(io.BytesIO(self.image_bytes))
        self.cwd = os.getcwd()
        self.folder_path = os.path.join(self.cwd,self.file_name)
        self.image_name = self.file_name+'.jpg'

    def create_folder(self):
        os.mkdir(self.folder_path)

    def save_text_file(self):
        with open(os.path.join(self.folder_path,self.file_name+'.txt'), 'w+', encoding = 'UTF-8') as file:
            [file.writelines(line+'\n') for line in self.text_lines]

    def save_image(self):
        self.image.save(os.path.join(self.folder_path, self.image_name))

def Main(credentials, img_path):
    fm = FileManager(Procedure(credentials, img_path))
    fm.create_folder()
    fm.save_text_file()
    fm.save_image()