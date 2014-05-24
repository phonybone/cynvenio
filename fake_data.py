'''
Generate fake fastq data from the rna.fa file, which contains
human rna.
'''

import sys, argparse, random
from fastq_parser import FastqParser
from random_read import RandomRead

def main(opts):
    random.seed(0)
    rr=RandomRead(opts.read_len, opts.default_qa)

    if opts.gene_fn:
        genes=read_genes_fn(opts.gene_fn)

    fuse=opts.fuse
    count=0
    with open(opts.output_fn, 'w') as output:
        fastq=FastqParser(opts.rna_file)
        for desc,seq in fastq:
            try:
                if desc not in genes:
                    continue
            except NameError:
                pass

            for i in xrange(opts.reads_per_gene):
                print >>output, rr(desc, seq)
                count+=1
                if count % opts.report_interval==0:
                    print >>sys.stderr, "%d reads..." % count

            fuse-=1
            if fuse == 0:
                break
    print '%d reads written to %s' % (count, opts.output_fn)


def read_genes_fn(gene_fn):
    genes=set()
    with open(gene_fn) as f:
        for line in f:
            genes.add(line.strip())
    return genes

def getopts():
    parser = argparse.ArgumentParser(description='Generate fake FASTQ data')
    parser.add_argument('--rna_file', default='/local/src/bowtie2/indexes/rna.fa')
    parser.add_argument('--output_fn', default='fake.fastq')
    parser.add_argument('--gene_fn')
    parser.add_argument('--read_len', default=100)
    parser.add_argument('--reads_per_gene', '-rpg', default=2000, type=int)
    parser.add_argument('--default_qa', default='z')

    parser.add_argument('-v', action='store_true', help='verbose')
    parser.add_argument('-d', action='store_true', help='debugging flag')
    parser.add_argument('-fuse', default=-1, type=int, help='debugging fuse')
    parser.add_argument('-report_interval', default=100000, type=int, help='status report')

    opts=parser.parse_args()
    if opts.d:
        print >> sys.stderr, opts
    return opts




if __name__=='__main__':
    sys.exit(main(getopts()))
