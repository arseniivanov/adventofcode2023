from collections import Counter

lookup = dict(zip("23456789TJQKA", range(14)))
hands = []

for line in open("input"):
    cards, score = line.split()
    cnt = Counter(cards)

    #Capture overall hand strength
    cnt = sorted(cnt.values(), reverse=True)

    #Capture order strength from unsorted cards
    cardcodes = [lookup[ch] for ch in cards]

    #Combine
    hands.append((cnt, cardcodes, int(score)))

#Use tuple sorting order to first account for hand strength, then look at cardcodes
print(sum((i+1)*hand[2] for i, hand in enumerate(sorted(hands))))
