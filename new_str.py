def new_str(phrases):
    dict = {}
    
    for word in phrases:
        word = word.split()
        match = word.pop()
        dict[match] = word 
        
    result_lst = []
    
    for word in phrases:
        word = word.split()
        for key, value in dict.items():
            if word[0] == key:
                new_phrase = value + word
                new_phrase = " ".join(new_phrase)
                result_lst.append(new_phrase)
    
    return result_lst
