def file_list(filename):
    """remove the whitespace for every word and put the words in a list"""
    txt_open = open(filename)
    txt_list = txt_open.readlines()
    new_txt_list = []

    for word in txt_list:
        new_txt_list.append(word.rstrip())
    
    return new_txt_list

def five_letter(new_txt_list):
    """find all the words that contains five letters and convert those words into lowercase"""
    five_list = []

    for word in new_txt_list:
        if len(word) == 5:
            five_list.append(word.lower())
    
    return five_list

def frequency(five_list):
    """find the frequency of every letter, and put them in a dictionary"""
    word_frequency = dict()

    for word in five_list:
        for i in range(5):
            if word[i] in word_frequency:
                word_frequency[word[i]] = word_frequency[word[i]] + 1
            else:
                word_frequency[word[i]] = 1
    
    return word_frequency

def top_five(word_frequency):
    """find the five letters with the highest counts and put them in a list with descending order"""
    highest = 0
    all_numbers = []
    top_five_list = []

    #put all the numbers in a list with descending order
    for key in word_frequency:
        all_numbers.append(word_frequency[key])
    all_numbers.sort(reverse=True) 

    top_five_list = all_numbers[0:5]

    #find the five correspoding letters and put them in a list with descending order
    final_alph_list = [0, 0, 0, 0, 0]
    for key in word_frequency:
        if word_frequency[key] in top_five_list:
            ordernum = top_five_list.index(word_frequency[key])
            final_alph_list[ordernum] = key
    
    return final_alph_list

print(top_five(frequency(five_letter(file_list("words.txt")))))


