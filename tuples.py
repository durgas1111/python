Task
Given an integer, , and space-separated integers as input, create a tuple, , of those integers. Then compute and print the result of hash(t)
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in tuple .

Output Format

Print the result of  hash(t).

Sample Input 0

2
1 2

Sample Output 0

3713081631934410656

Language
Pypy 3
1
2
3
Line: 3 Col: 45
Test against custom input

======================================================
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()
=======================================================

You need to:


Read the number of elements (not really needed for logic)


Read space-separated integers


Convert them into a tuple


Print the hash of that tuple



✅ Python Code
n = int(input())t = tuple(map(int, input().split()))print(hash(t))

🔍 Explanation


map(int, input().split()) → converts input to integers


tuple(...) → creates a tuple


hash(t) → computes the hash value



✅ Example
Input:
21 2
Output:
3713081631934410656

That’s all—simple tuple creation + built-in hash() function.Ads do not influence the answers you get from ChatGPT. Your chats stay private. Learn about ads and personalization

=========================================================================
