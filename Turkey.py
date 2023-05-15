def decline_word(word, gender, sentence):
    last = word[-1]
    second = word[-2]

    if sentence == "+":
        if gender == "ben":
            if last in ['a', '!']:
                return f"ben {word}y!m"
            elif last in ['e', 'i']:
                return f"ben {word}yim"
            elif last in ['o', 'u']:
                return f"ben {word}yum"
            elif last in ['ö', 'ü']:
                return f"ben {word}yüm"
            elif second in ['a', '!']:
                return f"ben {word}!m"
            elif second in ['e', 'i']:
                return f"ben {word}im"
            elif second in ['o', 'u']:
                return f"ben {word}um"
            elif second in ['ö', 'ü']:
                return f"ben {word}üm"

        elif gender == "sen":
            if last in ['a', '!'] or second in ['a', '!']:
                return f"sen {word}s!n"
            elif last in ['e', 'i'] or second in ['e', 'i']:
                return f"sen {word}sin"
            elif last in ['o', 'u'] or second in ['o', 'u']:
                return f"sen {word}sun"
            elif last in ['ö', 'ü'] or second in ['ö', 'ü']:
                return f"sen {word}sün"

        elif gender == "o":
            return f"o {word}"

        elif gender == "biz":
            if last in ['a', '!']:
                return f"biz {word}y!z"
            elif last in ['e', 'i']:
                return f"biz {word}yiz"
            elif last in ['o', 'u']:
                return f"biz {word}yuz"
            elif last in ['ö', 'ü']:
                return f"biz {word}yüz"
            elif second in ['a', '!']:
                return f"biz {word}!z"
            elif second in ['e', 'i']:
                return f"biz {word}iz"
            elif second in ['o', 'u']:
                return f"biz {word}uz"
            elif second in ['ö', 'ü']:
                return f"biz {word}üz"

        elif gender == "siz":
            if last in ['a', '!'] or second in ['a', '!']:
                return f"siz {word}s!n!z"
            elif last in ['e', 'i'] or second in ['e', 'i']:
                return f"siz {word}siniz"
            elif last in ['o', 'u'] or second in ['o', 'u']:
                return f"siz {word}sunuz"
            elif last in ['ö', 'ü'] or second in ['ö', 'ü']:
                return f"siz {word}sünüz"

        elif gender == "onlar":
            if last in ['a', '!', 'o', 'u'] or second in ['a', '!', 'o', 'u']:
                return f"onlar {word}lar"
            elif last in ['e', 'i', 'ö', 'ü'] or second in ['e', 'i', 'ö', 'ü']:
                return f"onlar {word}ler"

    if sentence == "-":
        d = "degil"
        if gender == "ben":
            return f"ben {word} {d}im"
        if gender == "sen":
            return f"sen {word} {d}sin"
        if gender == "o":
            return f"o {word} d"
        if gender == "biz":
            return f"biz {word} {d}iz"
        if gender == "siz":
            return f"siz {word} {d}siniz"
        if gender == "onlar":
            return f"onlar {word} {d}ler"

    if sentence == "?":
        if gender == "ben":
            if last in ["a", "!"] or second in ["a", "!"]:
                return f"ben {word} m!y!m"
            if last in ["e", "i"] or second in ["e", "i"]:
                return f"ben {word} miyim"
            if last in ["o", "u"] or second in ["o", "u"]:
                return f"ben {word} muyum"
            if last in ["ü", "ö"] or second in ["ü", "ö"]:
                return f"ben {word} müyüm"
        if gender == "sen":
            if last in ["a", "!"] or second in ["a", "!"]:
                return f"sen {word} m!s!n"
            if last in ["e", "i"] or second in ["e", "i"]:
                return f"sen {word} misin"
            if last in ["o", "u"] or second in ["o", "u"]:
                return f"sen {word} musun"
            if last in ["ü", "ö"] or second in ["ü", "ö"]:
                return f"sen {word} müsün"
        if gender == "o":
            if last in ["a", "!"] or second in ["a", "!"]:
                return f"o {word} m!"
            if last in ["e", "i"] or second in ["e", "i"]:
                return f"o {word} mi"
            if last in ["o", "u"] or second in ["o", "u"]:
                return f"o {word} mu"
            if last in ["ü", "ö"] or second in ["ü", "ö"]:
                return f"o {word} mü"
        if gender == "biz":
            if last in ["a", "!"] or second in ["a", "!"]:
                return f"biz {word} m!y!z"
            if last in ["e", "i"] or second in ["e", "i"]:
                return f"biz {word} miyiz"
            if last in ["o", "u"] or second in ["o", "u"]:
                return f"biz {word} muyiz"
            if last in ["ü", "ö"] or second in ["ü", "ö"]:
                return f"biz {word} müyüz"
        if gender == "siz":
            if last in ["a", "!"] or second in ["a", "!"]:
                return f"siz {word} m!s!n!z"
            if last in ["e", "i"] or second in ["e", "i"]:
                return f"siz {word} misiniz"
            if last in ["o", "u"] or second in ["o", "u"]:
                return f"siz {word} musunuz"
            if last in ["ü", "ö"] or second in ["ü", "ö"]:
                return f"siz {word} müsünüz"
        if gender == "onlar":
            if last in ['a', '!', 'o', 'u'] or second in ['a', '!', 'o', 'u']:
                return f"onlar {word}lar m!"
            elif last in ['e', 'i', 'ö', 'ü'] or second in ['e', 'i', 'ö', 'ü']:
                return f"onlar {word}ler mi"

    else:
        return 'error'


sentence = input("тип предложения (+ , - , ? :_ ")
gender = input("род (ben, sen, o, biz, siz, onlar : ")
word = input("сущ: ")

declined_word = decline_word(word, gender, sentence)
print("результат: ", declined_word)
