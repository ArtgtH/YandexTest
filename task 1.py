import re


def text_format(text: str) -> str:
	result: str = ''

	words_list = re.findall(r'\w+|,', text)
	len_of_str: int = max(map(len, words_list)) * 3

	len_of_current_str: int = 0

	for index, word in enumerate(words_list):

		next_word = index + 1
		if len(words_list) > next_word:
			if words_list[next_word] == ',':
				word += ','
				words_list.pop(next_word)

		length_word = len(word)
		if len_of_current_str < len_of_str:
			len_of_current_str_after = len_of_current_str + length_word
			if len_of_current_str_after > len_of_str:
				result = result[0:-1]
				result += f'\n{word} '
				len_of_current_str = length_word + 1
			else:
				result += f'{word} '
				len_of_current_str += length_word + 1
		else:
			result = result[0:-1]
			len_of_current_str = length_word + 1
			result += f'\n{word} '
	else:
		result = result[0:-1]

	return result


def main():
	text = input()
	print(text_format(text))


if __name__ == '__main__':
	main()
