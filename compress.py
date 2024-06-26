from typing import List, Optional


def alphanumeric_compress(string: str) -> str:
    """ Compress a string by counting the number of consecutive characters """

    def _append_char_count(compressed: List[str], char: Optional[str], count: int) -> None:
        """ Append the character and count to the compressed list """
        if char is None:
            return
        elif count > 1:
            # Append the previous character and count
            compressed.append(char + str(count))
        else:
            # Append the previous character
            compressed.append(char)

    compressed: List[str] = []
    count: int = 1

    initial_idx: int = 0
    prev_char: Optional[str] = None
    curr_char: Optional[str] = None

    # Skip all numeric characters in the beginning and find initial index
    while initial_idx < len(string) and not string[initial_idx].isalpha():
        initial_idx += 1
    
    # Check if initial index is within the string and set previous and current characters
    if initial_idx < len(string):
        prev_char = string[initial_idx]
        curr_char = prev_char # Needed in case string has only one character

    # Iterate through characters in the string starting right after first alphabetic character
    for i in range(initial_idx + 1, len(string)):
        curr_char = string[i]
        # Check if character is a letter
        if not curr_char.isalpha():
            curr_char = prev_char
            continue
        # Check if character is the same as the previous one
        elif curr_char == prev_char:
            count += 1
        # If character is different, append the previous character and count
        else:
            _append_char_count(compressed, prev_char, count)
            count = 1

        prev_char = curr_char

    # Append the last character and count
    _append_char_count(compressed, curr_char, count)
    return ''.join(compressed)
