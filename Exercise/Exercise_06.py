def word_count(text):    
   
    list1=text.split()
    totalLen = 0
    for i in list1:
        totalLen += len(i)
 
   
    avgLen = totalLen/len(list1)
   
    return {'Word count': len(list1), 'unique_words': len(set(list1)),'average_word_length':f"{avgLen:1.2f}",'longest_word':max(list1)}
 
text1 = "This is a sample text to analyze It contains multiple sentences and some interesting vocabulary"
print(word_count(text1))