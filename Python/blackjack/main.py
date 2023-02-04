import random

def deal_card():
  """returns random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

"""returns total score of the cards"""
def calculate_score(card):
  if len(card)==2 and sum(card)==21:
    return 0
  elif 11 in card and sum(card)>21:
    card.remove(11)
    card.append(1)
  return sum(card)


def compare(user_score,computer_score):
  if user_score==computer_score:
    return "draw"
  elif computer_score==0:
    return "Lose, oppenent has blackjack"
  elif user_score==0:
    return "You win, you have a blackjacl"
  elif computer_score>21:
    return "Computer went over You win"
  elif user_score>21:
    return "You went over You Loose"
  elif user_score>computer_score:
    return "You win"
  else:
    return "You loose"
  



while input("Do you want to play backjack?")=="y":
  user_cards=[]
  computer_cards=[]
  is_game_over=False
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your Cards: {user_cards},current score:{user_score}")
    print(f"Computer's first Card:{computer_cards[0]}")
    
    
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True
    else:
      user_should_deal=input("Type 'y' to get another card, type 'n' to pass:")
      if user_should_deal=="y":
        user_cards.append(deal_card())
      else:
        is_game_over=True
      
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  
  print(f"Your final hand is {user_cards} Your score: {user_score}")
  print(f"Computer's final hand is {computer_cards} Computer score:{computer_score}")
  print(compare(user_score,computer_score))