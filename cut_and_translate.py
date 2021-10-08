from main import *


if __name__ == "__main__":
    for pair in get_words_from_file("character.txt"):
        translate_transcript_one_word(pair.split(" ")[0])
