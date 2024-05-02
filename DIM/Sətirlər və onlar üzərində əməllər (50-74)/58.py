a = input("Cümlə daxil edin: ").split()
s = 0

for i in a:
    s += 1
    print(f"Daxil edilmiş cümlənin {s} saylı sözündə {
          i.count("w")} sayda w simvolu mövcuddur. ")

# Input: windows view www

# Output:
# Daxil edilmiş cümlənin 1 saylı sözündə 2 sayda w simvolu mövcuddur.
# Daxil edilmiş cümlənin 2 saylı sözündə 1 sayda w simvolu mövcuddur.
# Daxil edilmiş cümlənin 3 saylı sözündə 3 sayda w simvolu mövcuddur.
