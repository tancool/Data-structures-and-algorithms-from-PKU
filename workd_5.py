
def index(char_father,char_son):
    char_fater_index = 0
    char_son_index = 0

    while char_fater_index<len(char_father) and char_son_index < len(char_son):
        
        if char_father[char_fater_index] == char_son[char_son_index]:
            
            char_fater_index = char_fater_index + 1
            char_son_index = char_son_index + 1
        else:
            char_fater_index  = char_fater_index -  char_son_index + 1
            char_son_index = 0
    
    if char_son_index >= len(char_son):
        return char_fater_index - char_son_index+1
    return 0


if __name__ == "__main__":
    s1 = "ababctabcacbab"
    s2 = "abcac"
    print('发现下标为:{}'.format(index(s1,s2)))