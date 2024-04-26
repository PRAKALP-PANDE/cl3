from mrjob.job import MRJob
import re

class Csen(MRJob):
	def mapper(self, _, line):
		sentences = re.split(r'[.?!]', line)
		for sentence in sentences:
			if sentence.split():
				yield sentence.strip(), 1

	def reducer(self, sentence, count):
		yield sentence, sum(count)

if __name__ == '__main__':
	Csen.run()