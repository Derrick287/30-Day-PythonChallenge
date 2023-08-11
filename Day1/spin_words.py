def spin_words(sentence):
    #   Convert the sentence into a list called 'words' using .split()
    #   Reverse each word in word whose len()>5
    #   Join the words in a list words back into a sentence using .join()
    #   Return the joined reversed sentence
    
    words = sentence.split()    
    reversed_words = [word if len(word)<5 else word[::-1] for word in words] 
    reversed_sentence = " ".join(reversed_words)
    
    return reversed_sentence