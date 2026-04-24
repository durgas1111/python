Task
The provided code stub reads an integer, , from STDIN. For all non-negative 
integers i<n , print  i^2.

Example
n=3

The list of non-negative integers that are less than is . Print the square of each number on a separate line.

0
1
4

Input Format

The first and only line contains the integer, .

Constraints
1<_n<_20

Output Format

Print lines, one corresponding to each .

Sample Input 0

5

Sample Output 0

0
1
4
9
16

==================

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)


==============================






Congratulations!

You have passed the sample test cases. Click the submit button to run your code against all the test cases.
Input (stdin)

    5

Your Output (stdout)

    0

    1

    4

    9

    16

Expected Output

    0

    1

    4

    9

    16
