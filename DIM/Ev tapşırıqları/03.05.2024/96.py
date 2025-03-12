# Ilk həddi b olan və silsilə vuruğu a olan həndəsi silsilənin n-ci həddinin hesablanması üçün proqram yazın.
# Daxil etdiyimiz a və b ədədləri sıfırdan fərqlidir

b = int(input("Ilk həddi: "))
a = int(input("Silsilə Vuruğu: "))
n = int(input("Neçənci həddi tapmaq istəyirsiz?: "))

print(b*a**(n-1))

# Input:
# Ilk həddi: 2
# Silsilə Vuruğu: 2
# Neçənci həddi tapmaq istəyirsiz?: 5

# Output: 32
