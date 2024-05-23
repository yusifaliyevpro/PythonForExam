# 19. İstifadəçidən bir sıyahı (list) və bir rəqəm daxil etməsini istəyin və bu rəqəmi sıyahının içində axtarın.

n = int(input("Ədəd daxil edin: "))
b = input("Yoxlamaq istədiyiniz ədədi daxil edin: ")
a = []

for i in range(n):
    a.append(input(f"{i+1} saylı elementi daxil edin: "))

if b in a:
    print(f"b bu siyahının {a.index(b)+1}-ci elementidir")
