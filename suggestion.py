

class Suggestion(object):
    def __init__(self, type, wordIndex, goodLetter, badLetter, position, probability, frequency):
        self.type = type
        self.wordIndex = wordIndex
        self.goodLetter = goodLetter
        self.badLetter = badLetter
        self.position = position
        self.probability = probability
        self.bigram = 1
        self.frequency = frequency
    
    

class WordSuggestionPair(object):
    def __init__(self, word, correct):
        self.word = word
        self.correct = correct
        self.suggestions = [] 
        self.bigramOn = True
        self.totalP = .0001
        self.totalF = 0.0001
        self.totalB = 0.0001
        self.totalBigramOff = 0.0001
        self.totalBigramOn = 0.0001
        self.displayed = False 

    def addSuggestion(self, suggestion):
        self.suggestions.append(suggestion)

    def sortList(self,bigramOn):
        self.bigramOn = bigramOn
        self.suggestions.sort(key=self.sortSuggestions, reverse=True)
    

    def sortSuggestions(self, suggestion):
        bigram = 1
        if self.bigramOn:
            bigram = float(suggestion.bigram)
        return float(suggestion.frequency) * float(suggestion.probability) * bigram
    
    def __str__(self) -> str:
        return "" + self.word 
    
    def __repr__(self) -> str:
        return "" + self.word 