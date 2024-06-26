from typing import List


def alphanumeric_compress(string: str) -> str:
    """ Compress the string by counting the number of consecutive characters """

    def _append_char_count(compressed: List[str], char: str, count: int) -> None:
        """ Append the character and count to the compressed list """
        if count > 1:
            # Append the previous character and count
            compressed.append(char + str(count))
        else:
            # Append the previous character
            compressed.append(char)

    def _remove_numeric(string: str) -> str:
        """ Remove all numeric characters from the string """
        return ''.join([c for c in string if not c.isdigit()])
    
    compressed: List[str] = []
    count: int = 1

    clean_str: str = _remove_numeric(string)
    if not clean_str:
        return ""
    prev_char: str = clean_str[0]
    curr_char: str = prev_char # in case the string has only one character

    # Iterate through characters in the string starting right after first alphabetic character
    for i in range(1, len(clean_str)):
        curr_char = clean_str[i]
        # Check if character is the same as the previous one
        if curr_char == prev_char:
            count += 1
        # If character is different, append the previous character and count
        else:
            _append_char_count(compressed, prev_char, count)
            count = 1

        prev_char = curr_char

    # Append the last character and count
    _append_char_count(compressed, curr_char, count)
    return ''.join(compressed)
