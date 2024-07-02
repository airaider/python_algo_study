from programmers.util.test_runner import run_tests

from itertools import product


def generate_dictionary_product():
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    for length in range(1, 6):  # Length from 1 to 5
        words = [''.join(p) for p in product(vowels, repeat=length)]
        dictionary.extend(words)

    dictionary.sort()  # Sort lexicographically
    return dictionary


def generate_dictionary_for():
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    def generate_words(current_word, max_length):
        if len(current_word) > 0:
            dictionary.append(current_word)

        if len(current_word) < max_length:
            for vowel in vowels:
                generate_words(current_word + vowel, max_length)

    generate_words('', 5)
    return sorted(dictionary)



def solution(word):
    dictionary = generate_dictionary_for()
    return dictionary.index(word)+1

def solution1(word):
    answer = 0
    a = ["".join(list(j)) for i in range(1, 6) for j in product(["A", "E", "I", "O", "U"], repeat=i)]
    a.sort()
    return a.index(word)+1


if __name__ == "__main__":
    run_tests(solution)
