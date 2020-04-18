# same-type addition
print('same-type addition')
ii = 1 + 2  # <int> + <int>
print(ii, type(ii))
ff = 1.1 + 2.2  # <float> + <float>
print(ff, type(ff))
ss = 'saber' + ' fadaee'  # <str> + <str>
print(ss, type(ss))
ll = [1, 2] + [3, 5]  # <list> + <list>
print(ll, type(ll))

# different-type addition you may encounter error(s)!
print('\ndifferent-type addition')
# write a line to figure out type of <int> + <float>
i1 = 1 + 1.4
print(i1, type(i1))
# write a line to figure out type of <str> + <int>
i2 = 'sf' + 2
print(i2, type(i2))
# write a line to figure out type of <str> + <float>
i3 = 'sf' + 1.7
print(i3, type(i3))
# write a line to figure out type of <list> + <int>
i4 = [1, 3, 5] + [2, 4, 6]
print(i4, type(i4))
# write a line to figure out type of <list> + <float>
i5 = [1, 0, 7] + 5.4
print(i5, type(i5))
# write a line to figure out type of <list> + <str>
i6= [2, 4, 6, 8] + 'sf'
prinpt(i6, type(i6))