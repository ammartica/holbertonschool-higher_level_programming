#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    if strlen <= 0:
        my_tuple = (strlen, None)
    else:
        my_tuple = (strlen, sentence[0])
    return my_tuple
