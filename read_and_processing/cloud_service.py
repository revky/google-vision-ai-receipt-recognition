import os

from google.cloud import vision


class ApiConn:
    def __init__(self, cred):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred
        self.__client = vision.ImageAnnotatorClient()

    def get_client(self):
        return self.__client


def get_full_text_from_recipe(api_client, encoded_image):
    image = vision.Image(content=encoded_image)
    response = api_client.document_text_detection(image=image)
    full_text = response.full_text_annotation
    return full_text
