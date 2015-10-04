from string import maketrans

"""
You will make encryption and decryption methods for your team.
Your decryption must perfectly reverse your encryption.
Example code is included and you can run this python program at any time wihout
worrying about other teams.

All input will be strings so you should manipulate based on standard ASCII characters.



Sample transformations include-

///TRANSLATION
#Translate from these characters
in_trans = "abcd"
#Translate to these characters 
out_trans = "dbca"
#Create translation matrix
trans_matrix = maketrans(in_trans, out_trans)
#Translate text
encrypted_text = plain_text.translate(trans_matrix)


///CASE SWAP
text.swapcase() --swaps the casing (upper-lower) for strings.


///CENTER PAD
text.center(width, fillchar) --width is number of padding characters to either side
                             --fillchar sets which char to use for pad (space is default)
                             
//STRIP END
text.rstrip([chars]) --chars is characters to be stripped (space is default)


//STRIP FRONT
text.lstrip([chars]) --chars is characters to be stripped (space is default)

//REVERSE
text = ''.join(reversed(text)) --shows functionality of join as well


Feel free to Google for your own.
"""





"""
The encrypt method takes in a string and returns an encrypted verions of the string
"""
def encrypt(text):

    #Translate from these characters
    in_trans = "aeiou"
    #Translate to these characters 
    out_trans = "uoeia"
    #Create translation matrix
    trans_matrix = maketrans(in_trans, out_trans)
    #Translate the plain text
    text = text.translate(trans_matrix)
    
    #Now reverse the whole string
    text = ''.join(reversed(text))
    
    return text

"""
The decrypt method takes in a string and returns a decrypted version of the string
"""
def decrypt(text):
    #Reverse the encrypted string
    text = ''.join(reversed(text))
    
    #Translate from these characters
    in_trans = "uoeia"
    #Translate to these characters 
    out_trans = "aeiou"
    #Create translation matrix
    trans_matrix = maketrans(in_trans, out_trans)
    #Translate the encrypted text
    text = text.translate(trans_matrix)
    
    return text




"""
This is the test code for you encryption and decryption. Feel free to change 
the test sentence as you would like.
"""
if __name__ == "__main__":
    test_input = ("This is a test sentence for Team 2.")
    print "PLAIN TEXT: " + test_input
    temp_text = encrypt(test_input)
    print "ENCRYPTED: " + temp_text
    output = decrypt(temp_text)
    print "DECRYPTED: " + output