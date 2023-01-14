from nhancong import NhanVien
def in_list_nv():
    nv = [NhanVien('Lê Anh Duy', 23, 456640),
          NhanVien('Nguyễn Tuấn Anh', 20, 566671),
          NhanVien('Nguyễn Hoàng Minh Quý', 22, 8454560),
          NhanVien('Trần Phương Vi', 19, 7456430)]
    for item in nv:
        print(item)

in_list_nv()





def main():
  nv = [NhanVien('Lê Anh Duy', 23, 456640),
        NhanVien('Nguyễn Tuấn Anh', 20, 566671),
        NhanVien('Nguyễn Hoàng Minh Quý', 22, 8454560),
        NhanVien('Trần Phương Vi', 19, 7456430)]
  nv = sorted(nv, reverse = False)
  for item in nv:
    print(item)
if __name__ == '__main__':
    main()