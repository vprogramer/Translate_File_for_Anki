from main import write_translated_words
from main import get_words_from_file
import re


if __name__ == "__main__":
    # with open("podborka.txt", encoding="utf-8-sig") as f:
    #     lines = f.readlines()

    # (line.split("—") for line in lines)
    pattern = re.compile(r"(\D+) — (\D+)\s?([\[].+[\]])")
    for pair in get_words_from_file("podborka.txt"):
        gr = pattern.search(pair)
        print(gr.group(3))
        text = f"{gr.group(2)} — {gr.group(1)} {gr.group(3)}\n"
        write_translated_words(text, file="podborka.txt")
