def verify(number):
    # write your code here so that it verifies the card number
    #determine whether the card number is valid
    digitIndex = []
    count = 0
    for digit in number:
        if digit == "-":
            continue
        digitIndex.insert(count,digit)
        count += 1
    
    print(type(digitIndex), digitIndex)
  
  # be sure to indent your code!
  
    return True # modify this line as needed

ccNumber = "5000-0000-0000" # change this as you test your function
output = verify(ccNumber) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
