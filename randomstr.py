import subprocess
from subprocess import PIPE
import random
from tempfile import NamedTemporaryFile
from functools import reduce

def docmd(cmd,input):
    sp = subprocess.Popen(cmd,stdin = PIPE,stdout = PIPE)
    return sp.communicate(input = input)[0].decode('ascii')

def exists():
    try:
        res = docmd(["EasyQuantis","-l"],"")
        return not ("No Quantis USB device" in res)
    except OSError:
        return False


def randranges(n,minint=0,maxint=10):
    maxint -= 1
    f = NamedTemporaryFile(delete=False)
    name = f.name
    f.close()
    if not exists():
        return [random.randrange(minint,maxint+1) for i in range(n)]
    res = docmd(["EasyQuantis","-u","0","-n",str(n),"--min",str(minint),"--max",str(maxint),"-i",name,"-s",","],"")
    if not "Done" in res:
        return [random.randrange(minint,maxint+1) for i in range(n)]

    fp = open(name)
    data = map(int,fp.read().split(",")[:-1])
    fp.close()
    docmd(["rm",name],"")
    return data

def get_alphabet(n,alphabet = "abcdefghijklmnopqrstuvwxyz"):
    ind = randranges(n,0,len(alphabet))
    return reduce(lambda x,y: x+y,map(lambda x: alphabet[x],ind),"")
