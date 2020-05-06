# Given two strings, write an algorithm that will compare and return true or false
#  #based on whether or not those two strings are the same, ignoring casing
#Example: pYThOn and Python would return true because it's the same word
#with different casing

// HINT: Javascript has .toLowerCase() function built in.
function caseInsensitiveStringCompare(string1, string2) {
    

}
def caseInsensitiveStringCompare(string1, string2):
    string1 = string1.lower() 
    string2 = string2.lower()
    if string1 == string2:
        return True
    else:
        return False

print(caseInsensitiveStringCompare("pYThon","python"))        

#// Write a function that takes a string, and returns a reversed version
#// of that string. Example: an input of "hello world" would return 
#// "dlrow olleh"
#function reverse(string) {

#}
def reverse(string):
    new_string = ""
    for x in range(len(string)-1,-1,-1):
        new_string += string[x]
    return new_string

print(reverse("freddy"))



# // Write a function that takes a string, and returns an acronym.
# // Example: "please excuse my dear aunt sally" would return "pemdas"

# // HINT: Make note of how you would determine if a letter is the first in a word
# function acronyms(string) {

# }

def acronyms(string):
    new_string = ""
    new_string += string[0]
    for x in range(len(string)):
        if string[x] == " "
            new_string += string[x] + 1