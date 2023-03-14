def verify(number):
    # write your code here so that it verifies the card number
    #determine whether the card number is valid
    digitIndex = []
    count = 0
    digitsCount = 0
    wholeNumber = []
    for digit in number:
        if digit != "-":
            wholeNumber.insert(count, int(digit))
            digitIndex.insert(count, digit)
            count += 1
            digitsCount += int(digit)
            
            continue
    total = int(digitIndex[0] + digitIndex[1]) + int(digitIndex[10] + digitIndex[11])
    if wholeNumber[0] == 4:
        rule1 = "pass"
    else:
        rule1 = "return 1"
        return rule1
    if wholeNumber[3] > wholeNumber[4]:
        pass
    if digitsCount//4 == 0:
        rule3 = "pass rules 1-2"
    else:
        rule3 = "return 3"
        return rule3
    if total == 100:
        rule4 = "pass rules 1-3"
        output = rule4
        return output
    else:
        rule4 = "return 4"
        output = rule4
        return output
            
        
    
  
  # be sure to indent your code!
  
    return True # modify this line as needed

ccNumber = "5000-0000-0000" # change this as you test your function
output = verify(ccNumber) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
