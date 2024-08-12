# A group of friends are playing cards. Only numeric cards are being used, along with the joker card (equivalent to 0), and the symbols in the cards are not taken into account. Each player will receive a set of cards. The rule of the game is to rearrange the set of cards to the possible lowest number sequence. The player with the set of cards forming the smallest number wins the game. The number sequence of cards forming the smallest number wins the game. The number sequence of the cards should not start with a joker card. The task is to write a program for developing the logic of the game considering the set of cards as a number. The output will be the lowest possible number that can be formed not beginning with 0.

def smallest_number_from_card(cards):
    
    zero=cards.count('0')
    non_zero_digits=[card for card in cards if card != '0']

    if not non_zero_digits:
        
        return "Invalid card"

    non_zero_digits.sort()

    smallest_number="".join(non_zero_digits)

    if zero > 0:
        
        return smallest_number[0] + "0"*zero +  smallest_number[1:]

    return smallest_number

cards = input("Enter the set of cards (digits and jokers as 0): ").strip()
result = smallest_number_from_card(cards)
print(result)