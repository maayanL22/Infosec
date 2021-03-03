import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''

def compile_(format_):
    print(format_)
    fr = format_.split('\n')
    print(fr[1])
    fr[1] = fr[1] + ' hacker'
    print(fr)
    fr[2] = fr[2] + ' 1234'
    print(fr)
    print('\n'.join(fr))
    format_ = '\n'.join(fr) 
    print(format_)
    print(re.search(r'USERNAME: (.*)', format_).group(1).split(' '))
    length = len(re.search(r'USERNAME: (.*)', format_).group(1).split(' '))
    print(length)
    print(re.search(r'USERNAME: (.*)', format_).group(1).split(' ')[length-1])
    username = re.search(r'USERNAME: (.*)', format_).group(1).split(' ')[length-1]
    password = re.search(r'PASSWORD: (.*)', format_).group(1).split(' ')[length-1]
    return CODE.format(username=username, password=password)
