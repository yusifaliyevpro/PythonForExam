# 20. Valid Parentheses

s = input("Enter string: ")
t = ""
while s != t:
    t = s
    s = s.replace("{}", "").replace("[]", "").replace("()", "")

print("true" if s == "" else "false")
