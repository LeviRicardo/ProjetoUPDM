o = open("UPDM frases.txt", "r", encoding = "utf8")

frases = o.readlines()

o.close()

counter = 0
for i in frases:
	counter += 1
	i = i.strip()
	if len(i) > 280:
		print(f"A linha {counter} possui {len(i)} caracteres")













