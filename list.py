Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer .
    append e: Insert integer at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.

Initialize your list and read in the value of followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example

N=4
append 1
append 2
insert 13

print



  append1  : Append to the list, .
  qppend 2  : Append to the list, .
  insert 13 : Insert at index , .
   print  : Print the array.
    
Output:

[1, 3, 2]

Input Format

The first line contains an integer, , denoting the number of commands.
Each line of the subsequent lines contains one of the commands described above.

Constraints

    The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

================================

if __name__ == '__main__':
    N = int(input())


================================
Query:
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()
===============================================

Output:
Congratulations!

You have passed the sample test cases. Click the submit button to run your code against all the test cases.
Input (stdin)

    12

    insert 0 5

    insert 1 10

    insert 0 6

    print

    remove 6

    append 9

    append 1

    sort

    print

    pop

    reverse

    print

Your Output (stdout)

    [6, 5, 10]

    [1, 5, 9, 10]

    [9, 5, 1]

Expected Output

    [6, 5, 10]

    [1, 5, 9, 10]

    [9, 5, 1]

==================================


Python
You have earned 10.00 points!
You are now 11 points away from the 2nd star for your python badge.
69%59/70
Congratulations
You solved this challenge. Would you like to challenge your friends?
Compiler Message

Success

Input (stdin)

    12

    insert 0 5

    insert 1 10

    insert 0 6

    print

    remove 6

    append 9

    append 1

    sort

    print

    pop

    reverse

    print

Expected Output

    [6, 5, 10]

    [1, 5, 9, 10]

    [9, 5, 1]

    BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy
