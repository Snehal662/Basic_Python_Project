#importing the required library
from spellchecker import SpellChecker

#Creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
        
        def correct_text(self, text):
            words = text.split()
            corrected_words = []

            for word in words:
                corrected_word = self.spell.correction(word)
                if corrected_word != word.lower():
                    print(f'Correcting "{word}" to"{corrected_word}"')
                    corrected_words.append(corrected_word)
#returning the corrected text
return ' '.join(corrected_words)

#running the SpellCheckerApp
def run(self):
    print("\n---Spell Checker---")

    while True:
        text = input('Enter text to check (or type "exit"to quit):')

        if text.lower() == 'exit':
            print('Closing the program....')

            corrected_text = self.correct_text(text)
            print(f'Corrected Text : {corrected_text}')

#running the main program
if __name__ == "__main__":
    SpellCheckerApp().run()
