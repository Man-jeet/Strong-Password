ab=(input('enter the correct passoword: '))
if len(ab)==8:
    if ((('a'in ab) or ('b'in ab)or ('c'in ab)or ('d'in ab)or ('e'in ab)or ('f'in ab)or ('g'in ab)or ('h'in ab)or ('i'in ab)or ('j'in ab)or ('k'in ab)or ('l'in ab)or ('m'in ab)or ('n'in ab)or ('o'in ab)or ('p'in ab)or ('q'in ab)or ('r'in ab)or ('s'in ab)or ('t'in ab)or ('u'in ab)or ('v'in ab)or ('w'in ab)or ('x'in ab)or ('y'in ab)or ('z'in ab)) and (('A'in ab) or ('B'in ab)or ('C'in ab)or ('D'in ab)or ('E'in ab)or ('F'in ab)or ('G'in ab)or ('H'in ab)or ('I'in ab)or ('J'in ab)or ('K'in ab)or ('L'in ab)or ('M'in ab)or ('N'in ab)or ('O'in ab)or ('P'in ab)or ('Q'in ab)or ('R'in ab)or ('S'in ab)or ('T'in ab)or ('U'in ab)or ('V'in ab)or ('W'in ab)or ('X'in ab)or ('Y'in ab)or ('Z'in ab)) and (('1'in ab) or ('2'in ab) or ('3'in ab) or('4'in ab) or ('5'in ab) or ('6'in ab) or ('7' in ab) or ('8' in ab) or ('9'in ab)) and (('!' in ab) or ('@'in ab) or ('#'in ab) or ('$' in ab) or ('%'in ab) or ('^'in ab) or ('&'in ab) or ('*' in ab) or (','in ab) or ('?' in ab))):
        print('stong password')
    else:
        print('weak password')
        print('Enter the password in upper,lower, number and special character ')
elif len(ab)>8:
    print("your password length is greater")
else :
    print("Your password length is less")
