import random, math, sys
class LnDist(object):
    def __init__(self, N):
        if N<=0: raise ValueError(N)

        self.N=N
        self.X=math.exp(N)
        
    def __compute(self):
#            a=(random.random()*(self.X-1))+1
#            b=math.log(a)
#            c=self.N-math.floor(b)-1
#            if c>self.N:
#                print 'a=%g, b=%g, c=%g' % (a,b,c)

# This yields a different result:
#            yield math.floor(-math.log(random.random()))

        return self.N - math.floor(           # c
            math.log(                         # b
                random.random()*(self.X-1) +1 # a
                )
            ) - 1           # also c


    def __iter__(self):
        while True:
            yield self.__compute()



    def next(self):
        return self.__compute()

if __name__=='__main__':
    try:
        N=int(sys.argv[1])
    except Exception as e:
        print e
        N=10
    print 'N=%d' % N
    if N>16:
        print 'this could take a while...'

    d=LnDist(N)
    count=[0]*N
    for i in d:
        try:
            count[int(i)]+=1
        except IndexError as e:
            print '%s: %g' % (str(e), i)
            continue
        if count[N-1]==1:
            break


    for i,c in enumerate(count):
        print 'count[%d]: %d' % (i,c)

        
    
