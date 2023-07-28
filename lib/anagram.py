# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
        
    def match(self, word_list):
        matching_words = []
        
        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                matching_words.append(word)
                
        return matching_words
    