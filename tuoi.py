age = input("Bạn năm nay bao nhiêu tuổi? :")

if int(age) < 10:
	print("Bạn là thằng con nít")
elif int(age) < 18:
	print("Bạn là trẻ trâu")
	if int(age) >= 5 and int(age) <= 17:
		print("Bạn là trẻ nghé")
elif int(age) >= 18 and int(age) <= 50:
	print("Bạn là người lớn")
else:
	print("Bạn là người già")
