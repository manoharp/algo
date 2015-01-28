""""
Append list and reverse
""""

def append_list():
    count = 10**5
    nums = []
    for i in range(count):
        nums.append(i)
        nums.reverse()

"""
In [23]: profile.run('append_list()')
         200005 function calls in 3.520 CPU seconds
"""

"""
Now implement the same using insert instead of append. Notice the difference in CPU time.
"""

def append_list_reverse():
    count = 10**5
    nums = []
    for i in range(count):
        nums.insert(0,i)

"""
profile.run('append_list_reverse()')
100005 function calls in 3.719 CPU seconds
"""

