def verify(number):
    # write your code here so that it verifies the card number
    #determine whether the card number is valid
    digitIndex = []
    count = 0
    wholeNumber = []
    for digit in number:
        if digit == "-":
            continue
        digitIndex.insert(count, int(digit))
        count += 1
        digit1 = int(digit)
        if digit1 == digitIndex[0]:
            print(f'yes, {digit1}')
        
        """wholeNumber = int(digit)
        digit1 = int(digit)
        if digit1 == wholeNumber[0]:
            print(digit1)
        
        
        digitIndex.insert(count,int(digit))
        count += 1
    count1 = 0
    for digit in digitIndex:
        print(digitIndex[count1])
        if digit == digitIndex[count1]:
            
        
        
            print(type(digit), digit)"""
    
  
  # be sure to indent your code!
  
    return True # modify this line as needed

ccNumber = "5000-0000-0000" # change this as you test your function
output = verify(ccNumber) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
