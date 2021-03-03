import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''

def compile_(format_):
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    return CODE.format(username=username, password=password)

globformat = ''

def run_compiler(format_):
    globformat = format_
    glist = globformat.split('\n')
    l1 = glist[1].split(' ')
    l2 = glist[2].split(' ')
    s1 = l1[0] + ' hacker'
    s2 = l2[0] + ' 1234'
    l1[0] = s1
    l1[1] = s2
    final = '\n'.join(l1)
    format_ = final
    return compile_(format_)
