
#Question 1: Balanced Parentheses
def is_balanced(expression):
    stack = []
    opening_brackets = {'(', '{', '['}
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack

#Question 2: Remove Duplicates

def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

#Question 3: Word Frequency

import string

def word_frequency(sentence):
    words = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

