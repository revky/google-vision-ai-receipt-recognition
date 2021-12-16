from process_text import ProcessText as pt
from cloud_service import get_full_text_from_recipe, ApiConn
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def main(client, pic_path)->list:
    full_text = get_full_text_from_recipe(pic_path, client)
    all_symbols = pt.get_list_of_symbols_from_full_text(full_text)
    rebuilded_lines = pt.build_custom_lines_of_text(all_symbols)
    corrected_lines = pt.correct_mistakes_in_rebuilded_lines(rebuilded_lines)
    return corrected_lines

if __name__ == '__main__':
    app.run(debug=True)