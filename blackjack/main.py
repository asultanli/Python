


from art import logo
import random
print(logo)

def deal_card():
    #11 is the Ace.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = cards[random.randint(0,12)]
    return card
def calculate_score(list1):
    if 11 in list1 and 10 in list1 and len(list1)==2:
        return 0
    if 11 in list1 and sum(list1) == 21:
        list1.remove(11)
        list1.append(1)
        
    sum1 = sum(list1)
    return sum1

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Dealer has Blackjack! You lose."
    elif user_score == 0:
        return "You have Blackjack! You win."
    elif user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Dealer went over 21. You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

        
#main
#{}
computers_cards = []
users_cards = []
game_over = False
for i in range(2):
    users_cards.append(deal_card())
    computers_cards.append(deal_card())
    
while not game_over: 
    computers_score = calculate_score(computers_cards)
    users_score = calculate_score(users_cards)
    print(f"Your cards: {users_cards} Your score is {users_score}")
    print(f"Dealers first card is {computers_cards[0]}")

    if users_score == 0 or computers_score == 0 or users_score > 21:
        game_over = True
    else:
        choice = input("Do you want to add a card? y/n ")
        if choice == "y":    
            users_cards.append(deal_card())
            
        else:
            game_over = True
while computers_score != 0 and computers_score < 17:
    computers_cards.append(deal_card())
    computers_score = calculate_score(computers_cards)

print(compare(users_score,computers_score))
print(f"Dealers score was: {computers_score}")

