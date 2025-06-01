An algorithm for finding the Longest Common Substring (LCS) between two strings s1 and s2 using dynamic programming.

Explanation:
Input strings s1 and s2.

Check for minimum length (if at least one string is shorter than 2 characters, output 0).

Create a DP table (dp) of size (m+1) x (n+1), filled with zeros.

Filling the table:

If characters s1[i-1] and s2[j-1] match, then dp[i][j] = dp[i-1][j-1] + 1.

If not, dp[i][j] = 0.

Update max_len and end_index if a longer substring is found.

Output the result:

If max_len == 0 (no common substrings), output 0.

Otherwise, output the substring itself (s1[end_index - max_len + 1 : end_index + 1]).

Example of work:
Input:
abcde
abfde
Output:
ab
(since "ab" is the longest common substring).
If you want to print only the length (max_len), replace the last line with print(max_len).
This algorithm runs in O(m×n) (where m and n are the lengths of the strings).
