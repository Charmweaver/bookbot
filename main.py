from stats import get_words, count_letters, sorted_count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    results = []
    word_count = get_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words(text)} total words")
    print("--------- Character Count -------")
    print(count_letters(results))
    letters = count_letters(text)
    sorted_letters = sorted_count_letters(letters)
    for dict_letter in sorted_letters:
        print(f"{dict_letter['char']}: {dict_letter['num']}")
    print()
    print("============= END ===============")

main()






#def main():
#    contents = get_text("books/frankenstein.txt")
#    from stats import get_num_words    
#    from stats import get_letters
#    
#main()        
