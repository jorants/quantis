import math
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
    _,avg,__ = keydata(data)

    avgmax,avgmin = 3.76414323958, 2.67223279453

    if avg<avgmin:
        return False,   avgmin - avg 
    elif avg>avgmax:
        return False, avg - avgmax
    else:
        return True,0


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

def all_tests(s):
    scores = []
    
    all_ok = True
    for t in tests:
        passed,score = t(s.lower())
        scores.append(
            {
                'name':   t.__name__,
                'score':  score,
                'passed': passed
            }
        )
        all_ok = all_ok and passed
    
    score = sum(s['score']**2 for s in scores)**.5
    return all_ok, score, scores
