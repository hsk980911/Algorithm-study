cro_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_string = input()
cnt = 0
# for cro in cro_alphabet:
#   if cro in input_string:
#     cnt += input_string.count(cro)
for cro in cro_alphabet:
  input_string = input_string.replace(cro, '@')
print(len(input_string))