import pandas as pd

def knapsack_dp(values, weghts, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    df_step1 = pd.DataFrame.from_records(dp)
    print('Tạo mảng 2 chiều với số cột bằng len(capacity) , số hàng bằng len(values)')
    print(df_step1)
    """
    tính toán :
    có 2 trường hợp có thể xảy ra : 
        1. nếu đồ vật có khối lượng lớn hơn trọng tải hiện tại đang xét => không thể lấy thêm đồ vật đó
        2. else : đồ vật xem xét được bổ sung vào túi nếu tổng giá trị khi lấy thêm đồ vật lớn hơn việc không lấy thêm đồ vật đó
    """
    for i in range(1, n+1):
        for w in range(capacity + 1):
            if weghts[i - 1] > w :
                dp[i][w] = dp[i-1][w]
            else :
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i -1][w - weghts[i -1]])
        df_stepw = pd.DataFrame.from_records(dp)
        print('Xét đến đồ vật thứ '+str(i))    
        print(df_stepw)    
    
    selected_items = []
    i = n
    w = capacity
    while i > 0 and w > 0 : 
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w = w - weghts[i - 1]
        i = i - 1
        
    return dp[n][capacity] , selected_items

weights = [2, 1, 4, 3]
values = [3, 3, 4, 2]
capacity = 6

# Gọi hàm và in kết quả
result_value, selected_items = knapsack_dp(values, weights, capacity)
print(f"Total Value: {result_value}")
print("Selected Items:", selected_items)
