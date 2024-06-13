
#The Numbers Processor
The third program shows a simple method allowing you to input a line filled with numbers, and to process them easily. Note: the routine input() function, combined together with the int() or float() functions, is unsuitable for this purpose.
#ask the user to enter a line filled with any number of numbers (the numbers can be floats)
line = input("Enter a line of numbers - separate them with spaces: ")

if line !="":
    #split the line receiving a list of substrings
    strings = line.split()
    #initiate the total sum to zero
    total = 0
    try:
        #iterate through the list
        for substr in strings:
            #and try to convert all its elements into float numbers; if it works, increase the sum
            total += float(substr)
        #print the sum
        print("The total is:", total)
    
    #the program ends here in the case of an error   
    except:
        #print a diagnostic message showing the user the reason for the failure
        print(substr, "is not a number.")
else:
    print("Error empty input.")

>> 
Enter a line of numbers - separate them with spaces: 5 6 7
The total is: 18.0
Enter a line of numbers - separate them with spaces: 1 a 3
a is not a number.
Enter a line of numbers - separate them with spaces: 

Error empty input.
