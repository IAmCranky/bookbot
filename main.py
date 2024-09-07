def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    words = get_words(text)
    lower = get_lower(text)
    letters = get_letters(lower)
    
    letter_list = sorted(letters.items(), key=lambda item: item[1], reverse = True)
    final_list = [f"The '{l}' character was found {num} times" for l, num in letter_list]

    print(f"""--- Begin reports of {path}---""")
    print()
    print(f"""{words} words found in the document""")
    print()

    for i in final_list:
        print(i)

    print()
    print("--- End report ---")
    

def get_text(path):
    with open(path) as f:
        return f.read()

def get_words(words):
    count = words.split()
    return len(count)

def get_letters(lower):
    letters = {}
    for i in lower:
        if i.isalpha():
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    return letters
    


def get_lower(text):
    string = text.lower()
    return string
        

main()
