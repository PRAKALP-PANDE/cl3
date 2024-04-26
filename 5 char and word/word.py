from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"\b[\w'-]+\b")

class MRWord(MRJob):
    def mapper(self, _, line):
        for word in WORD_REGEXP.findall(line):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
	MRWord.run()

