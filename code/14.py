A, B = map(str, input().split())
alphabets = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet = alphabets.split()
print(alphabet.index(B)-alphabet.index(A)-1)