class NhanVien:
    def __init__(self, fullname: str, age: int, wage: float):
        self.hoten = fullname
        self.tuoi = age
        self.luong = wage

    def __str__(self) -> str:
        message = '[ho ten: ' + self.hoten + '; tuoi: ' \
                  + str(self.tuoi) + '; luong: ' \
                  + str(self.luong) + ']'
        return message

    def __gt__(self, other):
        return(self.tuoi < other.tuoi)
    def __ge__(self, other):
        return(self.tuoi <= other.tuoi)
    def __lt__(self, other):
        return(self.tuoi > other.tuoi)
    def __le__(self, other):
        return(self.tuoi >= other.tuoi)
    def __eq__(self, other):
        return(self.tuoi == other.tuoi)