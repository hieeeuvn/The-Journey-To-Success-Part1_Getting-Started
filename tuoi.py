age = input("Bạn năm nay bao nhiêu tuổi? :"

if age < 10:
	print("Bạn là thằng con nít")
elif age < 18:
	print("Bạn là trẻ trâu")
	if age >= 5 and age <= 17:
		print("Bạn là trẻ nghé")
elif age >= 18 and age <= 50:
	print("Bạn là người lớn")
else:
	print("Bạn là người già")
