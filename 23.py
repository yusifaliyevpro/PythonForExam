# a = input('Malların adlarını vergül işarələri ilə ayıraraq daxil edin. (Nümunə: alma,pendir,azov ): ').split(",")
# b = []

# for i in a:
#     b.append(i)
# print(b)

b = []
for i in range(1, 8):
    a = int(input(
        f"Həftənin {i} saylı günü sifariş olunan malların sayını daxil edin: "))
    b.append(a)
print(b)
