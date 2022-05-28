# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("story.txt", 'r') as d:
        filename = d.read()
        print(filename)
    
    return(filename)

read_file_content(filename)



from builtins import dict

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    words = text.split()
    count = dict() 

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    return count

print(count_words())



