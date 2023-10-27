def funcQuestion1(s, i):
    print(s[::-1] * i)


funcQuestion1("hello", 2)


# --------------------------------------------------------------------------
# Question 2
def funcQuestion2(s):
    upper = ""
    lower = ""

    for char in s:
        if char.isupper():
            upper += char
        else:
            lower += char

    new_string = upper + lower
    print(new_string)


funcQuestion2("RadWan")


# ------------------------------------------------------------------------
# Question 3
def funcQuestion3(s1, s2):
    sorted(s1)
    sorted(s2)
    return sorted(s1) == sorted(s2)


result = funcQuestion3("abab", "waba")
print(result)


# ---------------------------------------------------------------------------
# Question 4
def maximum(l):
    max_num = l[0]
    for num in l:
        if num > max_num:
            max_num = num
    print(f"The highest value in the list is {max_num} at index {l.index(max_num)}")


maximum([1, 2, 55, 4, 5])


def minimum(l):
    min_num = l[0]
    for num in l:
        if num < min_num:
            min_num = num
    print(f"The lowest value in the list is {min_num} at index {l.index(min_num)}")


minimum([55, 3, 5, 2, 1])


# -------------------------------------------------------------------------
# Question 5
def funcQuestion5(n):
    if n == 0:
        return 0
    return n % 10 + funcQuestion5(n // 10)


print(funcQuestion5(426))


# -------------------------------------------------------------------------
# Question 6
def remove_cons_dup(s):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return remove_cons_dup(s[1:])
    else:
        return s[0] + remove_cons_dup(s[1:])


print(remove_cons_dup("helllooooo woorrrrllllllllldddddddddddddddd"))
