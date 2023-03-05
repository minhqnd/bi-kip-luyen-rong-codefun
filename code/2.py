input = input()
input = [int(n) for n in input.split()]
if len(input) == 3 and all(i <= 100 for i in input):
    input = (input[0]-input[1])*input[2]
print(input)