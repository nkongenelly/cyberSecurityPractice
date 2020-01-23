alphabetsString = "abcdefghijklmnopqrstuvwxyz"
def split(alphabetsString):
    return list(alphabetsString)
alphabets = split(alphabetsString)
print (alphabetsString.find("m"))
OutputString = []
inputKey = input("Input the caesar Cipher key to use:")
caesarKey = inputKey

#Encryption or decryption?
choice = input("\n Please choose and press enter:\n 1).Type 1 for Encryption \n 2). Type 2 for decryption? ")

#ask for input
message = input("Input message to encyption\n") 
cipherKey = 3
print ("\n We are going to encode the message: " + message)

#split the string into characters
def split1(characterSet): 
    return list(characterSet) 
characters = split(message.lower())
message = message.lower()
print (characters)
#confirm string is not empty
if len(message) > 0:
    #shift characters according to key and skip spaces
    # print(len(message))


    i =0
    while i < len(message):
        if (message[i]) != ' ':
            x = message[i]
            #print (message[i])
            #print ("\n")
            #handle encrypt
            if choice == "1":
                y = alphabetsString.find(x) + int(caesarKey)
                #print (y)
                m = alphabetsString[y%26]
                OutputString.append(m)
                # print (OutputString)
                #print (m)
                i+=1
            else:
                y = alphabetsString.find(x) - int(caesarKey)
                #print (y)
                m = alphabetsString[y%26]
                OutputString.append(m)
                # print (OutputString)
                #print (m)
                i+=1
        else:
            OutputString.append(' ')
            i+=1
            
    # Python program to convert a list 
    # of character         
    def convert(s): 

    # initialization of string to "" 
        new = "" 
    
        # traverse in the string  
        for x in s: 
            new += x  
    
        # return string  
        return new 
    s = OutputString
    if choice == "1":
        print ("ciphertext = "+convert(s))
    else:
        print ("plaintext = "+convert(s))
else:
    message = input("\n Please input atleast one character")






