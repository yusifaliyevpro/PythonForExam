b1 = int(input("Birinci həddi daxil edin: "))
q = int(input("Silsilə vuruğunu daxil edin: "))
n = int(input("Neçənci həddə qədər olan həddlər cəmlənsin?: "))

s = b1*(1-q**n)/(1-q)
print(s)
