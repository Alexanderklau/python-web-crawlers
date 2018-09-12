def log(content, file='test.log', type=1):
    if type == 1:
        f = open(file, 'a+', encoding='utf-8')
    else:
        f = open(file, 'w+', encoding='utf-8')
        f.write(content)
