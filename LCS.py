s1 = input().strip()
s2 = input().strip()

if len(s1) < 2 or len(s2) < 2:
    print(0)
else:
    m = len(s1)
    n = len(s2)
    
    #Create a table (m+1) x (n+1), filled with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_len = 0  #Length of the longest common substring
    end_index = 0  #Index of the end of the substring in s1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i - 1  #Remember the end of the substring
            else:
                dp[i][j] = 0
    
    if max_len == 0:
        print(0)
    else:
        print(s1[end_index - max_len + 1 : end_index + 1])
