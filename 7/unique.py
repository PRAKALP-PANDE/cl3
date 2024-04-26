from mrjob.job import MRJob
import re

regexp = re.compile(r'[\w]')

class uniques(MRJob):
	def mapper(self, _, line):
		for word in regexp.findall(line):
			yield word.lower(), 1

	def reducer(self, word, count):
		yield word, sum(count)

if __name__ == '__main__':
	uniques.run()