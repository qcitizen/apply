def collapse(text):
    ret = ""
    prev = ""
    num_prev = 1
    for char in text:
        if char.isalpha():
            if char == prev:
                num_prev += 1
            else:
                if prev != "":
                    ret += prev
                    if num_prev > 1:
                        ret += str(num_prev)
                prev = char
                num_prev = 1
    if prev != "":
        ret += prev
        if num_prev > 1:
            ret += str(num_prev)
    return ret
    
def run_tests():
    assert(collapse("aaabccccdd") == "a3bc4d2")
    assert(collapse("aaaaaffffffffffc") == "a5f10c")
    assert(collapse("abcd") == "abcd")
    assert(collapse("ccceee12eccceee") == "c3e4c3e3")
    assert(collapse("effeac01cb65c") == "ef2eac2bc")
    print("Tests passed")
    
if __name__ == "__main__":
    run_tests()
