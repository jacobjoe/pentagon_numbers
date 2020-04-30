""" Pentagon numbers"""

lst = []
i = 1
# while loop for list 10000 pentagon numbers
while i < 10000:
    p = i * (3 * i - 1) / 2
    lst.append(int(p))
    i += 1
print(lst)
# while loop for hold a number in list till inner loop complete and switch numbers
i = 0
while i < len(lst):
    m = i + 1
    j = m
    # nested while for made calculations by select one number with each number
    while j < len(lst):
        if lst[i] != lst[j]:
            k = lst[i] + lst[j]
            # if condition for check the addition of two pentagon numbers is a pentagon number
            if k in lst:
                n = lst[j] - lst[i]
                # if condition for the difference between above checked numbers are in pentagon numbers
                if n in lst:
                    print("two nums are ", lst[i], lst[j])
                    j += 1
                else:
                    j += 1
            else:
                j += 1
        else:
            j += 1
    i += 1
