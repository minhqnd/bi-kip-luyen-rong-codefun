A, N = map(str, input().split())
alphabets = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet = alphabets.split()
if alphabet.index(A) <= 24:
    print(alphabet[alphabet.index(A) + int(N)])
else:
    print(alphabet[alphabet.index(A) - 26 + int(N)])