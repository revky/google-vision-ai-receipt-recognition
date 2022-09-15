from flask import Flask, request, jsonify
from cloud_service import get_full_text_from_recipe
from process_text import ProcessText as pt

KEY = "key.json"


def main(client, pic) -> list:
    full_text = get_full_text_from_recipe(client, pic)
    all_symbols = pt.get_list_of_symbols_from_full_text(full_text)
    rebuilded_lines = pt.build_custom_lines_of_text(all_symbols)
    corrected_lines = pt.correct_mistakes_in_rebuilded_lines(rebuilded_lines)
    print(corrected_lines)
    products_json = pt.generate_json(corrected_lines)
    return products_json


app = Flask(__name__)


@app.route("/read_products", methods=["POST"])
def process_image():
    file = request.files['image'].read()
    json_content = main(KEY, file)
    return jsonify(json_content)


if __name__ == "__main__":
    app.run(debug=True)