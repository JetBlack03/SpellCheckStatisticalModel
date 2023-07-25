

class Suggestion(object):
    def __init__(self, type, wordIndex, goodLetter, badLetter, position, probability, bigram, frequency):
        self.type = type
        self.wordIndex = wordIndex
        self.goodLetter = goodLetter
        self.badLetter = badLetter
        self.position = position
        self.probability = probability
        self.bigram = bigram
        self.frequency = frequency
    
    

