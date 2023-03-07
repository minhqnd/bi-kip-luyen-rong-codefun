def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 'YES'
    else:
        return 'NO'
    
A,B,C = map(int, input().split())
print(is_valid_triangle(A,B,C))