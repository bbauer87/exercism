from random import randint

# Score categories.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None

def score(dice, category):
    if category == "Yacht":
        if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
            global YACHT
            YACHT = 50
            return YACHT
        else:
            return 0
        
    elif category == "Choice":
        global CHOICE
        CHOICE=sum(dice)
        return CHOICE

    elif category == "Big Straight":
        comparison = [2,3,4,5,6]
        if dice == comparison:
            global BIG_STRAIGHT
            BIG_STRAIGHT = 30
            return BIG_STRAIGHT
        else:
            return 0
        
    elif category == "Little Straight":
        comparison = [1,2,3,4,5]
        if dice == comparison:
            global LITTLE_STRAIGHT
            LITTLE_STRAIGHT = 30
            return LITTLE_STRAIGHT
        else:
            return 0

    elif category == "Four of a Kind":
        tmp = []
        for x in dice:
            if x not in tmp: tmp.append(x)
        if len(tmp) != 2:
            return 0
        else:
            x = dice.count(tmp[0])
            y = dice.count(tmp[1])
            if x > y: repeated = (tmp[0], x)
            else:     repeated = (tmp[1], y)
            
            global FOUR_OF_A_KIND
            FOUR_OF_A_KIND = repeated[0] * repeated[1]
            return FOUR_OF_A_KIND
        
    elif category == "Full House":
        tmp = []
        for x in dice:
            if x not in tmp: tmp.append(x)
        if len(tmp) != 2:
            return 0
        else:
            x = dice.count(tmp[0])
            y = dice.count(tmp[1])
            global FULL_HOUSE
            FULL_HOUSE = x * tmp[0] + y * tmp[1]
            return FULL_HOUSE            
        
    elif category == "Sixes":
        if not dice.count(6):
            return 0
        else:
            global SIXES
            SIXES = dice.count(6) * 6
            return SIXES
        
    elif category == "Fives":
        if not dice.count(5):
            return 0
        else:
            global FIVES
            FIVES = dice.count(5) * 5
            return FIVES
        
    elif category == "Fours":
        if not dice.count(4):
            return 0
        else:
            global FOURS
            FOURS = dice.count(4) * 4
            return FOURS
        
    elif category == "Threes":
        if not dice.count(3):
            return 0
        else:
            global THREES
            THREES = dice.count(3) * 3
            return THREES
        
    elif category == "Twos":
        if not dice.count(2):
            return 0
        else:
            global TWOS
            TWOS = dice.count(2) * 2
            return TWOS
        
    elif category == "Ones":
        if not dice.count(1):
            return 0
        else:
            global ONES
            ONES = dice.count(1)
            return ONES
    else:
        return

dice=[randint(1,6) for x in range(5)]
print("\nThe five dices rolled:")
for x in dice: print(x,end=" ")
print("""\n\nWhich category you choose? (case-sensitive)

- Yacht
- Ones
- Twos
- Threes
- Fours
- Fives
- Sixes
- Full House
- Four of a Kind
- Little Straight
- Big Straight
- Choice
""")
category=input(">>> ")
result=score(dice, category)
if not result:
    print("Something went wrong with your category typing...")
else:
    print(f"You made a score of {result} point(s)!")
        
    
