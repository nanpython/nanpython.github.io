from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '950')
Config.set('graphics', 'height', '400')
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

import spacy

class POS(FloatLayout):
    input_text = ObjectProperty()
    out_label = ObjectProperty()


    def __init__(self, **kwargs):
        super(POS, self).__init__(**kwargs)
        self.nlp = spacy.load("en_core_web_sm")

    def submit_btn(self):
        sentence = self.input_text.text
        results = sentence + "\n\n"
        doc = self.nlp(sentence)

        for token in doc:
            print(token)
            results += str(token) + " (" + str(spacy.explain(token.tag_)) + ")\n"
        
        self.out_label.text = results
        self.input_text.text = ""

class Main(App):

    def build(self):
        return POS()

if __name__ == '__main__':
    Main().run()