def get_words(contents):
    return len(contents.split())

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = get_words(contents)
    print(f"{word_count} words found in the document")

main()






#def main():
#    contents = get_text("books/frankenstein.txt")
#    from stats import get_num_words    
#    from stats import get_letters
#    
#main()        
