# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:32:32 2020

@author: Igor

TODO: Add a probability for pick common/uncommon/rare
      Add a fallback to other card rarity when one groups is empty
      
"""

import random
from collections import namedtuple

Card = namedtuple('Card', 'name type')

# Card declaration
blacksmith = Card("Blacksmith", "Building")
inn = Card("Inn", "Building")
storeroom = Card("Storeroom", "Building")
tower = Card("Tower", "Building")
farm = Card("Farm", "Building")
harbor = Card("Harbor", "Building")
market = Card("Market", "Building")
stable = Card("Stable", "Building")
brewery = Card("Brewery", "Building")
granary = Card("Granary", "Building")
monastery = Card("Monastery", "Building")
siege_engine = Card("Siege Engine", "Building")
stronghold = Card("Stronghold", "Building")
training_field = Card("Training Field", "Building")
treasury = Card("Treasury", "Building")
citadel = Card("Citadel", "Building")
firepit = Card("Firepit", "Building")
temple = Card("Temple", "Building")
the_wall = Card("The Wall", "Building")
wizards_hut = Card("Wizards Hut", "Building")
aloth = Card("Aloth", "Hero")
dehengen = Card("Dehengen", "Hero")
devil_of_caroc = Card("Devil of Caroc", "Hero")
durance = Card("Durance", "Hero")
eder = Card("Eder", "Hero")
enfws = Card("Enfws", "Hero")
maneha = Card("Maneha", "Hero")
grieving_mother = Card("Grieving Mother", "Hero")
hiravias = Card("Hiravias", "Hero")
kana_rua = Card("Kana Rua", "Hero")
laudira = Card("Laudira", "Hero")
lenk = Card("Lenk", "Hero")
leyska = Card("Leyska", "Hero")
mafis = Card("Mafis", "Hero")
marceno = Card("Marceno", "Hero")
mordus = Card("Mordus", "Hero")
pallegina = Card("Pallegina", "Hero")
sagani = Card("Sagani", "Hero")
verzano = Card("Verzano", "Hero")
wula = Card("Wula", "Hero")
yngfey = Card("Yngfey", "Hero")
ystala = Card("Ystala", "Hero")
zacmar = Card("Zacmar", "Hero")
zahua = Card("Zahua", "Hero")
cipher = Card("Cipher", "Troop")
archers = Card("Archers", "Troop")
craftsmen = Card("Craftsmen", "Troop")
guards = Card("Guards", "Troop")
chanter = Card("Chanter", "Troop")
monk = Card("Monk", "Troop")
paladin = Card("Paladin", "Troop")


# Build listings
city_deck_stock_troops_common = {
        cipher: 10,
        archers: 12,
        craftsmen: 12,
        guards: 12
}

city_deck_stock_troops_uncommon = {
        chanter: 8,
        monk: 8,
        paladin: 8
}

city_deck_stock_troops_rare = {
        aloth: 1,
        dehengen: 1,
        devil_of_caroc: 1,
        durance: 1,
        eder: 1,
        enfws: 1,
        maneha: 1,
        grieving_mother: 1,
        hiravias: 1,
        kana_rua: 1,
        laudira: 1,
        lenk: 1,
        leyska: 1,
        mafis: 1,
        marceno: 1,
        mordus: 1,
        pallegina: 1,
        sagani: 1,
        verzano: 1,
        wula: 1,
        yngfey: 1,
        ystala: 1,
        zacmar: 1,
        zahua: 1,
}

city_deck_stock_buildings_common = {
        blacksmith: 8,
        inn: 8,
        storeroom: 8,
        tower: 8,
        farm: 16,
        }

city_deck_stock_buildings_uncommon = {
        harbor: 6,
        market: 6,
        stable: 6,
        brewery: 4,
        granary: 4,
        monastery: 4,
        siege_engine: 4,
        stronghold: 4,
        training_field: 4,
        treasury: 4,        
        }

city_deck_stock_buildings_rare = {
        citadel: 2,
        firepit: 2,
        temple: 2,
        the_wall: 2,
        wizards_hut: 2
}

# Build stacks
def build_stack(card_stock):
    cardlist = []
    for card, quantity in card_stock.items():
        cardlist.extend([card] * quantity)
    return cardlist


def build_shuffled_stack(card_stock):
    stack = build_stack(card_stock)
    random.shuffle(stack)
    return stack

city_deck_buildings_common = build_shuffled_stack(city_deck_stock_buildings_common)
city_deck_buildings_uncommon = build_shuffled_stack(city_deck_stock_buildings_uncommon)
city_deck_buildings_rare = build_shuffled_stack(city_deck_stock_buildings_rare)
city_deck_troops_common = build_shuffled_stack(city_deck_stock_troops_common)
city_deck_troops_uncommon = build_shuffled_stack(city_deck_stock_troops_uncommon)
city_deck_troops_rare = build_shuffled_stack(city_deck_stock_troops_rare)

city_deck_common = build_shuffled_stack({**city_deck_stock_buildings_common,
                                         **city_deck_stock_troops_common})

city_deck_uncommon = build_shuffled_stack({**city_deck_stock_buildings_uncommon,
                                         **city_deck_stock_troops_uncommon})
    
city_deck_rare = build_shuffled_stack({**city_deck_stock_buildings_rare,
                                         **city_deck_stock_troops_rare})

def build_pack(common, ncommon, uncommon, nuncommon, rare, nrare):
    pack = []
    for n in range(ncommon):
        pack.append(common.pop())

    for n in range(nuncommon):
        pack.append(uncommon.pop())
        
    for n in range(nrare):
        pack.append(rare.pop())        
    
    return pack

npacks = 17

packs = []
for p in range(npacks):
    packs.append(build_pack(city_deck_common, 5,
                            city_deck_uncommon, 4,
                            city_deck_rare, 2))

# Last pack is not even
