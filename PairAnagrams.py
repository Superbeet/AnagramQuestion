# Pair Anagrams

def find_anagrams(strings):
	if not strings:
		return []

	hashmap = {}
	size = len(strings)
	for i in xrange(size):
		sorted_str = "".join(sorted(strings[i]))
		if sorted_str not in hashmap:
			hashmap[sorted_str] = [strings[i]]
		else:
			hashmap[sorted_str].append(strings[i])

	result = []
	for strings in hashmap.values():
		anagram_pairs = pair_anagrams(strings)
		result.extend(anagram_pairs)

	result.sort()	# sort the result in alphabetical order

	return result

def pair_anagrams(strings):
	size = len(strings)
	result = []
	for i in xrange(0, size):
		for j in xrange(i + 1, size):
			if strings[i] < strings[j]:
				pair_str = strings[i] + " " + strings[j]
			else:
				pair_str = strings[j] + " " + strings[i]
			result.append(pair_str)
	return result

def load_data(path):
	# path = "./words"
	with open(path) as f:
		content = f.readlines()
	content = [x.strip('\n') for x in content]
	return content

# main function
def main():
	path = "./words"
	strings = load_data(path)
	result = find_anagrams(strings)

	for line in result:
		print line

main()

# assert find_anagrams(["abc", "acb"]) == ["abc acb"]
# assert find_anagrams(["abc", "", "acb", "bca"]) == ["abc acb", "abc bca", "acb bca"]
# assert find_anagrams(["abc", "acc"]) == []
