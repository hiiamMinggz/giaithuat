"""
Bài toán cái túi (Knapsack)
Đề bài : Cho một cái túi có sức chứa cố định (được biểu diễn bằng trọng lượng tối đa mà túi có thể chứa), và một danh sách các đồ vật, 
Mỗi đồ vật có trọng lượng và giá trị riêng. 
Mục tiêu là chọn một tập hợp con của các đồ vật để đặt vào túi sao cho tổng trọng lượng của chúng không vượt quá sức chứa của túi và tổng giá trị là lớn nhất.
Giải quyết bằng giải thuật tham lam
Bước 1 : Tính tỷ lệ giá trị/trọng lượng cho mỗi đồ vật
Bước 2 : Sắp xếp các đồ vật theo tỷ lệ giá trị giảm dần
Bước 3 : Chọn đồ vật theo thứ tự đến khi túi đầy
"""

import pandas as pd
pd.set_option('mode.chained_assignment', None)

def knapsack_01(W, n):
    print("Khởi tạo túi với trọng tải : ", W)
    print("Số lượng đồ vật : ",n)
    weight_list = []
    value_list = []
    ratio_list = []
    for i in range(n):
        w = float(input("Nhập vào khối lượng của đồ vật thứ " +str(i+1)+ ": "))
        v = float(input("Nhập vào giá trị của đồ vật thứ " +str(i+1)+ ": "))
        ratio = v/w
        
        weight_list.append(w)
        value_list.append(v)
        ratio_list.append(ratio)
        
    my_dict = {'Khối lượng': weight_list , 
               'Giá trị': value_list ,
               'Trọng số': ratio_list}
    df = pd.DataFrame(my_dict)
    print("Danh sách đồ vật đã nhập : ")
    print(df)
    # sắp xếp danh sách đồ vật theo thứ tự giảm dần trọng số
    df.sort_values('Trọng số', inplace=True, ascending=False)
    print("Danh sách đồ vật sau khi sắp xếp trọng số ")
    print(df)
    # Lấy đồ vật cho đến khi túi đầy
    # Tính tổng tích lũy của cột 'Khối lượng'
    cumulative_sum = df['Khối lượng'].cumsum()
    selected_rows = df[cumulative_sum <= W]
    selected_rows.loc[:, 'Chọn'] = 1
    unselected_rows = df[~(cumulative_sum <= 10)]
    unselected_rows.loc[:, 'Chọn'] = 0
    # in ra kết quả
    print("Lựa chọn các đồ vật theo thứ tự trọng số giảm dần cho đến khi đầy túi ")
    result_df = pd.concat([selected_rows, unselected_rows])
    print("Kết quả")
    print(result_df)
if __name__ == '__main__':
    knapsack_01(10,4)