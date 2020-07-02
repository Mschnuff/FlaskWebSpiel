import re

north = ('direction', 'north')
south = ('direction', 'south')
east = ('direction', 'east')
west = ('direction', 'west')

go = ('verb', 'go')
kill = ('verb', 'kill')
eat = ('verb', 'eat')

the = ('stop', 'the')
iN = ('stop', 'in')
of = ('stop', 'of')

bear = ('noun', 'bear')
princess = ('noun', 'princess')

lexicon = [north, south, east, west,
           go, kill, eat,
           the, iN, of,
           bear, princess]
def scan(string):
    # split up the string into a list of words
     #|,|;|!|:|\.
    #split_chars = [' ', ',', '.', '!', ':']
    listOfWords = re.split('[,.;! :*/%]', string)

    # der ansatz unten ist viel zu kompliziert. besser ist es die vorgefertigte funktion re zu importieren.
    # aber eine nette übung. :)
    """listOfWords.append(string)
     #print(listOfWords)
    for char in split_chars:
            for word in listOfWords:
                #print(listOfWords)
                listOfWords.pop(listOfWords.index(word))
                splitted_list = word.split(char)
                if splitted_list:
                    reverse_list = splitted_list.reverse()
                    print(splitted_list)
                    print(reverse_list)
                for new_word in reverse_list:
                    listOfWords.insert(0, new_word) """
                     
    print(listOfWords)
    # a tupel for each "known" Word
    
    # this list will contain all the directions that are found in
    # the sentence
    listOfFoundWords = []
    # loops through the sentence and puts each direction into the
    # the listofDirections
    for word in listOfWords:
        wordFound = False
        try:
            number_tupel = ('number', int(word))
            listOfFoundWords.append(number_tupel)
            wordFound = True
        except ValueError:
            for known_word in lexicon:
                if word == known_word[1]:
                    listOfFoundWords.append(known_word)
                    wordFound = True
        if not(wordFound):
            error_tupel = ('error', word)
            listOfFoundWords.append(error_tupel)
    return listOfFoundWords
