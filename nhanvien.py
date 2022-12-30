class NhanVien:
    def __init__(self,fullname,age,wage):
        self.hoten = fullname
        self.tuoi = age
        self.luong = wage

    def __str__(self):
        message= '[hoten:' + self.hoten + ';tuoi: ' + str(self.tuoi) + ';luong:' + str(self.luong) +']'
        return message


def main():
    nv1 = NhanVien('Le Anh Duy',19,1000)
    print(nv1)



if __name__=='__main__':
    main()



