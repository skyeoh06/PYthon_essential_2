# The IBAN Validator
# The standard says that validation requires the following steps (according to Wikipedia):

# (step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify the code to meet this requirement if you wish; note: you have to teach the code all the lengths used in Europe)
# (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
# (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;
# (step 4) Interpret the string as a decimal integer and compute the remainder of that number by modulo-dividing it by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.

# IBAN Validator.
# ask the user to enter the IBAN
iban = input("Enter IBAN, please: ")
# Remove the spaces
iban = iban.replace(' ','')
# the entered IBAN must consist of digits and letters only
if not iban.isalnum():
    # output the message
    print("You have entered invalid characters.")
# the IBAN mustn't be shorter than 15 characters 
elif len(iban) < 15:
    #  if it is shorter
    print("IBAN entered is too short.")
# the IBAN cannot be longer than 31 characters 
elif len(iban) > 31:
    # if it is longer
    print("IBAN entered is too long.")
# start the actual processing
else:
    # move the four initial characters to the number's end, and convert all letters to upper case
    iban = (iban[4:] + iban[0:4]).upper()
    # this is the variable used to complete the number, created by replacing the letters with digits
    iban2 = ''
    # iterate through the IBAN
    for ch in iban:
        #  if the character is a digit.
        if ch.isdigit():
            iban2 += ch
        else:
            # convert it into two digits 
            iban2 += str(10 + ord(ch) - ord('A'))
    # the converted form of the IBAN is ready – make an integer out of it
    iban = int(iban2)
    #If yes, then success
    if iban % 97 == 1:
        # If yes, then success
        print("IBAN entered is valid.")
    else:
        # the number is invalid
        print("IBAN entered is invalid.")
>>
Enter IBAN, please: 910292
IBAN entered is too short.
Enter IBAN, please: sdfahfkkn321320o3413knk4n31304i139
IBAN entered is too long.
Enter IBAN, please: de00001200121003123232
IBAN entered is invalid.
Enter IBAN, please: GB72 HBZU 7006 7212 1253 00
IBAN entered is valid.
