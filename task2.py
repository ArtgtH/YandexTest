def binary_search(prefix, words):

	left, right = 0, len(words) - 1
	result = -1

	while left <= right:
		mid = (left + right) // 2

		if words[mid].startswith(prefix):
			result = mid
			right = mid - 1
		elif words[mid] < prefix:
			left = mid + 1
		else:
			right = mid - 1

	return result


def main():

	n, q = map(int, input().split())
	words = [input() for _ in range(n)]

	for _ in range(q):

		k, prefix = input().split()
		k = int(k)

		index = binary_search(prefix, words)
		if index != -1 and index + k - 1 < n and words[index + k - 1].startswith(prefix):
			print(index + k)
		else:
			print(-1)


if __name__ == "__main__":
	main()
