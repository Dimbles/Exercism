def is_pangram(sentence):
    List = []
    #creating a list of 26 characters with each entry false
    for i in range(26):
        List.append(False)
    
    #returning false if sentence is empty
    if sentence == "":
        return False
    #converting the sentence to lowercase
    for c in sentence.lower():
        if not c == "" and ord(c) -ord('a') < 26 and ord(c) -ord('a') >= 0:
            
            #make the list index corresponding to the unicode character true
            List[ord(c) -ord('a')] = True
    
    #check if any of the list indexs are still false        
    for ch in List:
        if ch == False:
            return False
    
    return True

