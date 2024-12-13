def generate(n):
    answer = ""
    if n < 10:
        return n
    text = str(n)
    total = text
    while True:
        total = int(text[0]) + int(text[-1])
        if total < 10:
            break
    answer += str(total)
    answer += answer[-1]
    return answer
        
if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(17)) # 1
    print(generate(18)) # 2
    print(generate(19)) # 3
    print(generate(20)) # 11
    #print(generate(131)) # 1141
    
    ## 2 digit numbers
    # idea is add the first and last digits
    # 2 + 8 = 10 = 1+0
    
    
    """ 339 = 3303 3+9 = 12 1+2 = 3
    idea is                                             9                1011
    0: 0    10: 11  20: 111     30: 212                 100: 919    110: 1011   120: 1111
    1: 1    11: 22  21: 121     31: 222                 101: 929    111: 1021   121: 1121
    2: 2    12: 33  22: 131     32: 232                 102: 939    112: 1031   122: 1131
    3: 3    13: 44  23: 141     33: 242                             113: 1041   123: 1141   243: 
    4: 4    14: 55  24: 151     34: 252                                  1051
    5: 5    15: 66  25: 161     35: 262                                  1061
    6: 6    16: 77  26: 171     36: 272                                  1071
    7: 7    17: 88  27: 181     37: 282                                  1081
    8: 8    18: 99  28: 191     38: 292     98: 898     108: 999         1091
    9: 9    19: 101 29: 202     39: 303     99: 909     109: 1001   119: 1101   129:    
    9 + 8 = 17 = 1 + 7 = 8                                      1+9 =
    digit 1 + digit 2 = 101
    2 + 9 = 11 digit 1 + digit 2
    3 + 9 = 12 digit 1 + digit 2 = 1 + 2 3
    3 + 8 = 11 digit 1 + digit 2 = 2:
        so first digit is a 2
        second digit is initial digit 2 + 1 = 9
    
    
    123
    1 + 2 = 3
    2 + 3 = 6
    
    
    """