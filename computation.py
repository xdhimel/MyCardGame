import random
import itertools

def merge_sort(cards):
    if len(cards) <= 1:
        return cards
    mid = len(cards) // 2
    left_half = cards[:mid]
    right_half = cards[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0][0] < right[0][0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result

player1_name=input("Name : ")
player2_name=input("Name : ")
player3_name=input("Name : ")
player4_name=input("Name : ")

p1_cards = []
p2_cards = []
p3_cards = []
p4_cards = []
place_number = 0
current_hand_number = 0
current_deck_cards = []
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ["S","C","H","D"]
deck = itertools.product(suits,nums)
deck1=list(deck)
sorted_deck = dict()
i = 0
for k in deck1:
    sorted_deck[str(i)] = k
    i+=1
print(sorted_deck)
random_desk = list(sorted_deck.items())
random.shuffle(random_desk)
deck1 = [[i[0], ''.join(i[1])]for i in random_desk]
print(random_desk)
# for i in range(len(deck1)):
#       deck1[i] = ''.join(deck1[i][1])

def merge_sort(cards):
    if len(cards) <= 1:
        return cards
    mid = len(cards) // 2
    left_half = cards[:mid]
    right_half = cards[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0][0] < right[0][0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result
    
user1 = []
user2 = []
user3 = []
user4 = []

for i in range(13):
    user1.append(deck1[i])

user1.sort(key=lambda a: a[0])

print('-'*5)

for i in range(13,26):
     user2.append(deck1[i])
    

user2.sort(key=lambda a: a[0])

print('-'*5)

for i in range(26,39):
    user3.append(deck1[i])

user3.sort(key=lambda a: a[0])
print('-'*5)

for i in range(39, 52):
    user4.append(deck1[i])

user4.sort(key=lambda a: a[0])
print('-'*5)



print(user1)
print("\n",user2)
print("\n",user3)
print("\n",user4)

'''ranks = ['A', 'K','Q','J','10','9','8','7','6','5','4','3','2']
deck =[(rank,deck) for deck in deck1
       
       for rank in ranks]
print(*deck, sep="\n")'''