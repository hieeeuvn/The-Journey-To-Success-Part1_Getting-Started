age = 100000

if age < 10:
	print("con nít")
elif age < 18:
	print("trẻ trâu")
	if age >= 5 and age <= 17:
		print("trẻ nghé")
elif age >= 18 and age <= 50:
	print("Người lớn")
else:
	print("người già")