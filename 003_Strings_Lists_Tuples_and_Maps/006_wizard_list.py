wizard_list = 'spider legs, toe of frog, bat wing, slug butter, snake dandruff'
print(wizard_list)

wizard_list = ['spider legs', 'toe of frog', 'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)
print(wizard_list[2])

wizard_list[2] = 'snail tongue'
print(wizard_list)

print(wizard_list[2:5])

wizard_list.append('bear burp')
print(wizard_list)

wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

del wizard_list[4]
print(wizard_list)

del wizard_list[7]
del wizard_list[6]
del wizard_list[5]
print(wizard_list)
