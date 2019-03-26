find = {'abc', 'der'}
text = {'deterabc'}

if any([s for s in text if any(xs in s for xs in find)]):
    print('LOL')

