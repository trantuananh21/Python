class NhanVien():
    def __init__(self, ten, tuoi, ngay_sinh, ngay_lam_viec, que) -> None:
        self.ten = ten
        self.tuoi = tuoi
        self.ngay_sinh = ngay_sinh
        self.ngay_lam_viec = ngay_lam_viec
        self.que = que
        self.hsl = 4.2

class QuanLy(NhanVien):
    def __init__(self, ten, tuoi, ngay_sinh, ngay_lam_viec, que, quan_ly) -> None:
        super().__init__(ten, tuoi, ngay_sinh, ngay_lam_viec, que)
        self.quanly = quan_ly
        self.hsl = 5.0

class GiamDoc(NhanVien):
    def __init__(self, ten, tuoi, ngay_sinh, ngay_lam_viec, que, giam_doc) -> None:
        super().__init__(ten, tuoi, ngay_sinh, ngay_lam_viec, que)
        self.giam_doc = giam_doc
        self.hsl = 7.0