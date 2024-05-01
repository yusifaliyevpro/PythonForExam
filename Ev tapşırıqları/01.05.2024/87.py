# Klaviaturadan daxil edilmiş gün dəyərini "il", "ay", "gün" baxımından çap edən proqram yazın

gün = float(input("Vaxtı gün olaraq daxil edin: "))

il = gün//365
ay = (gün-il*365)//30
gün = (gün-il*365) % 30

print(f"{il} il, {ay} ay, {gün} gün")

# Input: Vaxtı gün olaraq daxil edin: 399
# Output: 1.0 il, 1.0 ay, 4.0 gün
