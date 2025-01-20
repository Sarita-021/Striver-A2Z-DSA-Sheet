def rev(n, temp): 
 
    # base case 
    if (n == 0): 
        return temp; 
 
    # stores the reverse of a number 
    temp = (temp * 10) + (n % 10); 
 
    return rev(n // 10, temp); 
 
# Driver Code 
num = 121; 
temp = rev(num, 0); 
 
if (temp == num): 
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
