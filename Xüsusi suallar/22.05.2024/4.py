# 4. Verilmiş n ədədinin polindrom olub-olmadığını yoxlayan proqram yazın.

n = input("Ədəd daxil edin: ")

if n[::-1] == n:
    print("Polindromdur!")
else:
    print("Polindrom deyil!")
