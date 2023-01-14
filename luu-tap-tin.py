from nhanvien import NhanVien
import os
import pickle

def ghi_nhanvien(thumuc: str, ten_taptin: str, obj: NhanVien):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(obj, f)
        print('Hoan thanh qua trinh ghi')
    except Exception as e:
        print('Error')

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
    nv1 = NhanVien('Tran Phuong Vi',32,11000)
    ghi_nhanvien(path, filename, nv1)
    noidung = doc_nhanvien(path, filename)
    print(noidung)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()




