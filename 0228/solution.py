def commonPrefix(inputs):
    # Write your code here
    counts = []
    for string in inputs:
        count = 0
        for char in range(len(string)):
            right_pre = string[char:]
            for i in range(len(right_pre)):
                if right_pre[i] == string[i]:
                    count += 1
                else:
                    break
        counts.append(count)
            
    return counts