class Card:
    """A poker playing card"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    """A deck composed of Cards"""

    def __init__(self, cards):
        self.cards = {"H": cards[0:13],  # 13 + 13 + 13 + 13
                      "D": cards[13:26],  # 14 to 27
                      "C": cards[26:39],  # 28 to 41
                      "S": cards[39:52]}  # 42 to 52


dict = {"a": 1, "b": 2}
# print(list(dict.keys()))
#
# # print(f"Cards Left: {self.count()}")
# print("Current Formation:")
# print("* * * * * *   * * * * * *   * * * * * *   * * * * * *\n"
#       "* 5S      *   * 5S      *   * 5S      *   * 5S      *\n"
#       "*         *   *         *   *         *   *         *\n"
#       "*  Sword  *   *  Enemy  *   *  Tonic  *   *  Enemy  *\n"
#       "*         *   *         *   *         *   *         *\n"
#       "*      5S *   *      5S *   *      5S *   *      5S *\n"
#       "* * * * * *   * * * * * *   * * * * * *   * * * * * * ")
# print("Equipped weapon:")
# print("* * * * * *\n"
#       "* 5S      *\n"
#       "*         *\n"
#       "*  Sword  *\n"
#       "*         *\n"
#       "*      5S *\n"
#       "* * * * * *")
# print("Beaten with this weapon:")
# print("* * * * * *\n"
#       "*         *\n"
#       "*         *\n"
#       "*  Hands  *\n"
#       "*         *\n"
#       "*         *\n"
#       "* * * * * *")

# Fiend
# Sword
# Tonic
x = [1,2,3]
def examine(x):
    try:
        for i in range(len(x) - 1):
          f"{x.pop()}"
    except IndexError:
        return


def unravel_type(list):
    try:
        s = ""
        for elem in list:
            s = s + f"*  {elem}  *   "
        return s

    except:
        return

if __name__ == "__main__":
    pass
