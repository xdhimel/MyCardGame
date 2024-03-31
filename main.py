import pygame
import random
import os
import time

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

BLACK = (0, 175, 0)
TABLE_COLOR = (0, 128, 0) 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Callbridge Card Game")


font = pygame.font.Font(None, 36)


def display_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))


def load_card_images(scale_factor=0.2):
    cards = {}
    suits = ['S', 'C', 'H', 'D']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    i=0
    for suit in suits:
        for value in values:
            img_path = os.path.join('cards', suit, f'{value}.jpg')
            card_image = pygame.image.load(img_path)
            card_image = pygame.transform.scale(card_image, (int(card_image.get_width() * scale_factor),
                                                             int(card_image.get_height() * scale_factor)))
            cards[(i, suit+value)] = card_image
            i+=1
    return cards


def create_shuffled_deck():
    deck = []
    suits = ['S', 'C', 'H', 'D']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    i= 0
    for suit in suits:
        for value in values:
            deck.append((i, suit+value))
            i+=1
    random.shuffle(deck)
    return deck


def deal_cards(deck, num_players):
    value_order =  ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    sorted_deck = sorted(deck, key=lambda card: card[0])
    hands = [[] for _ in range(num_players)]
    for i, card in enumerate(sorted_deck):
        hands[i % num_players].append(card)
    random.shuffle(hands)
    return hands


def scale_card(card_image, scale_factor):
    return pygame.transform.scale(card_image, (int(card_image.get_width() * scale_factor),
                                               int(card_image.get_height() * scale_factor)))


card_images = load_card_images()

deck = create_shuffled_deck()

num_players = 4

player_hands = deal_cards(deck, num_players)

running = True


number_to_display = 0
clock = pygame.time.Clock()
clicked_card = None
card_scale_factor = 1.25

clicked_time = None
stability_time = 5  

clicked = False
start = time.time()
end = 0
fps = 0
frames = 0

while running:
    current_time = pygame.time.get_ticks() / 1000  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        elif event.type == pygame.MOUSEBUTTONDOWN:
            number_to_display += 1
            clicked = True
            for i, hand in enumerate(player_hands):
                for j, card in enumerate(hand):
                    card_image = card_images[card]
                    card_width, card_height = card_image.get_size()
                    if i == 0:  # East
                        x = (SCREEN_WIDTH / 11)
                        y = (SCREEN_HEIGHT / 2.75) - ((len(hand) - 1) * 40 / 2) + (j * 40)
                    elif i == 1:  # West
                        x = (SCREEN_WIDTH - card_width - (SCREEN_WIDTH / 15))
                        y = (SCREEN_HEIGHT / 2.75) - ((len(hand) - 1) * 40 / 2) + (j * 40)
                    elif i == 2:  # North
                        x = (SCREEN_WIDTH / 2.14) - ((len(hand) - 1) * 40 / 2) + (j * 40)
                        y = (SCREEN_HEIGHT / 1.55)
                    else:  # South
                        x = (SCREEN_WIDTH / 2.14) - ((len(hand) - 1) * 40 / 2) + (j * 40)
                        y = (SCREEN_HEIGHT / 20)
                    
                    
                    if x < event.pos[0] < x + card_width / 3 and y < event.pos[1] < y + card_height/3:
                        clicked_card = (i, j)
                        print("Clicked Card: ", card)
                        clicked_time = current_time 
                        break

    screen.fill(BLACK)
    table_width = 400
    table_height = 300
    table_x = (SCREEN_WIDTH - table_width) / 1.90
    table_y = (SCREEN_HEIGHT - table_height) / 2.85
    pygame.draw.rect(screen, TABLE_COLOR, (table_x, table_y, table_width, table_height))

    padding = 40
    for i, hand in enumerate(player_hands):
        for j, card in enumerate(hand):
            if (i, j) == clicked_card and current_time - clicked_time <= stability_time:
                continue

            card_image = card_images[card]
            card_width, card_height = card_image.get_size()
            if i == 0:  # East
                x = (SCREEN_WIDTH / 11)
                y = (SCREEN_HEIGHT / 2.75) - ((len(hand) - 1) * padding / 2) + (j * padding)
                screen.blit(pygame.transform.rotate(card_image, 90), (x, y))
            elif i == 1:  # West
                x = (SCREEN_WIDTH - card_width - (SCREEN_WIDTH / 15))
                y = (SCREEN_HEIGHT / 2.75) - ((len(hand) - 1) * padding / 2) + (j * padding)
                screen.blit(pygame.transform.rotate(card_image, -90), (x, y))
            elif i == 2:  # North
                x = (SCREEN_WIDTH / 2.14) - ((len(hand) - 1) * padding / 2) + (j * padding)
                y = (SCREEN_HEIGHT / 1.55)
                screen.blit(card_image, (x, y))
            else:  # South
                x = (SCREEN_WIDTH / 2.14) - ((len(hand) - 1) * padding / 2) + (j * padding)
                y = (SCREEN_HEIGHT / 20)
                screen.blit(card_image, (x, y))

        

    
    if clicked_card and current_time - clicked_time <= stability_time:
        i, j = clicked_card
        card_image = card_images[player_hands[i][j]]
        card_width, card_height = card_image.get_size()
        if i == 0:  # East
            x = (SCREEN_WIDTH / 11)
            y = (SCREEN_HEIGHT / 2.75) - ((len(player_hands[i]) - 1) * padding / 2) + (j * padding)
            screen.blit(pygame.transform.rotate(scale_card(card_image, card_scale_factor), 90), (x, y))
            
        elif i == 1:  # West
            x = (SCREEN_WIDTH - card_width - (SCREEN_WIDTH / 15))
            y = (SCREEN_HEIGHT / 2.75) - ((len(player_hands[i]) - 1) * padding / 2) + (j * padding)
            screen.blit(pygame.transform.rotate(scale_card(card_image, card_scale_factor), -90), (x, y))
            
        elif i == 2:  # North
            x = (SCREEN_WIDTH / 2.14) - ((len(player_hands[i]) - 1) * padding / 2) + (j * padding)
            y = (SCREEN_HEIGHT / 1.55)
            screen.blit(scale_card(card_image, card_scale_factor), (x, y))
        else:  # South
            x = (SCREEN_WIDTH / 2.14) - ((len(player_hands[i]) - 1) * padding / 2) + (j * padding)
            y = (SCREEN_HEIGHT / 20)
            screen.blit(scale_card(card_image, card_scale_factor), (x, y))


    card_imag = pygame.image.load('2.jpg')
    card_imag1 = pygame.image.load('6.jpg')
    card_imag2 = pygame.image.load('J.jpg')
    card_imag3 = pygame.image.load('A.jpg')

    card_img = pygame.transform.scale(card_imag, (int(card_imag.get_width() * 0.2), int(card_imag.get_height() * 0.2)))
    card_img1 = pygame.transform.scale(card_imag1, (int(card_imag1.get_width() * 0.2), int(card_imag1.get_height() * 0.2)))
    card_img2 = pygame.transform.scale(card_imag2, (int(card_imag2.get_width() * 0.2), int(card_imag2.get_height() * 0.2)))
    card_img3 = pygame.transform.scale(card_imag3, (int(card_imag3.get_width() * 0.2), int(card_imag3.get_height() * 0.2)))

    screen.blit(card_img, (450, 335))
    screen.blit(card_img1, (350, 275))
    screen.blit(card_img2, (450, 185))
    screen.blit(card_img3, (550, 275))

    if clicked:
        display_text("FPS: {:.2f}".format(fps), 10, 10)

    display_text("Number: {}".format(number_to_display), 800, 650)

    pygame.display.update()
    end = time.time()
    frames += 1
    if (end - start) >= 1:
        fps = frames
        frames = 0
        start = time.time()

pygame.quit()