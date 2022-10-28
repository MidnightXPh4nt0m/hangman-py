import random


class Words:
    def __init__(self) -> None:
        self.analyzed_words = {}
        self.words = []
        self.err = 12
        f = open('words.txt', 'r')
        for i in f.readlines():
            self.words.append(i.replace('\n', ''))
    
    def analyze(self):
        i = 1
        for word in self.words:
            word_properties = {}
            word_properties['word'] = word
            word_properties['len'] = len(word)
            self.analyzed_words[f'{i}'] = word_properties
            i += 1
        if diff == 'easy':
            self.err = 6
        elif diff == 'medium':
            self.err = 8
        elif diff == 'hard':
            self.err = 12

    def gen(self, diff):
        words = []
        for word in self.analyzed_words.keys():
            words.append(self.analyzed_words[word])

        choosen_words = []
        if diff == 'new':
            for word in words:
                if word['len'] <= 3:
                    choosen_words.append(word['word'])
        elif diff == 'easy':
            for word in words:
                if word['len'] > 5 and len(word['word']) <= 6:
                    choosen_words.append(word['word'])
        elif diff == 'medium':
            for word in words:
                if word['len'] > 8 and len(word['word']) <= 12:
                    choosen_words.append(word['word'])
        elif diff == 'hard':
            for word in words:
                if  word['len'] > 10:
                    choosen_words.append(word['word'])
        else:
            return random.choice(words)['word']
        return random.choice(choosen_words)

    def get_error_limit(self):
        return self.err

class Hangman:
    def __init__(self, diff) -> None:
        self.diff = diff
        self.words = Words()
        self.words.analyze()

    def game(self):
        word = self.words.gen(diff=self.diff)
        print(len(word) * '___ ')
        blanks = []
        for i in range(0, len(word)):
            blanks.append('___ ')
        err = self.words.get_error_limit()
        wrong_geusses = 0
        guessed_letters = []
        correct_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while wrong_geusses <= err:
            if wrong_geusses == err:
                print(' :( :( :( You LOSE! ): ): ):')
                print(f'The correct word was: {word}')
                break
            guess = input('Enter your guess: ')
            while guess not in correct_characters:
                guess = input('Your guess should be just letters (not a word or a group of letter or numbers or symbols) enter your guess again:')
            sep_word = list(word)
            result = ''
            if guess in sep_word:
                while guess in sep_word:
                    index = sep_word.index(guess)
                    blanks[index] = guess
                    sep_word[index] = ''
            else:
                wrong_geusses += 1
                guessed_letters.append(guess)
                print(f'\nErrors Remaining: {err - wrong_geusses}')
                print(f'Wrong guesses: {str(guessed_letters)}\n')
            for i in blanks:
                    result += f'{i} '
            print(result)
            if result.replace(' ', '') == word:
                    print('\n\n ----- Congradulations! ----- \n\n')
                    break
            

if __name__ == '__main__':
    print('\t ***** HANGMAN ***** \n\n')
    diff = input('Enter Difficulty(new, easy, medium, hard, or leave it blank for random): ')
    game = Hangman(diff)
    game.game()
