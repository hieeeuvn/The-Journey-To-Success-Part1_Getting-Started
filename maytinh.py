human = input("Tôi là máy tính, tôi có thể giải mọi bài toán. Hôm nay, bạn muốn tính phép tính nào (ghi theo mẫu sau: cong/tru/nhan/chia)(nếu bạn cố ghi a/b là 1 chữ, nó sẽ không hoạt động) : ")

if human == "nhan":
    print("nhập số a")
    a = int(input())
    print("nhập số b")
    b = int(input())
    print("kết quả là: " + str(a * b))

elif human == "cong":
    print("nhập số a")
    a = int(input())
    print("nhập số b")
    b = int(input())
    print("kết quả là: " + str(a + b))

elif human == "tru":
    print("nhập số a")
    a = int(input())
    print("nhập số b")
    b = int(input())
    print("kết quả là: " + str(a - b))

elif human == "chia":
    print("nhập số a")
    a = int(input())
    print("nhập số b")
    b = int(input())
    if b == 0:
        print("Lỗi: Không thể chia cho 0")
    else:
        print("kết quả là: " + str(a / b))

elif human == "fuck u":
    print("fuck u, too")  # easter egg :))

elif human == "Hiếu có đẹp zai không":
    print("vì anh ấy là người tạo ra tôi, nên anh ấy rất đẹp trai")  # easter egg :))

else:
    print("viết sai rồi, hãy thử theo mẫu sau: cong/tru/nhan/chia")
