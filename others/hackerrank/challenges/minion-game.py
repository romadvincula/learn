def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    # consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    player_vowels = 0
    player_consonants = 0
    memory_dict = {}
    
    for i in range(0, len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            # print(substring)
            if substring[0] in vowels:
                player_vowels += 1
                # print(f"To Kevin, score: {player_vowels}")
            else:
                player_consonants += 1
                # print(f"To Stuart, score: {player_consonants}")
    
    if player_vowels > player_consonants:
        print(f"Kevin {player_vowels}")
    elif player_consonants > player_vowels:
        print(f"Stuart {player_consonants}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)