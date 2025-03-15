from random import randint
from Games.cards_and_deck import Card, Deck



class DungeonGame:
    def __init__(self, deck):
        self.weapons = {}
        for card in deck.cards["D"][0:9]:
            self.weapons[card] = []
        self.enemies = deck.cards["S"] + deck.cards["C"]
        self.potions = deck.cards["H"][0:9]
        self.universe = list(self.weapons.keys()) + self.enemies + self.potions
        self.health = 20
        self.run = True
        self.just_ran = False
        self.equipped = []
        self.weapon_history = []
        self.on_the_table_cards = []
        self.on_the_table_type = []
        self.first_round = True

    def count(self):
        return len(self.universe) == 0

    def game_over(self):
        return self.health <= 0

    def shuffle(self):
        shuffled = []
        while self.universe:
            shuffled.append(
                self.universe.pop(randint(0, len(self.universe) - 1)))
        while shuffled:
            self.universe.append(shuffled.pop())

    def run_away(self):
        while self.on_the_table_cards:
            self.universe.insert(0, self.on_the_table_cards.pop())
        self.run = False
        self.just_ran = True

    def new_round(self):
        i = 4
        if self.first_round is True:
            while i != 0 and self.count() is False:
                self.on_the_table_cards.append(self.universe.pop())
                i -= 1
            self.first_round = False

        elif self.just_ran is True:
            self.just_ran = False
            while i != 0 and self.count() is False:
                self.on_the_table_cards.append(self.universe.pop())
                i -= 1

        elif self.just_ran is False:
            self.run = True
            while i != 1 and self.count() is False:
                self.on_the_table_cards.append(self.universe.pop())
                i -= 1

    def representation(self):
        print(
            f"Current Formation:          Cards Left/Hidden: {len(self.universe)}       "
            f"   Health: {self.health}      ")
        number_of_cards_on_table = len(self.on_the_table_cards)
        temp_kind = []
        temp_card_top = self.on_the_table_cards.copy()
        temp_card_bottom = self.on_the_table_cards.copy()
        for card in self.on_the_table_cards:
            if card in self.enemies:
                temp_kind.append("Enemy")
            elif card in self.potions:
                temp_kind.append("Tonic")
            elif card in self.weapons:
                temp_kind.append("Sword")

        print("* * * * * *   " * number_of_cards_on_table)
        print(
            f"{unravel_kind_top(temp_card_top)}")
        print("*         *   " * number_of_cards_on_table)
        print(
            f"{unravel_type(temp_kind)}")
        print("*         *   " * number_of_cards_on_table)
        print(
            f"{unravel_kind_bottom(temp_card_bottom)}")
        print("* * * * * *   " * number_of_cards_on_table)

        if self.equipped == []:
            print("* * * * * *\n"
                  "*         *\n"
                  "*         *\n"
                  "*  Hands  *\n"
                  "*         *\n"
                  "*         *\n"
                  "* * * * * *")
        else:
            print("Equipped weapon:")
            print("* * * * * *\n"
                  f"* {self.equipped[0]}      *\n"
                  "*         *\n"
                  "*  Sword  *\n"
                  "*         *\n"
                  f"*      {self.equipped[0]} *\n"
                  "* * * * * *")
            print("Beaten with this weapon:")
            if self.equipped[1] == 15:
                print("None!")
            else:
                print(f"{unravel(self.weapon_history)}")

    def test(self):
        i = 30
        while i != 0:
            self.universe.pop()
            i -= 1

    def game_loop(self):

        name = input("Welcome to the Dungeon! What is your name?")
        print(f"Well {name}, let us enter the dungeon...")

        self.shuffle()
        # self.test()
        while self.game_over() is False and self.count() is False:
            self.new_round()
            while len(
                    self.on_the_table_cards) > 1 and self.game_over() is False:
                self.representation()
                self.action()

        if self.count() is True:
            while len(
                    self.on_the_table_cards) != 0 and self.game_over() is False:
                self.representation()
                self.action()
            if self.game_over() is True:
                print(
                    f"The dungeon puts another lost soul to rest... (rerun for replay)")
            else:
                print(
                    f"Truly impressive {name}, you have conquered this dungeon! (rerun for replay)")
        elif self.game_over() is True:
            print(
                f"The dungeon puts another lost soul to rest... (rerun for replay)")

    def action(self):
        action_or_run = 0
        action_no_run = 0

        if self.run is True:
            action_or_run = int(input(
                f"Select a card (1-{len(self.on_the_table_cards)}), or run away! (5)"))
            action_no_run = action_or_run

            if action_or_run == 5:
                self.run_away()
            elif (action_or_run or action_no_run) > len(
                    self.on_the_table_cards) or (
                    action_or_run or action_no_run) < 1:
                print(f"Your action choice is not valid, try again.")
                self.action()
            else:
                index = action_or_run - 1
                chosen_card = self.on_the_table_cards[index]
                if (action_or_run or action_no_run) in [1, 2, 3, 4]:

                    if chosen_card in self.weapons:
                        choice1 = int(input(
                            f"This is a Sword. Equip (1), or do nothing? (2)"))
                        if choice1 == 1:
                            self.equipped = [chosen_card, 15]
                            self.weapon_history = []
                            self.on_the_table_cards.remove(chosen_card)
                        elif choice1 == 2:
                            self.action()

                    if chosen_card in self.potions:
                        choice2 = int(
                            input(
                                f"This is a Tonic. Use (1), or do nothing? (2)"))
                        if choice2 == 1:
                            self.heal(chosen_card)
                            self.on_the_table_cards.remove(chosen_card)
                        elif choice2 == 2:
                            self.action()

                    if chosen_card in self.enemies:
                        choice3 = int(input(
                            f"This is an Enemy. Attack (1), or do nothing? (2)"))
                        if choice3 == 1:
                            self.attack(chosen_card)
                        elif choice3 == 2:
                            self.action()

        elif self.run is False:
            action_no_run = int(input(
                f"Select a card (1-{len(self.on_the_table_cards)})"))
            action_or_run = action_no_run

            if (action_or_run or action_no_run) > len(
                    self.on_the_table_cards) or (
                    action_or_run or action_no_run) < 1:
                print(f"Your action choice is not valid, try again.")
                self.action()
            else:
                index = action_or_run - 1
                chosen_card = self.on_the_table_cards[index]
                if (action_or_run or action_no_run) in [1, 2, 3, 4]:

                    if chosen_card in self.weapons:
                        choice1 = int(input(
                            f"This is a Sword. Equip (1), or do nothing? (2)"))
                        if choice1 == 1:
                            self.equipped = [chosen_card, 15]
                            self.weapon_history = []
                            self.on_the_table_cards.remove(chosen_card)
                        elif choice1 == 2:
                            self.action()

                    if chosen_card in self.potions:
                        choice2 = int(
                            input(
                                f"This is a Tonic. Use (1), or do nothing? (2)"))
                        if choice2 == 1:
                            self.heal(chosen_card)
                            self.on_the_table_cards.remove(chosen_card)
                        elif choice2 == 2:
                            self.action()

                    if chosen_card in self.enemies:
                        choice3 = int(input(
                            f"This is an Enemy. Attack (1), or do nothing? (2)"))
                        if choice3 == 1:
                            self.attack(chosen_card)
                        elif choice3 == 2:
                            self.action()

    def heal(self, card):
        raw_healing = rank_to_number_converter(card)
        current = self.health
        possible = self.health + raw_healing

        if current > possible:
            self.health = possible
        elif current <= possible:
            self.health = min(20, possible)

    def attack(self, card):
        raw_damage = rank_to_number_converter(card)

        if self.equipped == []:
            self.health -= raw_damage
            self.on_the_table_cards.remove(card)


        elif self.equipped[1] > raw_damage:
            if rank_to_number_converter(self.equipped[0]) < raw_damage:
                self.health -= raw_damage - rank_to_number_converter(self.equipped[0])
            self.equipped[1] = raw_damage
            self.weapon_history += number_to_rank_converter(raw_damage)
            self.on_the_table_cards.remove(card)

        elif self.equipped[1] <= raw_damage:
            choice4 = int(input(f"Your sword is too damaged for this enemy. "
                                f"Attack barehanded (1) or do nothing? (2)"))
            if choice4 == 1:
                self.equipped = []
                self.weapon_history = []
                self.health -= raw_damage
                self.on_the_table_cards.remove(card)
            elif choice4 == 2:
                self.action()
            else:
                print(f"Your action choice is not valid, try again.")
                self.action()


def unravel(listy):
    s = ""
    for item in listy:
        s = s + f'{item} '
    return s


def number_to_rank_converter(damage):
    if damage == 14:
        return "A"
    elif damage == 13:
        return "K"
    elif damage == 12:
        return "Q"
    elif damage == 11:
        return "J"
    elif damage == 10:
        return "T"
    else:
        return str(damage)


def rank_to_number_converter(card):
    if isinstance(card.rank, str):
        if "T" in card.rank:
            return 10
        elif "J" in card.rank:
            return 11
        elif "Q" in card.rank:
            return 12
        elif "K" in card.rank:
            return 13
        elif "A" in card.rank:
            return 14
    elif isinstance(card.rank, int):
        return card.rank


def unravel_type(listy):
    s = ""
    for elem in listy:
        s = s + f"*  {elem}  *   "
    return s


def unravel_kind_top(listy):
    s = ""
    for elem in listy:
        s = s + f"* {elem}      *   "
    return s


def unravel_kind_bottom(listy):
    s = ""
    for elem in listy:
        s = s + f"*      {elem} *   "
    return s


if __name__ == "__main__":
    twoHearts = Card(2, "H")
    threeHearts = Card(3, "H")
    fourHearts = Card(4, "H")
    fiveHearts = Card(5, "H")
    sixHearts = Card(6, "H")
    sevenHearts = Card(7, "H")
    eightHearts = Card(8, "H")
    nineHearts = Card(9, "H")
    tenHearts = Card("T", "H")
    jackHearts = Card("J", "H")
    queenHearts = Card("Q", "H")
    kingHearts = Card("K", "H")
    aceHearts = Card("A", "H")
    twoDiamonds = Card(2, "D")
    threeDiamonds = Card(3, "D")
    fourDiamonds = Card(4, "D")
    fiveDiamonds = Card(5, "D")
    sixDiamonds = Card(6, "D")
    sevenDiamonds = Card(7, "D")
    eightDiamonds = Card(8, "D")
    nineDiamonds = Card(9, "D")
    tenDiamonds = Card("T", "D")
    jackDiamonds = Card("J", "D")
    queenDiamonds = Card("Q", "D")
    kingDiamonds = Card("K", "D")
    aceDiamonds = Card("A", "D")
    twoClubs = Card(2, "C")
    threeClubs = Card(3, "C")
    fourClubs = Card(4, "C")
    fiveClubs = Card(5, "C")
    sixClubs = Card(6, "C")
    sevenClubs = Card(7, "C")
    eightClubs = Card(8, "C")
    nineClubs = Card(9, "C")
    tenClubs = Card("T", "C")
    jackClubs = Card("J", "C")
    queenClubs = Card("Q", "C")
    kingClubs = Card("K", "C")
    aceClubs = Card("A", "C")
    twoSpades = Card(2, "S")
    threeSpades = Card(3, "S")
    fourSpades = Card(4, "S")
    fiveSpades = Card(5, "S")
    sixSpades = Card(6, "S")
    sevenSpades = Card(7, "S")
    eightSpades = Card(8, "S")
    nineSpades = Card(9, "S")
    tenSpades = Card("T", "S")
    jackSpades = Card("J", "S")
    queenSpades = Card("Q", "S")
    kingSpades = Card("K", "S")
    aceSpades = Card("A", "S")

    cards = [
        # Hearts (2 to Ace)
        twoHearts, threeHearts, fourHearts, fiveHearts, sixHearts, sevenHearts,
        eightHearts, nineHearts, tenHearts, jackHearts, queenHearts, kingHearts,
        aceHearts,

        # Diamonds (2 to Ace)
        twoDiamonds, threeDiamonds, fourDiamonds, fiveDiamonds, sixDiamonds,
        sevenDiamonds,
        eightDiamonds, nineDiamonds, tenDiamonds, jackDiamonds, queenDiamonds,
        kingDiamonds, aceDiamonds,

        # Clubs (2 to Ace)
        twoClubs, threeClubs, fourClubs, fiveClubs, sixClubs, sevenClubs,
        eightClubs, nineClubs, tenClubs, jackClubs, queenClubs, kingClubs,
        aceClubs,

        # Spades (2 to Ace)
        twoSpades, threeSpades, fourSpades, fiveSpades, sixSpades, sevenSpades,
        eightSpades, nineSpades, tenSpades, jackSpades, queenSpades, kingSpades,
        aceSpades
    ]

    deck = Deck(cards)
    game = DungeonGame(deck)
    game.game_loop()
    # print(game.enemies)
    # print(game.weapons)
    # print(game.potions)

