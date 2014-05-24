class FastqParser(object):
    def __init__(self, fastq_fn):
        self.fastq_fn=fastq_fn
        self.bufsize=4096
        self.delimiter='>gi'


    def __iter__(self):
        prev_desc=None
        prev_seq=''

        with open(self.fastq_fn) as f:
            for line in f:
                if line.startswith(self.delimiter):
                    if prev_desc:
                        yield (prev_desc, prev_seq)
                    prev_desc=line.strip()
                    prev_seq=''
                else:
                    prev_seq+=line.strip()

