# 2D Array String Validation

## Description
This project validates whether a given string follows specific movement rules within a 4x4 character matrix. The string is valid if:

1. Each character exists in the 2D array.
2. Each character in the string appears in the same row or column as the previous character.

## Example 2D Array
```plaintext
  0  1  2  3
0 b  x  h  o
1 a  b  j  p
2 r  h  r  j
3 n  m  b  v
```

Example string: `"abhj"`

## Implementation
The program follows these steps:
1. Locate all occurrences of each character in the 2D array.
2. Start from the first character's position.
3. Ensure the next character appears in the same row or column as the previous character.
4. If all characters follow this rule, the string is valid.
