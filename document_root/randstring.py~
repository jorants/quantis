#HIDDEN
import random, math
import string
import zlib, bz2

import scipy.spatial 


def rstring(n):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(n))

keyboard = ["qwertyuiop","asdfghjkl","zxcvbnm"]

def to_coord(c):
    if c not in string.ascii_lowercase:
        return (-1, -1)
    for (y,row) in enumerate(keyboard):
        if c in row:
            x = row.index(c) + y*0.5
            return (x,y)

def dist(d1, d2):
    return scipy.spatial.distance.euclidean(d1,d2)

u = ["erqiowupifxbnzxcvzbwrtpujsdfgvazdkljkljklqawruozvxmbaasdlfkjxcgvboqweurupdusfyirtqhbzxcnvqweiquiadusfiouioudfsapierupiqweruipqweuipruwqeipau",
     "wrioprioyiosfgxfhjvxcnapsfuhpaweruhjdfhzxcnmvnaprtjqwepopasodfjhzvqtprqiohfvjkbaepruhsfkjhjkhasdsfkasdjfkjasdkjfjfpuqwerhjkvhbkzsdhbjkasdhfa",
     "awepruihgpsbjknbznfbpafgpuewrzkjdgfaplksjdfhrmtvbcvpyigqwerhmzbcxvmngbpsrujkdfhsapjvhcxzjkhawerkjhvqpvuiapiosudfhqwetpviyzcaxfvkasdfjkherwqa",
     "qporewuhasdfjkhzcxvmnbartppqpghaipetljkcvnalsadfhklzhxcvprylhsdfqwerqwerqwetuysfgjkxcvkbalhfkldsqwoipsdfoqwoisopfdipzcxbhjkfdhjafsdhsdfasdaf",
     "qweportuvbknzhcjklhasdfopihrtpihvcepqwuirqwpeuigqwerpugipzcvpguipuiqgwerpuiqgwerpuigiqweiuqwiouqweioazsdguohzcxgkjhzgjhgaehgkjhasdfpigpqggaa",
     "bmnapcxiqwtbaerlvwqeighhrvzcxlhqrpzgolqtgpicuvugqewtpcvkjadfrtpidfhcvkqaetpadjkcvhgtrpadfjktyhniarbjagsbkczvgalfgqwjhglalfkslafkasdlgqwpgopo",
     "alfgpaiofiwiofdjaoerkcvnqwpfnerwpcvjnrthpfguyqwpjadfpcvnwepcvbefobnalvjkzprhalcvjhwepvbalfgkzpcvhapfjhalcvoqwhzpvhqpfrfpajvpaialvjhapfhalcks",
     "ctglxcnvkjxchgioytrdfkfgsdbnlvhxdilfhaseklrtfhklvnvnsdkltuhqweiodbjcfgmbklghdfiopgbidfngserbntfildfhngklzdfgbjkladhtgilaerhnkltfbnsdfklgdfil",
    "ctglxcnvkjxchgioytrdfkfgsdbnlvhxdilfhaseklrtfhklvnvnsdkltuhqweiodbjcfgmbklghdfiopgbidfngserbntfildfhngklzdfgbjkladhtgilaerhnkltfbnsdfklgdfiluhgilasdfhgilaserhtgklfgjkdhilghaeriltgdfklsgdfihgilaeruthdfkjghsdfihgiosdrnw",
     ]
u = map(lambda s: filter(lambda c: c in string.ascii_lowercase, s.strip().lower()), u)

#u = map(lambda s: s[:70],u)

print to_coord('f')

def randomtests(s, verbose=True):
    n = len(s)
#    print "Length: " + str(n)
    score = 0.0
    for c in string.ascii_lowercase:
        score += abs(s.count(c) / float(n) - 1./26.)
    print "Character count score: " + str(score)
    print "Length: " + str(n) + "\tzlib:\t\t" + str(len(zlib.compress(s,9))) + "\t\tBZ2:\t\t" + str(len(bz2.compress(s)))
    print "\t\tzlib(10):\t" + str(len(zlib.compress(s*10,9))) + "\t\tBZ2(10):\t" + str(len(bz2.compress(s*10,9)))
    print "\t\tzlib(99):\t" + str(len(zlib.compress(s*99,9))) + "\t\tBZ2(99):\t" + str(len(bz2.compress(s*99,9)))
    print "\t\tzlib(1000):\t" + str(len(zlib.compress(s*1000,9))) + "\t\tBZ2(1000):\t" + str(len(bz2.compress(s*1000,9)))
    
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
    print "Average dist: " + str(avg_dist) + "\t Short hops #: " + str(short_hops) + "\t l/r: " + str(l * 1.0/r) + "\t alt: " + str(alternations)
    
        
print "User strings\n-----"
for s in u:
    randomtests(s)
#    print ""
    

nrand = 1
randlen = 140
print "\nRandom strings\n------"
for i in range(nrand):
    randomtests(rstring(140))

randomtests(rstring(357))

#print rstring(140)
#print rstring(140)
#print rstring(140)
