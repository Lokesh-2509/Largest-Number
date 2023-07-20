def largest_number(nums):
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x * 10, reverse=True)  # Custom comparison based on string concatenation
    largest_num = "".join(nums)
    largest_num = largest_num.lstrip('0')
    if not largest_num:
        return "0"
    return largest_num
if __name__ == "__main__":
    input_str = input("Enter the elements of the array (separated by space): ")
    A = list(map(int, input_str.split()))
    result = largest_number(A)
    print("Largest number:", result)
