from stats import get_book_text
from stats import get_num_words
from stats import count_lower_case_characters
from stats import sort_dict_by_value

def main():
    filepath="books/frankenstein.txt"
    book_text=get_book_text(filepath)
    words=get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    da=count_lower_case_characters(book_text)
    lod=sort_dict_by_value(da,True)
    for item in lod:
        k=item.get("key")
        v=item.get("value")
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")

main()

