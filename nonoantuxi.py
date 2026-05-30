from random import randint

player = input("Nhập lựa chọn của bạn (dam/keo/bao): ")
computer = randint(0, 2)

# Chuyển giá trị random của máy tính thành string
if computer == 0:
    computer = "dam"
elif computer == 1:
    computer = "keo"
else:
    computer = "bao"

# In ra lựa chọn của máy tính
print(f"Máy tính chọn: {computer}")

# So sánh và quyết định kết quả
if player == "keo":
    if computer == "keo":
        print("Hòa")
    elif computer == "dam":
        print("Máy tính thắng")
    elif computer == "bao":
        print("Bạn thắng")

elif player == "dam":
    if computer == "keo":
        print("Bạn thắng")
    elif computer == "dam":
        print("Hòa")
    elif computer == "bao":
        print("Máy tính thắng")

elif player == "bao":
    if computer == "keo":
        print("Máy tính thắng")
    elif computer == "dam":
        print("Bạn thắng")
    elif computer == "bao":
        print("Hòa")

else:
    print("Lựa chọn không hợp lệ. Vui lòng nhập 'dam', 'keo', hoặc 'bao'.")
