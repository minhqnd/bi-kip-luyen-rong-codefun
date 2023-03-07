n = int(input("Nhập số lượng số: "))
numbers = []

for i in range(n):
    number = int(input("Nhập số: "))
    numbers.append(number)

if len(numbers) > 0:
    min_number = min(numbers)
    max_number = max(numbers)
    print("Số đầu tiên là:", min_number)
    print("Số cuối cùng là:", max_number)
else:
    print("Không có số nào được nhập.")