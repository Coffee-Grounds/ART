import argparse

parser = argparse.ArgumentParser()

parser.add_argument("sentence", type=str, help="тип предложения")
parser.add_argument("gender", type=str, help="местоимение")
parser.add_argument("word", type=str, help="сущ")

args = parser.parse_args()

print(args)

vowels_to_ending = {
    "a": "ı",
    "ı": "ı",
    "e": "i",
    "i": "i",
    "o": "u",
    "u": "u",
    "ö": "ü",
    "ü": "ü"
}


def decline_word(sentence, gender, word):
    last = word[-1]
    penultimate = word[-2]
    ending = vowels_to_ending.get(last)
    ending_second = vowels_to_ending.get(penultimate)
    two = ending or ending_second

    if sentence == "affirmative":
        if gender == "ben":
            if ending is not None:
                return f"ben {word}y{ending}m"

            if ending_second is not None:
                return f"ben {word}{ending_second}m"

        if gender == "sen":
            if two is not None:
                return f"sen {word}s{two}n"

        if gender == "o":
            return f"o {word}"

        if gender == "biz":
            if ending is not None:
                return f"biz {word}y{ending}z"

            if ending_second is not None:
                return f"biz {word}{ending_second}z"

        if gender == "siz":
            if two is not None:
                return f"siz {word}s{two}n{two}z"

        if gender == "onlar":
            if last in ['a', 'ı', 'o', 'u'] or penultimate in ['a', 'ı', 'o', 'u']:
                return f"onlar {word}lar"
            elif last in ['e', 'i', 'ö', 'ü'] or penultimate in ['e', 'i', 'ö', 'ü']:
                return f"onlar {word}ler"

    if sentence == "negative":
        d = "degil"
        if gender == "ben":
            return f"ben {word} {d}im"
        if gender == "sen":
            return f"sen {word} {d}sin"
        if gender == "o":
            return f"o {word} {d}"
        if gender == "biz":
            return f"biz {word} {d}iz"
        if gender == "siz":
            return f"siz {word} {d}siniz"
        if gender == "onlar":
            return f"onlar {word} {d}ler"

    if sentence == "question":
        if gender == "ben":
            if two is not None:
                return f"ben {word} m{two}y{two}m"
        if gender == "sen":
            if two is not None:
                return f"sen {word} m{two}s{two}n"
        if gender == "o":
            if two is not None:
                return f"o {word} m{two}"
        if gender == "biz":
            if two is not None:
                return f"biz {word} m{two}y{two}z"
        if gender == "siz":
            if two is not None:
                return f"siz {word} m{two}s{two}n{two}z"
        if gender == "onlar":
            if last in ['a', 'ı', 'o', 'u'] or penultimate in ['a', 'ı', 'o', 'u']:
                return f"onlar {word}lar m!"
            elif last in ['e', 'i', 'ö', 'ü'] or penultimate in ['e', 'i', 'ö', 'ü']:
                return f"onlar {word}ler mi"


declined_word = decline_word(args.sentence, args.gender, args.word)
print("результат: ", declined_word)
