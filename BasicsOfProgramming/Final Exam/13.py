N = 7

x = [((-1) ** k) * k for k in range(N)]
x.sort(reverse=True)
print(x)  # [6, 4, 2, 0, -1, -3, -5]

x.sort(key=lambda x: abs(x), reverse=True)
print(x)  # [6, -5, 4, -3, 2, -1, 0]

# Bu sualda sort funksiyasına key parametri vermişik çünki
# istəmirik ki sıralamada mənfilər nəzərə alınsın sırf
# modul qiymətinə görə sıralansın, və sort olduqdan
# sonrada list tərsinə çevrilsin deyə reverse=True parametri vermişik
