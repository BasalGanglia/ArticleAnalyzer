from collections import Counter
from typing import Dict

import spacy

from .debugging import app_logger as log

class DataProcessor():

    def __init__(self):
        log.info('spacy: loading model')
        self.nlp = spacy.load('en_core_web_sm')
        log.info('spacy: loaded model')
        self.skip = ['CARDINAL', 'MONEY', 'ORDINAL', 'DATE', 'TIME']
    def entities(self, doc) -> Counter:
        t = [e.text.lower() for e in doc.ents i e.label_ not in self.skip]
        return Counter(t)
    
    def process(self, text: str) -> Dict:
        return {'entities': self.entities(self.nlp(text))}
    
    def process_message(self, post):
        return None
