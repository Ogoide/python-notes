cats = []

while True:
    cat_name = input('Enter the name of cat ' + str(len(cats)+1) + '. (Or enter nothing to stop..)\n')
    # Input doesn't work like print. To add additional string values, you need to use string concatenation (+).
    if cat_name != '':
        cats.append(cat_name)
        # or, by using list concatenation, cats = cats + [cat_name]
    else:
        break

print('The cats\' names are:')
for cat in cats:
    print(f'\t{cat}')

