def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_count = word_count(text)
    character_count = get_character_count(text)
    print(f"--- Begin report of: {book_path} ---")
    print(f"{total_count} words found in the document")
    for key in character_count:
        print(f"The {key} character was found {character_count[key]} times")
    print("--- End of Report ---")

def get_character_count(text):
    lower_text = text.lower()
    character_count = {
        "a": 0,"b": 0,"c": 0,"d": 0,"e": 0, "f": 0,"g": 0,"h": 0,"i": 0,"j": 0,"k": 0,"l": 0,"m": 0,
        "n": 0,"o": 0,"p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,"y": 0,"z": 0
    }
    for key in character_count:
        character_count[key] = lower_text.count(key)
    return character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())


main()
