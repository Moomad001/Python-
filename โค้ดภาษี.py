income = int(input('เงินได้รวมเงินเดือน:'))
expenses = int(input('ค่าใช้จ่าย:'))
discount = int(input('ค่าลดหย่อน:'))
X = int(input('เงินได้ที่ไม่ใช่เงินเดือน:'))
N = (income-expenses-discount)
A = (0/100)
B = (5/100)
C = (10/100)
D = (15/100)
E = (20/100)
F = (25/100)
G = (30/100)
H = (35/100)
if N < 150001: 
  payable = N*A
if N > 150000 and N < 300001: 
  payable = N*B 
if N > 300000 and N < 500001: 
  payable = N*C
if N > 500000 and N < 750001: 
  payable = N*D
if N > 750000 and N < 1000001: 
  payable = N*F
if N > 1000000 and N < 2000001: 
  payable = N*G
if N > 2000000 and N < 5000001: 
  payable = N*H         
print ('เงินได้, %s' %income,"บาท")
print ('ค่าใช้จ่าย, %s' %expenses,"บาท")
print ('ค่าลดหย่อน, %s' %discount,"บาท")
print ('เงินได้สุทธิ, %s' %N,"บาท")
if N < 150001: 
  print ('ภาษี, %s' %A,"%")
if N > 150000 and N < 300001: 
  print ('ภาษี, %s' %B,"%")
if N > 300000 and N < 500001: 
  print ('ภาษี, %s' %C,"%")
if N > 500000 and N < 750001: 
  print ('ภาษี, %s' %D,"%")
if N > 750000 and N < 1000001: 
  print ('ภาษี, %s' %F,"%")
if N > 1000000 and N < 2000001: 
  print ('ภาษี, %s' %G,"%")
if N > 2000000 and N < 5000001: 
  print ('ภาษี, %s' %H,"%")
if X < 150001: 
  Z = X*0.005
if X > 150000 and N < 300001: 
  Z = X*0.005 
if X > 300000 and N < 500001: 
  Z = X*0.005
if X > 500000 and N < 750001: 
  Z = X*0.005
if X > 750000 and N < 1000001: 
  Z = X*0.005
if X > 1000000 and N < 2000001: 
  Z = X*0.005
if X > 2000000 and N < 5000001: 
  Z = X*0.005                 
print ('ค่าภาษี, %s' %Z,"บาท")  
print ('เงินภาษีที่ต้องจ่าย, %s' %payable,"บาท") 
