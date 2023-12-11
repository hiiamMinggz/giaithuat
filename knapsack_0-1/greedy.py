def knapsack(values, weights, capacity):
    """0-1 Knapsack Problem solution greedy method

    Args:
        values (list[foat|int]): The list contains the values of each item
        weights (_type_): The list contains the weghts of each item
        capacity (_type_): The carrying capacity of the bag
    """
    n = len(values) 
    ratios = [(values[i] / weights[i], values[i], weights[i]) for i in range (n)]
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    total_weght = 0
    selected_items = []
    
    for ratio, value, weight in ratios:
        if total_weght + weight <= capacity :
            total_value += value
            total_weght += weight
            selected_items.append((value, weight))
            
    return total_value , total_weght , selected_items

values = [6, 5, 8, 9]
weights = [2, 3, 5, 7]
capacity = 10

result = knapsack(values, weights, capacity)
print(f"Total Value: {result[0]}, Total Weight: {result[1]}")
print("Selected Items:", result[2])