import re
from typing import List

from math_helper import MathHelper as mh


class ProcessText:
    def is_space_here(symbol) -> bool:
        # checks if symbol has type distinct from 0
        # means is not space character
        return symbol.property.detected_break.type_ != 0

    def get_list_of_symbols_from_full_text(full_text):
        return [symbol
                for page in full_text.pages
                for block in page.blocks
                for paragraph in block.paragraphs
                for word in paragraph.words
                for symbol in word.symbols]

    def build_custom_lines_of_text(all_symbols):
        # for each symbol draws function that represents its current direction and position
        # whenever function detects that two following symbols do not share same linear function
        # it breaks the line
        rebuilded_lines = []
        current_line = ''
        for symbol in all_symbols:
            symbol_cords = symbol.bounding_box.vertices

            if len(current_line) <= 1:
                m, b = mh.find_linear_parameters(symbol_cords)

            if mh.if_share_line(symbol_cords, m, b):
                current_line += symbol.text
                current_line += " " if ProcessText.is_space_here(symbol) else ""
                m, b = mh.find_linear_parameters(symbol_cords)
            else:
                rebuilded_lines.append(current_line)
                current_line = symbol.text

        return rebuilded_lines

    def contains_product(line: str) -> bool:
        if re.search(r'\s\d+[,.]+?\d\d\s?[0OABC846]\s', line):
            return True
        return False

    def has_needed_length(line: str) -> bool:
        if len(line) > 15:
            return True
        return False

    def has_product_properties(line: str) -> bool:
        if ProcessText.contains_product(line) and ProcessText.has_needed_length(line):
            return True
        return False

    def extract_price(text_content: str):
        t = text_content.replace(':', '0')
        pattern = r'[^.,-]\.?(\s?\d+[,.]+?\d\d\s?[0OABC846]\s)'
        if re.search(pattern, t) and len(t) > 25:
            price = re.findall(pattern, t)
            return price[0]
        return ""

    def correct_mistakes_in_rebuilded_lines(rebuilded_lines):
        # iterate through all the items and if item with specific characteristic is found
        # add it to the previous one, and skip the current iteration
        corrected_lines = []
        for i in range(len(rebuilded_lines)):
            current_item = rebuilded_lines[i]
            if ProcessText.contains_product(current_item) and len(
                    current_item) < 25 and not ProcessText.contains_product(corrected_lines[-1]):
                corrected_lines[-1] += current_item
                continue
            corrected_lines.append(current_item)

        return corrected_lines

    def generate_json(corrected_lines: List[str]):
        products = []
        for i, line in enumerate(corrected_lines):
            if ProcessText.has_product_properties(line):
                price = ProcessText.extract_price(line)
                line = line.removesuffix(price)
                products.append({'name': line.strip(), 'quantity': 1,
                                 'price': float(re.findall(r'\d+\.\d+', price.strip())[0]),
                                 'id': i})
        return products
