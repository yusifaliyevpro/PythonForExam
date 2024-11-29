a = input("Mətn daxil edin: ")

# a)
print('iti')

# b)
print(a.count("ə"))

# c)
a = a.split(" ")
s = ""
for i in a:
    s += i[0]*len(i)
    s += " "
print(s)
