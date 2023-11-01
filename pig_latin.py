def latin(sentence):
	words = sentence.split()
	result = []
	for word in words:
		if len(word) == 1:
			new_word = word + 'ay'
		else:
			new_word = word[1:] + word[0] + 'ay'
		result.append(new_word)
	new_sentence = " ".join(result)
	return new_sentence
sentence = input("Enter a sentence")
print(latin(sentence))
