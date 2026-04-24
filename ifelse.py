Task
Given an integer, , perform the following conditional actions:

    If is odd, print Weird
    If is even and in the inclusive range of to , print Not Weird
    If is even and in the inclusive range of to , print Weird
    If is even and greater than , print Not Weird

Input Format

A single line containing a positive integer, .

Constraints
1<_n<_100

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3

Sample Output 0

Weird

Explanation 0
n=3

is odd and odd numbers are weird, so print Weird.

Sample Input 1

24

Sample Output 1

Not Weird

Explanation 1
n=24
n>20

and is even, so it is not weird.

========================================

Task
Given an integer n, perform the following:


If n is odd, print Weird


If n is even and in the range 2 to 5, print Not Weird


If n is even and in the range 6 to 20, print Weird


If n is even and greater than 20, print Not Weird



Input Format


A single integer n


Constraint:


1 < n < 100



Python Code
n = int(input())if n % 2 != 0:    
print("Weird")else:    
if 2 <= n <= 5:        
print("Not Weird")    
elif 6 <= n <= 20:       
 print("Weird")    
else:       
 print("Not Weird")

Sample Input 0
3
Sample Output 0
Weird
Explanation


n = 3 → odd → Weird



Sample Input 1
24
Sample Output 1
Not Weird
Explanation


n = 24


24 is even


24 is greater than 20
→ So output is Not Weird



That’s the full problem, logic, code, and examples all together.
