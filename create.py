import os

path = "midterm"

tasks = [
    "Basic Arithmetic Calculator",
    "Odd or Even",
    "Square of a Number",
    "Area of a Circle",
    "List of Multiples",
    "Sum of Digits",
    "Factorial of a Number",
    "Reverse a String",
    "Palindrome Checker",
    "Count Vowels and Consonants",
    "Fibonacci Sequence",
    "Simple Interest Calculator",
    "Temperature Converter",
    "Prime Number Checker",
    "Binary to Decimal Converter",
    "Random Password Generator",
    "Longest Common Prefix",
    "Remove Duplicates from Sorted Array",
    "Word Count",
    "Character Frequency in a String",
    "List Sorting",
    "Finding Duplicates",
    "Roman to Integer",
    "Two Sum",
    "Generate Parentheses",
    "Rock, Paper, Scissors Game",
    "Basic To-Do List",
    "Largest and Smallest Number in a List",
    "Simple Quiz",
    "Pascal's Triangle",
]


for i in range(1, len(tasks) + 1):
    a = open(os.path.join(path, f"{i}.py"), "w", encoding="utf-8")
    a.write(f"# {i}. {tasks[i-1]}")
    a.close()

# for i in range(1, 26):
#     os.remove(os.path.join(path, f"{i}.py"))
