def rev(sentence):

    split_result = sentence.split()
    split_result.reverse()
    print (" ".join(split_result))
  
sen = input()
rev(sen)