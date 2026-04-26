2. Automation (File Handling)

Use case: Read a file and count words

with open("sample.txt", "r") as f:
    text = f.read()

words = text.split()
print(len(words))

✅ Output: Total word count
