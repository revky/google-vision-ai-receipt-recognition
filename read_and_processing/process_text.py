from math_helper import MathHelper as mh
import re
class ProcessText:
    def is_space_here(symbol)->bool:
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

    def if_price_without_product(text_line):
        return re.search(r'[^\-]\s\d+[,.]+?\d\d\s?[0OABC]\s', text_line)

    def correct_mistakes_in_rebuilded_lines(rebuilded_lines):
        # iterate through all the items and if item with specific characteristic is found
        # add it to the previous one, and skip the current iteration
        processed_lines = []
        for i in range(len(rebuilded_lines)):
            current_item = rebuilded_lines[i]
            if ProcessText.if_price_without_product(current_item) and len(current_item) < 25 and not ProcessText.if_price_without_product(processed_lines[-1]):
                processed_lines[-1] += current_item
                continue
            processed_lines.append(current_item)

        return processed_lines
