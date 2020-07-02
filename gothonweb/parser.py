class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1] # this is the 'princess'
        self.verb = verb[1]
        self.object = obj[1]

    # checks whether a list of words exists and has items
    # and returns the wordtype of the first item
def peek(word_list):
    if word_list: # exists and has items
        wordTuple = word_list[0]
        return wordTuple[0]
    else:
        return None
    # removes the first item from a list of words. if the
    # wordtype of the removed item matches an expected
    # type, it is returned.
def match(word_list, expecting):
    if word_list:
        wordTuple = word_list.pop(0)

        if wordTuple[0] == expecting:
            return wordTuple
        else:
            return None
    else:
        return None

    # skips words of a certain type from the list of words
    # by not doing anything with the returns of peek and match
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

    # skips all stop words and returns the Word-Tuple when
    # it finds a word of type 'verb'
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        # list wird nicht gepopped
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
