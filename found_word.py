def play_found_word():
    text, text_, word, word_ = found_word_informations()

    mark, mark_2 = found_word_searching(text, text_, word, word_)

    highlighted_word_in_the_text(text_, mark, mark_2)








def found_word_informations():
    text = input("Enter the text you want to search for -> ").strip().lower()
    word = input("Enter the word you want to search in text -> ").strip().lower()

    text_ = []
    for letter in text:
        text_.append(letter)
    word_ = []
    for letter in word:
        word_.append(letter)
    text_.append(" ")
    text_.append(" ")

    return(text, text_, word, word_)

def found_word_searching(text, text_, word, word_):
    mark = 0
    mark_2 = 0

    for c in range(0, len(text)):
        cont = c
        cont_2 = 0
        
        for k in range(0, len(word)):
            if(text_[cont] == word_[k]):
                
                cont_2 += 1
            else:
                break
            cont += 1
            if(cont_2 == len(word) and text_[cont] == ' '):
                mark = cont - len(word)
                mark_2 = cont + 1
                print("\nThe word was found\n")
    
    return(mark, mark_2)

def highlighted_word_in_the_text(text_, mark, mark_2):
    cont = 0
    cont_2 = 0
    marked_text = []

    for c in range(0, len(text_)):
        if(c == mark):
            marked_text.append("\033[1;34m[\033[m")
            cont += 1
        elif(c == mark_2):
            marked_text.append("\033[1;34m]\033[m")
            cont += 1
        else:
            marked_text.append(text_[cont_2])
            cont_2 += 1

    print(*marked_text, sep='')
    print("")


if(__name__ == "__main__"):
    play_found_word()