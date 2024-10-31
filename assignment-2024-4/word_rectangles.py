import sys
import copy


#-----------------------------------------------------------------------------------------------------------------------
def update_array(word:str, A):
    common_pref = ""
    current_col = 0
    global max_col 
    
    for i, letter in enumerate(word):
        letter_num = ord(letter)
        if A[current_col][letter_num-64] == 0:
            if(word == common_pref):
                A[current_col][0] = word
                return
            else:
                A[current_col][letter_num-64]=word
                return
        elif type(A[current_col][letter_num-64]) == int:
            current_col = A[current_col][letter_num-64]-1
            common_pref += letter
        else:
            old_word = A[current_col][letter_num-64]
            k = 0

#With the loop 'while' we want the characters in both words match and we check that we haven't reached the end of either word
            while k < len(old_word) and k < len(word) and old_word[k] == word[k]:
                A.append([0] * 27)  
                max_col += 1  
                A[current_col][ord(word[k]) - 64] = max_col + 1  
                common_pref += word[k]  
                current_col = A[current_col][ord(word[k]) - 64] - 1 
                k += 1  
                if(common_pref==old_word):
                    A[max_col][0]=old_word
                else:
                    A[max_col][ord(old_word[i])-64]=old_word
                A[max_col][ord(word[i])-64]=word
                return

#--------------------------------------------------------------------------------------------------------------
#In this function we print the trie based on the priciples/format of the excercise
def print_trie(trie_array):
    abc = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, len(trie_array[0])):
        if(type(trie_array[0][i])==int):
            print(f"{abc[i]} [{trie_array[0][i]}", end="")
        else:
            print(f"{abc[i]} ['{trie_array[0][i]}'", end="")

        for j in range(1, len(trie_array)):
            if(type(trie_array[j][i])==int):
                print(f", {trie_array[j][i]}", end="")
            else:
                print(f", '{trie_array[j][i]}'", end="")
        print("]\n")

#--------------------------------------------------------------------------------------------------------------------------
#(it's not finished)
def search(n, m, trie_array, words_list, all_words):
    # check every horizontal word created if it exists in the trie
    # if at least one doesn't exist then we have to check for other words
    for i in range(0, m):
        word = ''.join([word[i] for word in words_list])
    


#-----------------------------------------------------------------------------------------------------------------
#we read the file and take the parameters
horizontal_path = sys.argv[2]

with open(horizontal_path, 'r') as file:
    lines = file.readlines()
    horizontal_words = [line.rstrip('\n') for line in lines]

# we sort them because we want to advantage their alphabeticl sequence
horizontal_words.sort(

trie_array = [[0] * 27]
max_col = 0
count = 0
for word in horizontal_words:
    update_array(word, trie_array)

#first case 
if len(sys.argv) == 3 and sys.argv[1] == "print_trie":
    print_trie(trie_array)

#second case
elif len(sys.argv) == 5 and sys.argv[1] == "find_rectangles":
    horizontal_size = len(horizontal_words[0])
    with open(sys.argv[3], 'r') as file:
        lines = file.readlines()
        vertical_words = [line.rstrip('\n') for line in lines]
    vertical_size = len(vertical_words[0])

    for word in vertical_words:
        search(horizontal_size, vertical_size, trie_array, word, vertical_words)
