def find_duplicate(x):
    for char in x :
        print('(' if x.count(char)==1 else ')',end='')

find_duplicate('(( @')