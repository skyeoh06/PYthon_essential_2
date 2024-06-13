# 1.1
# The Caesar Cipher: encrypting a message
# We've written it using the following assumptions:

# it accepts Latin letters only (note: the Romans used neither whitespaces nor digits)
# all letters of the message are in upper case (note: the Romans knew only capitals)

# Caesar cipher.
#ask the user to enter the open (unencrypted), one-line message
text = input("Enter your message: ")
#prepare a string for an encrypted message (empty for now)
cipher = ''
#start the iteration through the message
for char in text:
    #if the current character is not alphabetic
    if not char.isalpha():
        #ignore it
        continue
    #convert the letter to upper-case
    char = char.upper()
    #get the code of the letter and increment it by one
    code = ord(char) + 1
    #if the resulting code has "left" the Latin alphabet
    if code > ord('Z'):
        #change it to the A code
        code = ord('A')
    #append the received character to the end of the encrypted message
    cipher += chr(code)
#print the cipher
print(cipher)

>>
Enter your message: test
UFTU
Enter your message: ave caesar
BWFDBFTBS

#1.2
#The Caesar Cipher: decrypting a message
# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
>>
Enter your cryptogram: uftu
TEST
Enter your cryptogram: BWFDBTBS
AVECASAR
