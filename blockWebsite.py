import os
import re
import urllib2

def block(website):
    f = os.popen('ipconfig /displaydns')
    lines = filter(lambda x:x.count(website)>0,f.readlines())
    lines = list(set(map(parse, lines)))
    lines = map(lambda x:'   127.0.0.1       ' + x + '\n',lines)
    with open('C:\Windows\System32\drivers\etc\hosts','a') as hosts:
        hosts.writelines(lines)
    os.system('ipconfig /flushdns')
    print lines


def unblock(website):
    with open('C:\Windows\System32\drivers\etc\hosts','w+') as hosts:
        lines=filter(lambda x:x.count(website)==0,hosts.readlines())
        hosts.seek(0)
        print lines
        hosts.writelines(lines)

def parse(line):
    res = re.search(r'[a-z]+\.',line)
    if res:
        return res.string[res.start():-1]

if __name__=='__main__':
    block('zhihu')
