n = int(input("Layers: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

left = ""
right = ""
k = n - 1 ## next letter
length = n * 2 - 1

while k > 0:
    left = left + alphabet[k]
    right = alphabet[k] + right
    length -= 2
    print(left + length * alphabet[k] + right)
    k -=1
    
print(left + length * alphabet[k] + right)

'''
n	3
alphabet	"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
left	"CB"
right	"BC"
k	0
length	1

'''

while k < n - 1:
    print(left + length * alphabet[k+1] + right)
    length += 2
    k +=1
    left = left[:-1]
    right = right[1:]




'''
Layers: 3
CCCCC
CBBBC
CBABC
CBBBC
CCCCC

'''