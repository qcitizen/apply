from collections import defaultdict


def compress(message: str) -> str:
    """Compress an alphanumeric  by collapsing consecutive values.

    Args:
        message: The message to compress

    Returns:
        str: The compressed message

    >>> compress('aaabccccdd')
    a3bc4d2
    >>> compress('aaaaaffffffffffc')
    a5f10c
    """
    letter_counts = defaultdict(int)
    previous_letter = None
    compressed_message = ""
    for letter in message:
        if letter.isdigit():
            continue

        if previous_letter and previous_letter != letter:
            current_letter_count = letter_counts.get(previous_letter)
            compressed_message += f'{previous_letter}{current_letter_count}'
        else:
            # previous_letter is equivalent to letter
            letter_counts[letter] += 1

        previous_letter = letter

    return compressed_message
