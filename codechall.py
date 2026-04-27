Coding Exercise: Decoding a Secret Message

In this exercise, you will write code to solve a problem. Your code must be in Python (preferred), JavaScript, TypeScript, Java, Kotlin, C#, C++, Go, Rust, Swift or Ruby—solutions in other languages will not be accepted! You can write your code using any IDE you want.

Problem

You are given a published Google Doc like this one that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

    The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

    The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

    Any positions in the grid that do not have a specified character should be filled with a space character.

    You can assume the document will always have the same format as the example document linked above.

For example, the simplified example document linked above draws out the letter 'F':

█▀▀▀
█▀▀ 
█   

Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

Specifications

    Your code must be written in Python (preferred), JavaScript, TypeScript, Java, Kotlin, C#, C++, Go, Rust, Swift or Ruby.

    You may use external libraries.

    You may write helper functions, but there should be one function that:

    1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND

    2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.

Please submit the complete code for your function:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
import requests
import re

def decode_secret_message(url: str) -> None:
    # Step 1: Fetch document content
    response = requests.get(url)
    text = response.text

    # Step 2: Parse lines assuming format: character x y
    # (adjust regex if format differs slightly)
    pattern = re.findall(r'(.+?)\s+(\d+)\s+(\d+)', text)

    points = []
    max_x = 0
    max_y = 0

    for char, x, y in pattern:
        x, y = int(x), int(y)
        points.append((char, x, y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Step 3: Create grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Step 4: Place characters
    for char, x, y in points:
        grid[y][x] = char

    # Step 5: Print grid (reverse y to ensure correct orientation if needed)
    for row in reversed(grid):
        print("".join(row))


Explain how your code works in 2-3+ complete sentences.
The function first downloads the Google Doc content using the provided URL and extracts all character coordinate entries using a regular expression. It then determines the maximum x and y values to construct a 2D grid filled with spaces. Each character is placed into its correct position in the grid based on its coordinates. Finally, the grid is printed row by row (reversing vertically if needed) to display the hidden uppercase letter message.
The function first downloads the Google Doc content using the provided URL and extracts all character coordinate entries using a regular expression. It then determines the maximum x and y values to construct a 2D grid filled with spaces. Each character is placed into its correct position in the grid based on its coordinates. Finally, the grid is printed row by row (reversing vertically if needed) to display the hidden uppercase letter message.

To verify that your code works, please run your function with this URL as its argument: https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub

===============================================================================

Coding assessment input data
Updated automatically every 5 minutes

The table below contains the input data needed to solve the coding assessment exercise.

x-coordinate
	

Character
	

y-coordinate

87
	

░
	

0

78
	

█
	

3

28
	

░
	

2

26
	

█
	

2

9
	

█
	

1

48
	

░
	

2

31
	

░
	

5

48
	

█
	

0

27
	

░
	

0

48
	

░
	

4

15
	

░
	

4

74
	

█
	

1

35
	

█
	

2

71
	

█
	

0

61
	

█
	

5

35
	

█
	

3

67
	

░
	

4

63
	

░
	

4

41
	

░
	

1

73
	

█
	

5

40
	

█
	

2

67
	

█
	

0

32
	

░
	

4

39
	

░
	

4

65
	

█
	

6

60
	

░
	

6

49
	

█
	

0

40
	

█
	

0

46
	

█
	

1

79
	

█
	

1

66
	

█
	

6

87
	

█
	

4

72
	

█
	

6

56
	

█
	

6

73
	

█
	

2

8
	

█
	

6

14
	

░
	

3

79
	

█
	

5

8
	

█
	

5

60
	

░
	

0

82
	

█
	

0

54
	

░
	

5

54
	

█
	

0

79
	

░
	

2

66
	

█
	

2

61
	

█
	

2

38
	

█
	

2

44
	

█
	

0

35
	

░
	

1

88
	

█
	

5

84
	

█
	

6

8
	

█
	

1

78
	

█
	

1

28
	

█
	

4

52
	

█
	

5

75
	

░
	

5

49
	

█
	

6

15
	

█
	

0

13
	

█
	

1

0
	

█
	

0

78
	

█
	

2

41
	

█
	

0

10
	

░
	

4

1
	

█
	

0

83
	

█
	

0

46
	

█
	

2

73
	

█
	

1

77
	

█
	

4

77
	

█
	

1

26
	

█
	

3

47
	

█
	

4

73
	

░
	

0

27
	

█
	

3

79
	

░
	

4

12
	

█
	

2

89
	

░
	

1

68
	

█
	

0

1
	

█
	

6

74
	

█
	

2

61
	

█
	

4

89
	

░
	

5

46
	

█
	

6

27
	

█
	

1

27
	

█
	

4

77
	

█
	

5

80
	

█
	

0

0
	

█
	

2

13
	

█
	

5

2
	

░
	

5

65
	

█
	

0

39
	

█
	

3

69
	

█
	

6

10
	

░
	

6

46
	

█
	

0

73
	

░
	

6

27
	

█
	

5

36
	

░
	

4

47
	

█
	

5

16
	

█
	

6

22
	

░
	

0

85
	

█
	

0

33
	

█
	

2

37
	

█
	

4

54
	

█
	

6

18
	

█
	

0

28
	

█
	

5

31
	

█
	

2

39
	

█
	

1

7
	

█
	

3

38
	

█
	

4

1
	

█
	

1

42
	

░
	

0

83
	

█
	

6

40
	

█
	

1

53
	

█
	

5

70
	

█
	

6

21
	

█
	

0

65
	

█
	

2

10
	

░
	

2

80
	

░
	

1

87
	

█
	

5

0
	

█
	

5

10
	

░
	

3

38
	

█
	

3

55
	

█
	

6

30
	

█
	

4

67
	

░
	

5

48
	

█
	

6

19
	

█
	

0

2
	

░
	

0

38
	

░
	

6

15
	

█
	

1

84
	

█
	

0

62
	

█
	

4

0
	

█
	

4

67
	

█
	

3

0
	

█
	

1

74
	

█
	

5

37
	

█
	

5

38
	

█
	

5

53
	

█
	

1

62
	

░
	

1

14
	

█
	

5

88
	

█
	

1

29
	

█
	

6

86
	

█
	

6

47
	

█
	

2

32
	

█
	

3

62
	

█
	

2

25
	

█
	

1

34
	

█
	

4

8
	

█
	

2

26
	

█
	

0

36
	

░
	

2

79
	

░
	

3

33
	

█
	

1

6
	

█
	

3

80
	

█
	

6

8
	

█
	

0

65
	

█
	

5

58
	

█
	

6

63
	

░
	

2

54
	

░
	

4

27
	

█
	

2

46
	

█
	

5

4
	

█
	

3

20
	

█
	

6

86
	

█
	

5

56
	

█
	

0

22
	

█
	

1

28
	

█
	

6

8
	

█
	

4

5
	

█
	

3

53
	

█
	

3

73
	

█
	

4

29
	

░
	

3

35
	

█
	

5

55
	

█
	

0

16
	

░
	

5

36
	

█
	

6

87
	

█
	

3

37
	

█
	

6

80
	

░
	

5

61
	

█
	

3

75
	

░
	

4

34
	

█
	

3

17
	

█
	

0

70
	

█
	

3

30
	

█
	

5

59
	

█
	

6

21
	

█
	

5

28
	

█
	

3

21
	

█
	

1

19
	

█
	

6

52
	

█
	

4

65
	

█
	

4

45
	

█
	

0

23
	

░
	

5

85
	

█
	

6

1
	

█
	

2

66
	

█
	

3

86
	

█
	

1

59
	

█
	

0

52
	

█
	

6

63
	

░
	

3

22
	

░
	

6

50
	

░
	

6

69
	

█
	

0

66
	

█
	

0

88
	

█
	

4

18
	

█
	

6

31
	

█
	

3

46
	

█
	

3

10
	

░
	

5

78
	

█
	

5

66
	

█
	

1

68
	

█
	

3

17
	

█
	

6

73
	

░
	

3

89
	

░
	

2

23
	

░
	

1

89
	

░
	

3

16
	

░
	

1

36
	

░
	

3

47
	

█
	

1

58
	

█
	

0

54
	

░
	

1

66
	

█
	

4

71
	

█
	

6

35
	

█
	

4

9
	

█
	

6

67
	

░
	

1

10
	

░
	

0

32
	

█
	

2

16
	

█
	

0

13
	

█
	

3

28
	

░
	

1

50
	

░
	

0

21
	

█
	

6

9
	

█
	

5

0
	

█
	

3

68
	

█
	

6

81
	

█
	

6

0
	

█
	

6

72
	

█
	

0

52
	

█
	

3

22
	

█
	

5

62
	

░
	

5

48
	

░
	

3

74
	

█
	

4

45
	

█
	

6

87
	

█
	

1

72
	

█
	

3

47
	

█
	

0

54
	

░
	

3

34
	

█
	

1

53
	

█
	

4

65
	

█
	

1

33
	

░
	

3

20
	

█
	

0

39
	

░
	

5

36
	

█
	

5

9
	

█
	

0

57
	

█
	

6

57
	

█
	

0

46
	

█
	

4

75
	

░
	

2

15
	

░
	

2

81
	

█
	

0

77
	

█
	

2

60
	

█
	

1

78
	

█
	

4

77
	

█
	

3

44
	

█
	

6

1
	

█
	

4

14
	

█
	

2

9
	

█
	

3

14
	

█
	

1

13
	

█
	

4

48
	

░
	

1

34
	

█
	

2

87
	

░
	

6

69
	

█
	

3

75
	

░
	

1

29
	

█
	

5

3
	

█
	

3

54
	

░
	

2

60
	

█
	

5

15
	

█
	

6

79
	

█
	

6

13
	

█
	

2

87
	

█
	

2

52
	

█
	

1

2
	

░
	

1

89
	

░
	

4

65
	

█
	

3

39
	

█
	

2

29
	

░
	

4

2
	

░
	

2

26
	

█
	

1

2
	

█
	

3

8
	

█
	

3

53
	

█
	

2

1
	

█
	

3

66
	

█
	

5

30
	

░
	

6

9
	

█
	

2

71
	

█
	

3

88
	

█
	

2

10
	

░
	

1

53
	

█
	

6

2
	

░
	

4

53
	

█
	

0

47
	

█
	

3

62
	

█
	

3

15
	

█
	

5

52
	

█
	

2

25
	

█
	

0

88
	

█
	

3

47
	

█
	

6

67
	

░
	

2

86
	

█
	

0

2
	

░
	

6

32
	

█
	

1

1
	

█
	

5

40
	

░
	

3

14
	

█
	

4

61
	

█
	

1

67
	

█
	

6

31
	

█
	

4

48
	

░
	

5

70
	

█
	

0

79
	

█
	

0

52
	

█
	

0

39
	

█
	

0

82
	

█
	

6

12
	

█
	

3

9
	

█
	

4

41
	

░
	

2

12
	

█
	

4
