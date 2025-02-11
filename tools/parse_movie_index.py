import sys
import re

# Download https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index.txt.bz2
# Run bzip2 -dk enwiki-latest-pages-articles-multistream-index.txt.bz2
WIKI_INDEX_FILE = "/home/spencerkee/Documents/scripts/interest-map-thingy/enwiki-latest-pages-articles-multistream-index.txt"

BANNED_STRINGS = [
    "(soundtrack)",
]


def main():
    try:
        file = open(WIKI_INDEX_FILE, "r", encoding="utf-8")
    except Exception as e:
        print(e)
        sys.exit(1)

    fout = open("movie_index.txt", "w", encoding="utf-8")
    for line in file.readlines():
        # TODO Revisit this regex because it could remove films with 3 colons in them.
        if (
            "(film)" in line
            and not re.search(r".*\:.*\:.*\:", line)
            and not any((string for string in BANNED_STRINGS if string in line))
        ):
            fout.write(line)
    # TODO Should probably remove stuff like 3677974913:2947545:Wikipedia:Articles for deletion/Anamnesis (film)
    # TODO Should probably remove 24281337533:78109455:Bombay (film) (soundtrack)
    # TODO Should probably just parse the xml.
    file.close()
    fout.close()
    # There are 47519 films on wikipedia.


if __name__ == "__main__":
    main()
