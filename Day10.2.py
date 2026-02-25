#WAP to find the longest word in a sentence

sentence = input("Enter a Sentence: ")
word = sentence.split()
longest = ""
for word in word:
    if len(word) > len(longest):
        longest = word
    print("Longest Number is: ", longest)
    print("len", len(longest))