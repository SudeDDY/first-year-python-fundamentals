class ArrayStack:                     # created stack adt
    def __init__(self):
        self._data = []               # stack is created by using "list"
    def __len__(self):
        return len(self._data)        # returns the lenght
    def push(self, e):
        self._data.append(e)          # push method, inserts to top (end of the list)
    def pop(self):
        return self._data.pop()       # pop method, removes from top (end of the list, deletes last element)
    def is_empty(self):
        return len(self._data) == 0   # checks if it is empty or not
            
s = ArrayStack()
word = input("Enter a word: ")        # takes the word 
reversed = ""                         # creates an empty string
for w in word:
    s.push(w)                         # all letters pushed into new stack
while not s.is_empty():               # if not empty, pops from "word" and pushes into "reversed"
    reversed += s.pop()               # because of system of stack, the word created by reversing
if word == reversed:
    print(f"{word} is a palindrome")  # if the original one and the second versions are same, it is palindrome
else:                                 # if they are not same, then it is not palindrome
    print(f"{word} is NOT a palindrome")

print(f"Your word: {word}, Reversed: {reversed}")