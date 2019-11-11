from avril.corpus.corpus import Corpus
from avril.corpus.readers.dictionary_loader import DictionaryLoader

viet_dict_11K = DictionaryLoader('Viet11K.txt')
viet_dict_22K = DictionaryLoader('Viet22K.txt')
viet_dict_39K = DictionaryLoader('Viet39K.txt')
viet_dict_74K = DictionaryLoader('Viet74K.txt')

__all__ = ['Corpus', 'DictionaryLoader']
