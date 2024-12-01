"""
https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CANDYDIST
"""
# Question link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CANDYDIST

import webbrowser

# Open the link when required
webbrowser.open("https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CANDYDIST")
print("Visit the question page: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CANDYDIST")


t = int(input())  # Number of test cases
for _ in range(t):
    n, x = map(int, input().split())  # Read candies (n) and group size (x)
    
    if n % x == 0:  # Check if candies can be distributed evenly
        even = n // x  # Calculate the number of groups
        if even % 2 == 0:  # Check if the number of groups is even
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
