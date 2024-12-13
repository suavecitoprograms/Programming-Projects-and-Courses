# Write your solution here
def list_sum(a, b):
    sum = []
    for item in a:
        sum.append(item)
    for i in range(0, len(b)):
        sum[i] += b[i]
    return sum
    
def main(sum):
    if list_sum():
        print(sum)

if __name__ == "__main__":
    main()
    