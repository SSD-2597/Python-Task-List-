#Q1. Find the nth term in an array
# Find the missing number in an array.
# Let us consider the list containing n distinct numbers taken from 0,1,2,_ _ _,n but one number is missing.
# Write the function to find the missing number.

N = 5
A = [0,1,2,4]
Output : 3




A = [0,1,2,6,8,7,4,3]
n = 9

def Missing_Number(A,n):
    for i in range(0,n+1):
        if i not in A:
            return i
print(Missing_Number(A,n))



# Valid Parentheses Checker
# Q2.Write the function to check whether the given string containing only (),[],{} is balanced.
def is_Valid(s):
    stack = []
    lookup = {'(' : ')' , '['  : ']' , '{' : '}'}
    stk = []
    for brack in str:
        if brack in lookup:
            str.append(brack)
        else:
            if(not stk or lookup[stk.pop()] != brack):
                return False
    return not stk
print(is_Valid(str))



# Q2.Valid Parentheses Checker

string = input("Enter the string containning only (),{},[] : ")
stack = []
i = 0
balanced = True
while i < len(string):
    ch = string[i]
# If the stack is containning only open brackets
    if ch == '(' or ch == '{' or ch == '[':
     stack.append(ch)
# If the stack is containing only closing brackets
    elif ch == ')' or ch == '}' or ch == ']':
     if len(stack) == 0:
       balanced = False
       break
     top = stack.pop()
     if (ch == ')' and top != '(') or  (ch == '}' and top != '{')  or  (ch == ']'  and  top != '[') :
       balanced = False
       break
    i+=1
 
 # Finally, string is balanced and stack is empty
if balanced and len(stack) == 0:
      print("String is Balanced")
else:
      print("String is not Balanced")




