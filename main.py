from googletrans import Translator
from bs4 import BeautifulSoup
import requests


def translate_transcript_one_word(word):
    url = "https://wooordhunt.ru/word/"
    response = requests.get(url + word)

    soup = BeautifulSoup(response.text, "lxml")

    translation = soup.find("div", class_="t_inline_en")
    transcription = soup.find_all("span", class_="transcription")
    # choose britain english transcription
    br_index = 1
    if transcription[br_index] is None or translation is None:
        translate_many_words(word)
        return 0
    transcription = transcription[br_index]

    pair = f"{word} — {translation.text} {transcription.text}\n"
    rev_pair = f"{translation.text} — {word} {transcription.text}\n"
    # !!! bad idea
    write_translated_words(pair)
    write_translated_words(rev_pair)


def translate_many_words(message):
    translator = Translator()
    results = translator.translate(message, dest='ru')
    translation = f"{message} — {results.text}\n"
    rev_translation = f"{results.text} — {message}\n"
    # !!! bad idea
    write_translated_words(translation)
    write_translated_words(rev_translation)


def get_words_from_file(file):
    with open(file, encoding="utf-8-sig") as f:
        lines = f.readlines()
    return lines


def write_translated_words(words, file="translated.txt"):
    with open(file, "a", encoding="utf-8-sig") as f:
        f.write(words)


if __name__ == "__main__":
    file_name = 'words.txt'
    for item in get_words_from_file(file_name):
        item = item.rstrip("\n")
        print(item)
        if " " in item:
            translate_many_words(item)
        else:
            translate_transcript_one_word(item)
