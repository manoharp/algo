import math

def cache(f):
    def a(*args):
        key = tuple(args)
        if key not in a.d:
            a.d[key] = f(*args)
        return a.d[key]
    a.d = {}
    return a

def nearby(q,x,y):
    n=1
    l=[]
    ds=[]
    xa=x
    ya=y
    q.sort()
    q.reverse()
    for pro,s,t,p in q:
        if s!=x and t!=y:
            dist2 = math.sqrt(x**2+y**2)
            dist3 = math.sqrt((s-xa)**2+(t-ya)**2)
            if (dist2+sum(ds))*.32>dist3:
                n+=1
                l.append((s,t,p))
                ds.append(dist3)
                xa=s
                ya=t
                if n>5:
                    break
 
    return n,l
                
    
@cache
def profit(x,y,p,d,c):
    dist = math.sqrt(x**2+y**2)
    cost = (c+2)*dist
    money = d*p
    return (money-cost,x,y,p)
    

n,c,d=raw_input().split()
n=int(n)
c=float(c)
d=float(d)
l=[]
for _ in xrange(n):
    l.append(tuple([int(i) for i in raw_input().split()]))
    
    
cd=1/d
ad = [ profit(x,y,p,1,c) for x,y,p in l]
ad.sort()
ad.reverse()


l = [ (x,y,p) for _,x,y,p in ad]
xact=False
for i in xrange(n):
    if not i%(n/10):
        cd*=d
        
    q = [profit(x,y,p,cd,c) for x,y,p in l[:50] ]
    pro,x,y,p = max(q)
    if pro < 0:
        break
    
    if xact:
        print 0,0
    xact=True
    
    q = [(px1,x1,y1,p1) for px1,x1,y1,p1 in q if px1>0]
    no,ps = nearby(q,x,y)
    print x,y,no
    for s,t,w in ps:
        print s,t
        l.remove((s,t,w))

    l.remove((x,y,p))  
    
    
