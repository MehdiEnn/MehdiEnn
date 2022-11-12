Dict = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "One Hundred",
    1000: "One Thousand",
    1000000: "One Million",
    1000000000: "One Billion",
    1000000000000: "One Trillion"
}


def two_digs(answer):
    if int(answer) in Dict:
        letters = Dict[int(answer)]
        return letters
    elif 16 <= int(answer) <= 19:
        letters = Dict[int(answer[-1])] + "teen"
        if "Eightteen" in letters:
            letters = letters.replace("Eightteen", "Eighteen")
        return letters
    elif 20 <= int(answer) <= 99:
        unit = answer[-1]
        answer = int(answer) - int(unit)
        letters = Dict[int(answer)] + "-" + Dict[int(unit)]
        return letters


def three_digs(answer):
    hundreds = answer[0]
    digits = answer[-2:]
    if int(answer) in Dict:
        letters = Dict[int(answer)]
        return letters
    else:
        if int(digits) in Dict:
            letters = Dict[int(hundreds)] + " hundred " + Dict[int(digits)]
            return letters
        elif 16 <= int(digits) <= 19:
            letters = Dict[int(hundreds)] + " hundred " + Dict[int(digits[-1])] + "teen"
            if "Eightteen" in letters:
                letters = letters.replace("Eightteen", "eighteen")
            return letters
        elif 20 <= int(digits) <= 99:
            unit = answer[-1]
            digits = int(digits) - int(unit)
            letters = Dict[int(hundreds)] + " hundred " + Dict[int(digits)] + "-" + Dict[int(unit)]
            return letters


def thousand_digs(answer):
    if int(answer) in Dict:
        letters = Dict[int(answer)]
        return letters
    else:
        digs = three_digs(answer[-3:])
        if len(answer) == 4:
            thousands = Dict[int(answer[0])]
            letters = thousands + " thousand " + digs
            return letters
        elif len(answer) == 5:
            thousands = two_digs(answer[0: 2])
            letters = thousands + " thousand " + digs
            return letters
        elif len(answer) == 6:
            thousands = three_digs(answer[0: 3])
            letters = thousands + " thousand " + digs
            return letters


def million_digs(answer):
    if int(answer) in Dict:
        letters = Dict[int(answer)]
        return letters
    else:
        million = answer[:-6]
        if len(million) == 1:
            millions = Dict[int(million)]
        elif len(million) == 2:
            millions = two_digs(million)
        elif len(million) == 3:
            millions = three_digs(million)

        thousands = three_digs(answer[-6: -3])
        digs = three_digs(answer[-3:])
        letters = millions + " million " + thousands + " thousand " + digs
        return letters


def billion_digs(answer):
    billion = answer[:-9]
    if len(billion) == 1:
        billions = Dict[int(billion)]
    elif len(billion) == 2:
        billions = two_digs(billion)
    elif len(billion) == 3:
        billions = three_digs(billion)

    millions = three_digs(answer[-9: -6])
    thousands = three_digs(answer[-6: -3])
    digs = three_digs(answer[-3:])
    letters = billions + " billion " + millions + " million " + thousands + " thousand " + digs
    return letters


def trillion_digs(answer):
    trillion = answer[:-12]
    if len(trillion) == 1:
        trillions = Dict[int(trillion)]
    elif len(trillion) == 2:
        trillions = two_digs(trillion)
    elif len(trillion) == 3:
        trillions = three_digs(trillion)

    billions = three_digs(answer[-12: -9])
    millions = three_digs(answer[-9: -6])
    thousands = three_digs(answer[-6: -3])
    digs = three_digs(answer[-3:])
    letters = trillions + " trillion " + billions + " billion " + millions + " million " + \
        thousands + " thousand " + digs
    return letters


x = input("Enter a number : ")
length = len(x)
if length == 2:
    output = two_digs(x)
elif length == 3:
    output = three_digs(x)
elif 4 <= length <= 6:
    output = thousand_digs(x)
elif 7 <= length <= 9:
    output = million_digs(x)
elif 10 <= length <= 12:
    output = billion_digs(x)
elif 13 <= length <= 15:
    output = trillion_digs(x)
else:
    output = Dict[int(x)]

for zeros in ((" Zero thousand", ''), (" Zero hundred", ''), (" Zero million", ''), (" Zero billion", ''),
              (" Zero", '')):
    output = output.replace(*zeros)

print(output.lower().capitalize())
