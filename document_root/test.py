<!doctype html>
<html>
<head>
<title>Quantum = cool</title>
<style>

.txtbox{
    border: 3px solid black;
    height: 300px;
    width: 500px;
}

.button{

background-color: #BB0000;
border: 1px solid black;
color: white;
padding: 5px 10px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 16px;
}


.bad{
    background-color: #FFBBBB ;
}

.ok{
    background-color: #BBFFBB ;
}


td{
    border: 1px solid black;
    padding: 5px;
    }

table{
border-collapse: collapse;
    }

</style>

</head>
<body>
<center>
<table>

<?python


import math
import random
import string

keyboard = ["qwertyuiop","asdfghjkl","zxcvbnm"]

def to_coord(c):

    if c not in string.ascii_lowercase:
        return (-1, -1)
    for (y,row) in enumerate(keyboard):
        if c in row:
            x = row.index(c) + y*0.5
            return (x,y)

def dist(x,y):
    return sum(map(lambda t: (t[0]-t[1])**2,zip(x,y)))**.5


def keydata(s):
    n = len(s)
    coords = map(to_coord, s)
    prev = coords[0]
    avg_dist = 0.0
    short_hops = 0
    alternations = 0
    for cur in coords[1:]:
        d = dist(prev, cur) 
        avg_dist += d / (n-1.)
        if d <= 1.8:
            short_hops += 1. / (n-1.)
        if (prev[0] < 4.5) != (cur[0] < 4.5):
            alternations += 1. / (n-1.)
        prev = cur
    l = len(filter(lambda coord: coord[0] < 4.5, coords))
    r = n - l
    return short_hops,avg_dist,alternations


def hop_test(data):

    hops,_,__ = keydata(data)
    hopmin,hopmax = .09090909090,.292929292929
    if hops<hopmin:
        return False, hopmin - hops
    elif hops>hopmax:
        return False, hops - hopmax 
    else:
        return True,0

def avgdist_test(data):
    """
    hops_list = []
    for j in range(100):
        rand = "".join([random.choice(string.ascii_lowercase) for i in range(len(data))])
        _,hops,__ = keydata(rand)
        hops_list.append(hops)

    print max(hops_list),min(hops_list)
    return False,0.
    """
    _,avg,__ = keydata(data)

    avgmax,avgmin = 3.76414323958, 2.67223279453

    if avg<avgmin:
        return False,   avgmin - avg 
    elif avg>avgmax:
        return False, avg - avgmax
    else:
        return True,0

"""
hops_list = []
for j in range(1000):
rand = "".join([random.choice(string.ascii_lowercase) for i in range(len(data))])
_,__,hops = keydata(rand)
hops_list.append(hops)
hops_list.sort()
print hops_list[5],hops_list[-5]
return False,0."""

def alternations_test(data):

    altmin,altmax = 0.373737373737, 0.636363636364

    _,__,alt = keydata(data)


    if alt<altmin:
        return False,  altmin - alt
    elif alt>altmax:
        return False, alt - altmax
    else:
        return True,0

    
    
def bz2test(data):
    import bz2
    avr = 301.
    s = bz2.compress(data*1000)
    return len(s)/avr > .980 , max(0,1- len(s)/avr)

def frequency_test(data):
    """
    hops_list = []
    for j in range(1000):
        rand = "".join([random.choice(string.ascii_lowercase) for i in range(len(data))])
        score = .0
        for c in string.ascii_lowercase:
            score += abs(rand.count(c) / float(len(rand)) - 1./26.)
        hops_list.append(score)
    hops_list.sort()
    print hops_list[-20:]
    print len(filter(lambda x: x<.533,hops_list))
    
    return False,0.
    score = 0.0
    """
    score = .0
    for c in string.ascii_lowercase:
        score += abs(data.count(c) / float(len(data)) - 1./26.)

    if score> .533:
        return False, score-.533
    else:
        return True,0


    
def entropy_test(data):
    score = .0
    for c in string.ascii_lowercase:
        if data.count(c) != 0:
            score += (data.count(c) / float(len(data)) ) * math.log((data.count(c) / float(len(data))))
    if -score<3.:
        return False, 3+score
    else:
        return True, 0
    

def row_test(data):
    def row_freq_abs(data):
        rows = map(lambda x: to_coord(x)[1],data)
        score = .0
        for c in [0,1,2]:
            print abs(rows.count(c) / float(len(rows)))
            score += abs(rows.count(c) / float(len(rows)) - len(keyboard[c])/26.)
        return score
    score = row_freq_abs(data)
    if score> .27:
        return False,score-.27
    else:
        return True,0


tests = [
    bz2test,
    hop_test,
    avgdist_test,
    alternations_test,
    frequency_test,
    row_test,
    entropy_test
    ]

frmt_ok = """
<tr>
  <td class='ok'>%s</td>
  <td class='ok'>%.03f</td>
  <td class='ok'>Passed</td> 
</tr>
"""
frmt_bad = """
<tr>
  <td class='bad'>%s</td>
  <td class='bad'>%.03f</td>
  <td class='bad'>Failed</td> 
</tr>
"""

scores = []
all_ok = True
for t in tests:
    passed,score = t(POST['data'][0].lower())
    if passed:
        println(frmt_ok % (t.__name__ , score))
    else:
        all_ok = False
        println(frmt_bad % (t.__name__ , score))
    scores.append(score)


import numpy as np
score = np.linalg.norm(np.array(scores))

nohtyp?>
</table>

<?python

if not all_ok:
    println("<h1>You Puny Human!!!</h1>")
    println("<img src='human.gif' />")
else:
    println("<h1>Wow, quantum is cool!</h1>")
    println("<img src='quantum.gif' />");
#println( score)

nohtyp?>
</center>
</body>

</html>
