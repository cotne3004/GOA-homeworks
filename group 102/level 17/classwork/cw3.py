# 3) შექმენი ცარიელი სეტი და add გამოყენებით დაამატე 3 რიცხვი და მერე გადააქციე tuple-ად და გამოიტანე იმ 
# tuple-დან გამოიტანე უდიდესი და უმცირესი რიცხვი და ასევე გამოიტანე მათი ჯამი.

sett = set()

sett.add(13)
sett.add(30)
sett.add(4)

tup_set = tuple(sett)

print(min(tup_set))
print(max(tup_set))
print(sum(tup_set))