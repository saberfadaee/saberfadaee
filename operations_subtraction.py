# same-type subtraction (subtractions which raise error commented out.)
print('same-type subtraction:')
ii = 3 - 2  # <int> - <int>
print(ii, type(ii))
ff = 1.1 - 2.2  # <float> - <float>
print(ff, type(ff))
# 'saber' - ' fadaee' will raise error there is NO str str subtraction
# [1, 2] - [3, 5] will raise error there is NO list list subtraction

# different-type subtraction you may encounter error(s)!
print('\ndifferent-type subtraction:')
imf = 3 - 2.3  # <int> - <float>
print(imf, type(imf))
# write a line to figure out type of <str> - <int>
# write a line to figure out type of <str> - <float>
# write a line to figure out type of <list> - <int>
# write a line to figure out type of <list> - <float>
# write a line to figure out type of <list> - <str>
