digits = [
    # 0
    "###"
    "# #"
    "# #"
    "# #"
    "###",

    # 1
    "  #"
    " ##"
    "# #"
    "  #"
    "  #",

    # 2
    "## "
    "  #"
    " # "
    "#  "
    "###",

    # 3
    "###"
    "  #"
    "###"
    "  #"
    "###",

    # 4
    "# #"
    "# #"
    "###"
    "  #"
    "  #",

    # 5
    "###"
    "#  "
    "## "
    "  #"
    "## ",

    # 6
    "###"
    "#  "
    "###"
    "# #"
    "###",

    # 7
    "###"
    "  #"
    " # "
    " # "
    " # ",

    # 8
    "###"
    "# #"
    "###"
    "# #"
    "###",

    # 9
    "###"
    "# #"
    "###"
    "  #"
    "###",

    # :
    "   "
    " # "
    "   "
    " # "
    "   ",
]

print("".join(chr(35+sum(0 if bit==" " else 1<<i for i,bit in enumerate(digit[j::3]))) for digit in digits for j in range(3)))
