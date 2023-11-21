

flag_register = 0x1234
the_mask = 8


print(f'This Flag {flag_register}')

if flag_register & the_mask:
    flag_registerlag_register = flag_register & ~the_mask
    print(flag_registerlag_register)
else:
    print('cara')
 
