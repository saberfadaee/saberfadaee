# same-type division (divisions which raise error commented out.)
print('same-type division:')
ii = 3 / 2  # <int> / <int>
print(ii, type(ii))
ff = 1.1 / 2.2  # <float> / <float>
print(ff, type(ff))
# 'saber' / ' fadaee' will raise error there is NO str str division
# [1, 2] / [3, 5] will raise error there is NO list list division

# different-type division you may encounter error(s)!
print('\ndifferent-type division:')
imf = 3 / 2.3  # <int> / <float>
print(imf, type(imf))
# write a line to figure out type of <str> / <int>
# imf1= 'sf' / 2
# print(imf1, type(imf1))
# write a line to figure out type of <str> / <float>
# imf2= 'sf' / 2.1
# print(imf2, type(imf2))
# write a line to figure out type of <list> / <int>
# imf3= [1, 3, 5] / 2
# print(imf3, type(imf3))
# write a line to figure out type of <list> / <float>
# imf4= [1, 3, 5] / 2.5
# print(imf4, type(imf4))
# write a line to figure out type of <list> / <str>
# imf5= [1, 3, 5] / 'sf'
# print(imf5, type(imf5))