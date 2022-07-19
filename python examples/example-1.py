# write function of random number
def even_or_odd(num):
# determine if number is even by dividing by 2
  if num % 2 == 0:
# return fizz if true
    return 'fizz'
# if false return buzz
  else:
    return 'buzz'

print(even_or_odd(1002))