def get_words(contents):
    return len(contents.split())

def count_letters(contents):
    result = {}

    for l in contents:
        l = l.lower()
        if l not in result:
            result[l] = 0
        result[l] += 1

    return result

def sort_on(dict):
    return dict["num"]

def sorted_count_letters(letters):
    results = []
    for letter in letters:
        if letter.isalpha():
            dict = {}
            dict["char"] = letter
            dict["num"] = letters[letter]
            results.append(dict)
    results.sort(reverse=True, key=sort_on)
    return results
    
