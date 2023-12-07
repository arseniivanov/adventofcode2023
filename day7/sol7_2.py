from collections import Counter

lookup = dict(zip("J23456789TQKA", range(14)))
hands = []

for line in open("input"):
    cards, score = line.split()
    cnt = Counter(cards)
    
    #Do not account for jokers during strength sorting as its a "0"
    jokers = cnt.get("J", 0)
    del cnt["J"]

    #Deal with JJJJJ scenario
    if not cnt: cnt={"J":0}

    #Capture overall hand strength
    cnt = sorted(cnt.values(), reverse=True)

    #Add back jokers as the strongest card
    cnt[0] += jokers

    #Capture order strength from unsorted cards
    cardcodes = [lookup[ch] for ch in cards]

    #Combine
    hands.append((cnt, cardcodes, int(score)))

#Use tuple sorting order to first account for hand strength, then look at cardcodes
print(sum((i+1)*hand[2] for i, hand in enumerate(sorted(hands))))
