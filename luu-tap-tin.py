from nhanvien import NhanVien
import os
import pickle

def ghi_nhanvien(thumuc: str, ten_taptin: str, obj: NhanVien):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(obj, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print('Xay ra loi trong qua trinh ghi file')

def doc_nhanvien(thumuc: str, ten_taptin: str) -> NhanVien:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            nv = pickle.load(f)
        return nv
    except Exception as e:
        return None

def main():
    path = 'G:\\Đồ Án'
    filename = 'nhanvien2.dat'
    sv1 = NhanVien('Van Nhi', 25, 10)
    ghi_nhanvien(path, filename, sv1)
    noidung = doc_nhanvien(path, filename)
    print(noidung)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()





with open(os.path.join(path, filename), 'wb') as f:
    pickle.dump(sv, f)
print('Ket thuc qua trinh luu du lieu')