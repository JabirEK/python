def generate_key(passcode):
    key_word = 0
    for leter in passcode:
        key_word = key_word + ord(leter)
    return key_word

print(generate_key("banana"))

if __name__=='__main__':
    print("Here run only in main file not in importing file")