import random
from ln_dist import LnDist

'''
Create a random-ish read from a given sequence by selecting a portion out
at a random location.  Further alter the seleceted portion with some number
of random mutations.

Todo: write some code (here or elsewhere) that takes a collection of 
random reads, along with their position relative to the original sequence,
and randomly mutates a portion of them all the same way, to mimic a real-life
mutation that's been replicated.
'''

class RandomRead(object):
    def __init__(self, read_len, default_qa, max_muts=3):
        self.count=0
        self.read_len=read_len
        self.default_qa=default_qa
        self.max_muts=max_muts
        self.ln_dist=LnDist(max_muts)

    def __call__(self, desc, seq):
        try:
            start=random.randint(0, len(seq)-self.read_len)
            read=seq[start:start+self.read_len]
            l=self.read_len
        except ValueError:          # if len(seq) > opts.read_len
            read=seq
            start=0
            l=len(read)

        # do mutations:
        if self.max_muts > 0:
            n_muts=self.ln_dist.next()
            while n_muts>0:
                i=random.randint(0, l-1)
                base=random.choice('ACTG')
                seq=seq[:i]+base+seq[i+1:] # strings are immutable
                n_muts-=1


        self.count+=1
        short_desc='|'.join(desc.split('|')[:4]) + ('<%d-%d>' % (start, start+l))
        return '@%s %d-%d\n%s\n+\n%s' % (short_desc, start, start+l, read, self.default_qa*l)

