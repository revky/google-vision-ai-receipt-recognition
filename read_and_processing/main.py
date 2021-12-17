from process_text import ProcessText as pt
from cloud_service import get_full_text_from_recipe, ApiConn
import argparse
from pprint import pprint

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, help='path to image')
ap.add_argument('-c','--cred', required=True, help='path to google api credentials')
args = vars(ap.parse_args())
api = ApiConn(args['cred'])

def main(client, pic_path)->list:
    full_text = get_full_text_from_recipe(pic_path, client)
    all_symbols = pt.get_list_of_symbols_from_full_text(full_text)
    rebuilded_lines = pt.build_custom_lines_of_text(all_symbols)
    corrected_lines = pt.correct_mistakes_in_rebuilded_lines(rebuilded_lines)
    return corrected_lines


pprint(main(api.get_client(), args['image']))