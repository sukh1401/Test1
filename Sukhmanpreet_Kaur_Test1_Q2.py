s_input = input("Enter a string : ")

def findLength(s_input):
    counter = 0
    for i in s_input:
        counter += 1
    return counter
print(findLength(s_input))
