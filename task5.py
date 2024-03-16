import sys


def autocomplete(prefix, words):
	max_popularity = -1
	autocomplete_index = -1
	for i, word_popularity in enumerate(words):
		word, popularity = word_popularity
		if word.startswith(prefix) and popularity > max_popularity:
			max_popularity = popularity
			autocomplete_index = i
	return autocomplete_index


def main():
	n, q = map(int, input().split())
	words = []
	for _ in range(n):
		word, popularity = input().split()
		words.append((word, int(popularity)))

	t = ''
	for _ in range(q):
		query = input()
		if query[0] == '+':
			t += query[2]
		else:
			t = t[:-1]
		print(autocomplete(t, words) + 1)


sys.setrecursionlimit(10 ** 6)
main()
