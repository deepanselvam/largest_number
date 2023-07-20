class Number:
    def largestNumber(self, nums):
        strs = [str(num) for num in nums]
        strs.sort(key=lambda x: x*2, reverse=True)
        largest_num = ''.join(strs)
        largest_num = largest_num.lstrip('0')
        return largest_num

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    num = Number()
    print(num.largestNumber(arr))
