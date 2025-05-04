#Finding if a words first letter is capitalized and exist between A-Z or not by ASCII value using chr() function
#ASCII value of A is 65 and Z is 90
def check_capitalized(word):
    a=ord(word[0])
    if a in range(65,91):
        print("True")
word= "Ali"
print(check_capitalized(word))