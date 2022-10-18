numbers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
input_alphabet = list(input())
time = 0
for i in input_alphabet:
  for j in numbers:
    if i in j:
      time += numbers.index(j) + 3
      
print(time)