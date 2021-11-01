import re

def is_palin(words):
    forward = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backward = forward[::-1]
    return forward == backward