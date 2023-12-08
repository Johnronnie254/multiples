# Project Title: Multiple Code Challenge

## Overview

This project contains three Python functions that address different tasks related to string manipulation, sequence processing, and word frequency analysis.

1. **is_balanced(expression):** Determines if a given string containing parentheses, curly braces, and square brackets is balanced.

2. **remove_duplicates(sequence):** Removes duplicates from a given sequence (list or tuple) while maintaining the original order of elements.

3. **word_frequency(sentence):** Calculates the frequency of each word in a given sentence.

## Usage

### 1. is_balanced(expression)

The function `is_balanced` checks whether a string containing parentheses, curly braces, and square brackets is balanced.

#### Example

```python
from your_module import is_balanced

expression = "(({}))"
result = is_balanced(expression)
print(result)  # Output: True

###test 2

from your_module import remove_duplicates

sequence = [1, 2, 3, 1, 2, 4, 5]
result = remove_duplicates(sequence)
print(result)  # Output: [1, 2, 3, 4, 5]


##test 
from your_module import word_frequency

sentence = "This is a sample sentence. This sentence is a sample."
result = word_frequency(sentence)
print(result)
# Output: {'this': 2, 'is': 2, 'a': 2, 'sample': 2, 'sentence': 2}


