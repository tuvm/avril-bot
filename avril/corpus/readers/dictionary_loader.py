from os.path import join, dirname
from avril.util.file_io import read


class DictionaryLoader:
    def __init__(self, filepath):
        data_folder = join(dirname(dirname(__file__)), "data")
        data_file = join(data_folder, filepath)
        self.data_file = data_file
        self.words_data = None

    @property
    def words(self):
        if not self.words_data:
            content = read(self.data_file).strip()
            words = content.split("\n")
            self.words_data = words
        return self.words_data
