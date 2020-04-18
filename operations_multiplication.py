# same-type multiplication (multiplications which raise error commented out.)
print('same-type multiplication:')
ii = 3 * 2  # <int> * <int>
print(ii, type(ii))
ff = 1.1 * 2.2  # <float> * <float>
print(ff, type(ff))
# 'saber' * ' fadaee' will raise error there is NO str str multiplication
# [1, 2] * [3, 5] will raise error there is NO list list multiplication

# different-type multiplication you may encounter error(s)!
print('\ndifferent-type multiplication:')
imf = 3 * 2.3  # <int> * <float>
print(imf, type(imf))
# write a line to figure out type of <str> * <int>
imf2 = 'sf' * 2
print(imf2, type(imf2))
# write a line to figure out type of <str> * <float>
imf3 = 'sf' * 2.1
print(imf3, type(imf3))
# write a line to figure out type of <list> * <int>
imf4 = [1, 3, 5] * 2
print(imf4, type(imf4))
# write a line to figure out type of <list> * <float>
imf5 = [1, 3, 5] * 7.6
print(imf5, type(imf5))
# write a line to figure out type of <list> * <str>
imf6 = [1, 3, 5] * 'sf'
print(imf6, type(imf6))
