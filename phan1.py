import random

def ham_ngau_nhien():
  n=abs(int(input('n=')))
  random.seed(123)
  a= abs(float(input('a=')))
  b= abs(float(input('b=')))
  f = [(b-a)*random.random()+a for i in range(n)]
  print('ham f :')
  return f

v= ham_ngau_nhien()
print(v)


def sap_xep(v):
    reverse = len(v)
    if reverse == True:
        x1 = sorted(v, reverse=True)
        print('sắp xếp giảm dần:', x1)
    else:
        x2 = sorted(v, reverse=False)
        print('sắp xếp tăng dần:', x2)
z = sap_xep(v)
print(z)

from math import isclose

def tim_n(v):
  n = abs(float(input('nhap n= ')))
  if n in v:
    for i in range(len(v)):
      if isclose(n,v[i]):
        print("nhung gia tri trong list v bang n,",n,"=v[",i,"]=",v[i])
  else:
    print("ko tim thay")

b = tim_n(v)
print(b)



import pickle
y = str(v)
ten = str(input('Nhập vào tên tập tin: '))
dang = ten[-4:]
def luutaptin(ten,dang):
  if dang == '.txt':
    with open(ten,'w') as x:
     x.write(y)
  if dang == '.dat':
    with open(ten,'wb') as x:
     pickle.dump(y,x)
  else:
    print('Không tìm thấy loại tập tin')



def main():
  x=ham_ngau_nhien(-7,7,10)
  oath='D:\\data'
  filename= 'Caua2.txt'

  n=str(input("nhap loai tep can ghi'van ban' hoac'nhiphan':"))
  ghi_tap_tin(oath,filename,x,n)

  m=input("nhap chieu can sap xep'True' hoac'False':")
  print(m)
  if m=='True':
    x1=sap_xep_tang_dan(x)
  elif:
    x2=sap_xep_giam_dan(x)
  else:
    print("khong the sap xep")
  k=str(input("nhap loai tep can ghi'van ban' hoac'nhiphan':"))
  ghi_tap_tin(oath,filename,x1,k)

  a=float(input("nhap so can tim:"))
  vitri=tim_kiem_vi_tri(x,a)

  if len(vitri)==0:
    print("khong tim thay n")
  else:
    print("vi tri n:", vitri)


  if __name__ == "__main__":
    main()


