import os
import msgpack
import pkg_resources


class CharConverter:

    def __init__(self, option='v2s'):
        """
        Initialize the converter with a option format.

        :param option: option format, either 'v2s' (simplified) or 'v2t' (traditional).
        """
        if option not in ['v2s', 'v2t']:
            raise ValueError("Option must be either 'v2s' (simplified) or 'v2t' (traditional).")
        mapping_file_path = pkg_resources.resource_filename('char_converter', f'data/{option}.msgpack')

        with open(mapping_file_path, 'rb') as f:
            self.mapping = msgpack.unpack(f, raw=False)


    def convert(self, text):
        """
        Convert the text based on the mapping.

        :param text: The input text.
        :return: Converted text.
        """
        converted_text = [self.mapping.get(char, [char])[0] for char in text]
        return ''.join(converted_text)


    def convert_file(self, input_file, output_file):
        """
        Convert the text from an input file and save the converted text to an output file.

        :param input_file: Path to the input file.
        :param output_file: Path to the output file.
        """
        with open(input_file, 'r', encoding='utf-8-sig') as f_input:
            input_text = f_input.read()

        converted_text = self.convert(input_text)

        with open(output_file, 'w', encoding='utf-8-sig') as f_output:
            f_output.write(converted_text)