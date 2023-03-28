# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string


def main():
    alphabet = "".join([
        string.ascii_lowercase,
        string.digits,
    ])
    len_word = 1
    generate_words(
        alphabet=alphabet,
        len_word=len_word,
        amount_of_words=10,
    )


def generate_words(alphabet: str, len_word: int, amount_of_words: int | None = None) -> None:
    for index, word in enumerate(alphabet, start=1):
        if amount_of_words is None or index <= amount_of_words:
            print(index, word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
