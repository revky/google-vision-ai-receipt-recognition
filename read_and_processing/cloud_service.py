import os

from google.cloud import vision


def get_full_text_from_recipe(cred, content):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred
    vision_client = vision.ImageAnnotatorClient()
    response = vision_client.annotate_image({'image': {'content': content}, 'features': [
        {'type_': vision.Feature.Type.DOCUMENT_TEXT_DETECTION}],
                                             'image_context': {
                                                 "text_detection_params": {"advanced_ocr_options": ["legacy_layout"]}}})
    full_text = response.full_text_annotation
    return full_text
