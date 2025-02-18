def is_valid_string(arr, s):
    positions = {}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] not in positions:
                positions[arr[i][j]] = []
            positions[arr[i][j]].append((i, j))
    
    if s[0] not in positions:
        return False
    
    prev_positions = positions[s[0]]
    
    for char in s[1:]:
        if char not in positions:
            return False
        
        next_positions = []
        for prev_row, prev_column in prev_positions:
            for next_row, next_column in positions[char]:
                if next_row == prev_row or next_column == prev_column:
                    next_positions.append((next_row, next_column))
        
        if not next_positions:
                     
                     
                     
            return False
        
        prev_positions = next_positions
    
    return True

arr = [
    ["a", "x", "h", "o"], 
    ["a", "b", "j", "p"], 
    ["r", "h", "r", "j"], 
    ["n", "m", "b", "v"]
]

s = "nmjo"
print(is_valid_string(arr, s))
