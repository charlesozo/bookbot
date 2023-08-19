def main():
    bookpath = "github.com/charlesozo/bookbot/books/frankeinstein.txt"
    text = get_book_path(bookpath)
    num_words = get_number_of_words(text)
    print(f"{num_words} was found in the document")
    word_dic = count_letters(text)
    print("--- End report ---")
def count_letters(word):
    words_lst = word.split()
    words_dic = {}
    char_lst = []
    for words in words_lst:
        for word in words.lower():
            if word in words_dic:
                words_dic[word] += 1
            else:
                words_dic[word] = 1
    for keys, values in words_dic.items():
        if keys.isalpha():
            char_lst.append( (keys, values))
    sorted_word = lambda x:x[1]
    char_lst.sort(key=sorted_word, reverse=True)
    for i in char_lst:
        print(f"The {i[0]} character was found {i[1]} times")
            
        
def get_number_of_words(string):
    words = string.split()
    return len(words)
def get_book_path(path):
    with open(path) as f:
        return f.read()
main()
