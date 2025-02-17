def is_valid_string(arr, s):
    positions = {}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] not in positions:
                positions[arr[i][j]] = []
            positions[arr[i][j]].append((i, j))
    #print(positions)
    if s[0] not in positions:
        return False
    
    prev_positions = positions[s[0]]
    print(prev_positions)
    for char in s[1:]:
        if char not in positions:
            return False

        found = False
        for prev_row, prev_column in prev_positions:
            for next_row, next_column in positions[char]:
                if next_row == prev_row or next_column == prev_column:
                    prev_positions = [(next_row, next_column)]
                    found = True
                    break
            if found:
                break
        if not found:
            return False
    return True

arr = [
    ["a", "x", "h", "o"], 
    ["a", "b", "j", "p"], 
    ["r", "h", "r", "j"], 
    ["n", "m", "b", "v"]
]
s = "abhj"
print(is_valid_string(arr, s))
