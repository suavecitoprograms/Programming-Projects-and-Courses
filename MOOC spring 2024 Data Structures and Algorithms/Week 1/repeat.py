def find(s):
    n = len(s)
    for i in range(1, n+1):
        if n % i == 0 and s[:i] * (n//i) == s:
            return i
            


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7