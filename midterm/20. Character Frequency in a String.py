# 20. Character Frequency in a String

a = input("Enter the text: ")
chars = []
freq = []
for i in a:
    if not i in chars:
        chars.append(i)
        freq.append(1)
    else:
        freq[chars.index(i)] += 1

for i in range(len(chars)):
    print(f"{chars[i]}: {freq[i]/len(a)*100}%")
