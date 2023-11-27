# Đề bài : Giải hệ phương trình bậc nhất 2 ẩn (x, y)
# phân tích : Tham số [[a1, b1, c1], [a2, b2, c2]]
# Ý tưởng : sử dụng phương pháp thay 

def he_phuong_trinh(list1: list, list2: list):
    a1, b1, c1 = float(list1[0]), float(list1[1]), float(list1[2])
    a2, b2, c2 = float(list2[0]), float(list2[1]), float(list2[2])
    
    y = (c2 - ((a2 * c1) / a1)) / ((-a2 * b1) / a1 + b2)
    x = (c1 - b1 * y) / a1
    
    print(x)
    print(y)
    return 0

he_phuong_trinh([3,5,1], [2,-1,-8])