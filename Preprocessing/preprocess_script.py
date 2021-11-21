import os
import io
from google.cloud import vision
from math_helper import MathHelper

class ApiConnector:
    def __init__(self, cridentials_path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cridentials_path
        self.client = vision.ImageAnnotatorClient()

class TextDetection:
    def __init__(self, client, image_path):
        self.image_path = image_path
        self.client = client
        with io.open(self.image_path,'rb') as image_bytes:
            self.content = image_bytes.read()

        self.image = vision.Image(content=self.content)
        self.response = self.client.document_text_detection(image=self.image)
        self.full_text = self.response.full_text_annotation
    
    def get_all_symbols(self) -> list:
        return [
            symbol 
        for page in self.full_text.pages
        for block in page.blocks
        for paragraph in block.paragraphs
        for word in paragraph.words
        for symbol in word.symbols
        ]


    def get_all_lines(self) -> list:
        lines = []
        line_str = ''
        math = MathHelper

        for symbol in self.get_all_symbols():
            if len(line_str) <= 1:
                m,b = math.find_linear_parameters(symbol.bounding_box.vertices)

            if math.share_line(symbol.bounding_box.vertices, m, b):
                line_str += symbol.text
                line_str += " " if math.is_space_here(symbol) else ""
                m,b = math.find_linear_parameters(symbol.bounding_box.vertices)
                if m == 0:
                    continue   
            else:
                lines.append(line_str)
                line_str = symbol.text

        return lines

class Procedure:
    def __init__(self, credentials_path, img_path):
        self.auth = ApiConnector(credentials_path)
        self.client = self.auth.client
        self.td = TextDetection(self.client, img_path)
    
