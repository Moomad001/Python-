W = float(input("ใส่น้ำหนักของคุณ "))
H = float(input("ใส่ส่วนสูงของคุณ "))
print("น้ำหนักของคุณ คือ : %d " % W)
print("ส่วนสูงของคุณ คือ : %d " % H)
B = (W / ((H / 100) * (H / 100)))
print("BMI ของคุณ คือ : %.2f " % B)
if B > 0 and B < 18.5:
    print("น้ำหนักต่ำกว่าเกณฑ์")
elif B >= 18.5 and B <= 22.8:
    print("สมส่วน")
elif B >= 22.9 and B <= 24.8:
    print("น้ำหนักเกิน")
elif B >= 24.9 and B <= 29.8:
    print("โรคอ้วน")
elif B > 29.9:
    print("โรคอ้วนอันตราย")
else:
    print("ไม่อยู่ในเงื่อนไข")
