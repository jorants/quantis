#HIDDEN
import subprocess
from subprocess import PIPE
import sys
import os
import random
from tempfile import NamedTemporaryFile

def docmd(cmd,input):
    sp = subprocess.Popen(cmd,stdin = PIPE,stdout = PIPE)
    return sp.communicate(input = input)[0]


def exists():
    res = docmd(["EasyQuantis","-l"],"")
    return not ("No Quantis USB device" in res)





def get_ints(n,minint=0,maxint=10):
    f = NamedTemporaryFile(delete=False)
    name = f.name
    f.close()
    res = docmd(["EasyQuantis","-u","0","-n",str(n),"--min",str(minint),"--max",str(maxint),"-i",name,"-s",","],"")
    if not "Done" in res:
        return [random.randrange(minint,maxint+1) for i in range(n)]
    #raise IOError("Quantis did something wierd")

    fp = open(name)
    data = map(int,fp.read().split(",")[:-1])
    fp.close()
    docmd(["rm",name],"")
    return data

def get_alphabet(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ind = get_ints(n,minint=0,maxint=25)    
    return reduce(lambda x,y: x+y,map(lambda x: alphabet[x],ind),"")
