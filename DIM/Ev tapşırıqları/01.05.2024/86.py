# Klaviaturadan daxil edilmiş saniyə dəyərini "saat", "dəqiqə", "saniyə" baxımından çap edən proqram yazın

san = float(input("Vaxtı saniyə olaraq daxil edin: "))

saat = san//3600
deq = (san-saat*3600)//60
san = (san-saat*3600) % 60

print(f"{saat} saat, {deq} dəqiqə, {san} saniyə")

# Input: Vaxtı saniyə olaraq daxil edin: 3725.5
# Output: 1.0 saat, 2.0 dəqiqə, 5.5 saniyə
