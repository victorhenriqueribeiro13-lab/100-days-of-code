import game_data
import random
import art




user_guess = ""
SCORE = 0
user_right = True
print(art.logo)
def comparing(a,b):
    global user_guess
    global SCORE
    global user_right
    if SCORE > 0:
        print(art.logo)
    if SCORE > 0:
        print(f"You're right! Current score: {SCORE}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_guess == 'A' and a['follower_count'] > b['follower_count']:
        SCORE += 1
    elif user_guess == 'B' and b['follower_count'] > a['follower_count']:
            SCORE += 1
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        user_right = False
    if user_right:
        print("\n" * 100)


a = random.choice(game_data.data)
while user_right:
    b = random.choice(game_data.data)
    if b == a:
        b = random.choice(game_data.data)
    comparing(a, b)
    if user_guess == 'A' and a['follower_count'] > b['follower_count']:
        a = a
    elif user_guess == 'B' and b['follower_count'] > a['follower_count']:
        a = b




















# is_user_right = True
# while is_user_right:
#     score = 0
#     a = random.choice(game_data.data)
#     print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
#     print(art.vs)
#     b = random.choice([x for x in game_data.data if x['name'] != a['name']])
#     print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
#     user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
#     if user_guess == 'A' and a['follower_count'] > b['follower_count']:
#         score += 1
#         print(f"You are right! Final score: {score}")
#     elif user_guess == 'B' and b['follower_count'] > a['follower_count']:
#         score += 1
#         print(f"You are right! Final score: {score}")
#     else:
#         is_user_right = False
#         print(f"Sorry, that's wrong. Final score: {score}")
