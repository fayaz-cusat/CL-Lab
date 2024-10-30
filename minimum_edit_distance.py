def minimum_edit_distance(str1, str2):
    # Initialize the matrix
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    # Create a distance matrix
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
    
    # Fill the first row and first column
    for i in range(len_str1 + 1):
        dp[i][0] = i  # Deleting all characters from str1
    for j in range(len_str2 + 1):
        dp[0][j] = j  # Inserting all characters from str2
    
    # Compute the edit distance
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                           dp[i][j - 1] + 1,    # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
    
    edit_distance = dp[len_str1][len_str2]
    
    # Backtrack to find the operations
    operations = []
    i, j = len_str1, len_str2
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or dp[i][j] == dp[i - 1][j] + 1):
            operations.append(f"Delete '{str1[i - 1]}' from str1")
            i -= 1
        elif j > 0 and (i == 0 or dp[i][j] == dp[i][j - 1] + 1):
            operations.append(f"Insert '{str2[j - 1]}' into str1")
            j -= 1
        else:
            operations.append(f"Substitute '{str1[i - 1]}' with '{str2[j - 1]}'")
            i -= 1
            j -= 1
    
    operations.reverse()  # Reverse the operations to get the correct order
    return edit_distance, operations

# Example usage
str1 = "kitten"
str2 = "sitting"
distance, edit_operations = minimum_edit_distance(str1, str2)
print(str1, str2)
print(f"Edit Distance: {distance}")
print("Edit Operations:")
for op in edit_operations:
    print(op)
