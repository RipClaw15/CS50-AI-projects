from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

A_say_Knave = Symbol("A said he is a knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),

)
# Biconditional is only true if both conditions are true
knowledge0 = And(knowledge0,Biconditional(AKnight,And(AKnave,AKnight)))


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave)))
)
knowledge1 = And(knowledge1,Biconditional(And(AKnave,BKnave),AKnight))
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),

)
same = Or(And(AKnight,BKnight),And(AKnave,BKnave))
different = Or(And(AKnight,BKnave),And(AKnave,BKnight)) 
knowledge2 = And(knowledge2,And(Biconditional(AKnight,same),Biconditional(BKnight,different)))
# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))),
)

# A said he is either a knight or a knave, but we dont know what he said, 
# if he said he is a knight then he is a knight,
# if he said he is a knave, that is impossible, because a knave always lies, 
# so A must be a knight
# but what if A is a knave and lied that he is a knight?
# So as I said earlier, it is impossible for A to say that "I am a knave", we know this for sure

# B said that A said " I am a knave", which we discussed previously, that is impossible
# so probably B is lying, he must be a knave
# B also said that C is a knave, which as we discussed earlier, 
# if B is a knave that could only mean that C is a knight for sure

# C said that A is a knight, which if C is a knight also means that A is a knight

# In the end A must be a Knight, C must be a Knight, because we know, 
# what B said is impossible to be true, so B is a Knave



knowledge3 = And(knowledge3,
                Not(A_say_Knave),
                Biconditional(BKnight,A_say_Knave),
                Biconditional(BKnight,CKnave),
                Biconditional(CKnight,AKnight)
                )


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
