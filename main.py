def compress(input_str: str) -> str:
    """
    Compresses the input string by replacing repeated characters with the character followed by the count of the
    repetitions. Characters that do not repeat will not be followed by the count of repetitions. Additionally, the
    function will strip numbers from the input string.
    :param input_str: The string to be compressed.
    :return: The compressed string.
    """

    if not input_str:
        return ""

    result = ""
    count = 1
    prev_char = input_str[0]

    for char in input_str[1:]:
        if not char.isalpha():
            continue

        if char == prev_char:
            count += 1
        else:
            result += prev_char if count == 1 else prev_char + str(count)
            prev_char = char
            count = 1

    result += prev_char if count == 1 else prev_char + str(count)

    return result


if __name__ == "__main__":
    assert compress('aaabccccdd') == 'a3bc4d2'
    assert compress('aaaaaffffffffffc') == 'a5f10c'
    assert compress('abcd') == 'abcd'
    assert compress('ccceee12eccceee') == 'c3e4c3e3'
    assert compress('effeac01cb65c') == 'ef2eac2bc'

    # Test case for empty string
    assert compress('') == ''

    # Additional edge case for string containing special characters
    assert compress('ef#fea$$c01cb/&@65c') == 'ef2eac2bc'
