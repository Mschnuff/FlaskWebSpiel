from nose.tools import *
from gothonweb.parser import *


def test_Sentence():
    subjTuple = ('noun', 'ich')
    verbTuple = ('verb', 'bin')
    objTuple = ('noun', 'Schöner Mensch')
    testSentence = Sentence(subjTuple, verbTuple, objTuple)
    assert_equal(testSentence.subject, subjTuple[1])
    assert_equal(testSentence.verb, verbTuple[1])
    assert_equal(testSentence.object, objTuple[1])

def test_peek():
    empty_word_list = []
    peek_word_list = [('test', 'bla')]
    peek_word = peek_word_list[0]
    assert_equal(peek(empty_word_list), None)
    assert_equal(peek(peek_word_list), peek_word[0])

def test_match():
    empty_word_list = []
    assert_equal(match(empty_word_list, 'völlig_egal'), None)
    match_word_list = [('test', 'bla'), ('nicht_test', 'nochmehrbla')]
    match_tuple = ('test', 'bla')
    assert_equal(match(match_word_list, 'test'), match_tuple)
    assert_equal(match(match_word_list, 'test'), None)
    match_word_list = [('test', 'bla'), ('nicht_test', 'nochmehrbla')]
    assert_equal(match(match_word_list, 'quatsch'), None)

def test_parse_verb():
    pv_word_list = [('stop', 'egal'), ('verb', 'auchegal')]
    verb_tuple_from_list = pv_word_list[1]
    messed_up_word_list = [('kram', 'egal'), ('verb', 'blabla')]
    assert_equal(parse_verb(pv_word_list), verb_tuple_from_list)
    assert_raises(ParserError, parse_verb, messed_up_word_list)

def test_parse_object():
    po_word_list = [('stop', 'kram'), ('stop', 'wumms'), ('noun', 'obejct')]
    obj_tuple_from_list = po_word_list[2]
    po_word_listb = [('stop', 'kram'), ('direction', 'wumms')]
    obj_tuple_from_listb = po_word_listb[1]
    assert_equal(parse_object(po_word_list), obj_tuple_from_list)
    assert_equal(parse_object(po_word_listb), obj_tuple_from_listb)
    messed_up_word_list = [('verb', 'messed'), ('verb', 'up')]
    assert_raises(ParserError, parse_object, messed_up_word_list)

def test_parse_subject():
    ps_word_list = [('stop', 'einNomen'), ('noun', 'einNomen'), ('egal', 'egal')]
    ps_word_listb = [('stop', 'ein'), ('stop', 'tolles'), ('verb', 'wort')]
    ps_word_listb_copy = ps_word_listb
    ps_tuple = ('noun', 'einNomen')
    fixed_tuple = ('noun', 'player')
    assert_equal(parse_subject(ps_word_list), ps_tuple)
    assert_equal(parse_subject(ps_word_listb), fixed_tuple)
    skip(ps_word_listb_copy, 'stop')
    assert_equal(ps_word_listb, ps_word_listb_copy)
    messed_up_word_list = [('direction', 'norden'), ('noun', 'ich')]
    assert_raises(ParserError, parse_subject, messed_up_word_list)

def test_parse_sentence():
    word_list = [('noun', 'Ich'), ('verb', 'bin'),  ('stop', 'ein'),
        ('noun', 'Hamster')]
    messed_up_word_list = [('stop', 'dieser'), ('noun', 'Satz'), ('verb', 'ist'),
        ('stop', 'nicht'), ('adjektiv', 'parsbar')]
    #assert_equal(parse_subject(word_list), ('noun', 'Ich'))
    #assert_equal(parse_verb(word_list), ('verb', 'bin'))
    #assert_equal(parse_object(word_list), ('noun', 'Hamster'))
    mein_sentence = parse_sentence(word_list)
    assert_equal(mein_sentence.subject, 'Ich')
    assert_equal(mein_sentence.verb, 'bin')
    assert_equal(mein_sentence.object, 'Hamster')
    # !!! wichtig !!! assert_equal testet bei objekten auf Identität
    # nicht auf gleichheit !!! wichtig !!!
    #assert_equal(Sentence(('noun', 'Ich'), ('verb', 'bin'), ('noun', 'Hamster')),
    #    parse_sentence(word_list))
    assert_raises(ParserError, parse_sentence, messed_up_word_list)
