# pillarsdraft
Build draft boosters for Pillars of eternity: Lords of Eastern Reach board game

## How to use

Execute the python file: `cube_pillars.py`

The output will be the pack contents as in:

```
Pack 1 contents:
Craftsmen, Tower, Guards, Craftsmen, Storeroom, Training Field, Monk, Stronghold, Stable, Durance, Lenk

Pack 2 contents:
Farm, Guards, Guards, Storeroom, Cipher, Paladin, Stable, Harbor, Chanter, Wizards Hut, Mafis

Pack 3 contents:
Farm, Blacksmith, Farm, Storeroom, Blacksmith, Paladin, Chanter, Siege Engine, Brewery, Kana Rua, Citadel

Pack 4 contents:
Craftsmen, Craftsmen, Farm, Farm, Farm, Monastery, Paladin, Harbor, Harbor, Temple, Grieving Mother

Pack 5 contents:
Farm, Tower, Inn, Cipher, Farm, Chanter, Paladin, Market, Stable, Mordus, Laudira

Pack 6 contents:
Craftsmen, Farm, Guards, Archers, Guards, Treasury, Monk, Stronghold, Stable, Yngfey, Temple

Pack 7 contents:
Blacksmith, Tower, Inn, Tower, Inn, Chanter, Granary, Treasury, Stable, Eder, Pallegina

Pack 8 contents:
Inn, Archers, Blacksmith, Archers, Guards, Siege Engine, Stable, Training Field, Market, Firepit, Aloth

Pack 9 contents:
Craftsmen, Archers, Blacksmith, Archers, Cipher, Monastery, Chanter, Monastery, Monk, Wizards Hut, Zahua

Pack 10 contents:
Blacksmith, Farm, Farm, Cipher, Archers, Treasury, Monastery, Monk, Brewery, Hiravias, Enfws

Pack 11 contents:
Inn, Cipher, Tower, Blacksmith, Farm, Granary, Market, Brewery, Harbor, Ystala, Firepit

Pack 12 contents:
Guards, Guards, Inn, Inn, Cipher, Chanter, Monk, Stronghold, Market, Devil of Caroc, Wula

Pack 13 contents:
Archers, Storeroom, Blacksmith, Craftsmen, Farm, Training Field, Chanter, Siege Engine, Treasury, The Wall, Citadel

Pack 14 contents:
Tower, Farm, Craftsmen, Farm, Archers, Monk, Granary, Monk, Market, Dehengen, Zacmar

Pack 15 contents:
Storeroom, Craftsmen, Cipher, Cipher, Storeroom, Monk, Paladin, Brewery, Paladin, Leyska, Verzano

Pack 16 contents:
Archers, Archers, Guards, Craftsmen, Archers, Stronghold, Paladin, Harbor, Training Field, The Wall, Marceno

Pack 17 contents:
Farm, Cipher, Tower, Guards, Craftsmen, Harbor, Paladin, Chanter, Siege Engine, Maneha, Sagani
```


## Rules to play with packs.

Instead a single deck for everyone run this program to build a group of 17 packs of 11 cards each.

Pack or put each pile turned down.

Run the drafting to build the deck. Each player will build its own deck with 40 cards.

Play the game as usual, when the rule say: Draw a card from City Deck, draw it from your own deck.

Discarded cards are not shuffled back.

Game ends when all city decks are empty

## Drafting methods

### Round robin

Each player choose a pile (in some order) until every player has the same amount of piles/packs

```
4 players = 4 piles/packs
3 players = 6 piles/packs
2 players = 8 piles/packs
```

Build a 40 card deck using these cards. Play as usual.

### Competitive

1. Pick the first pile/pack

2. The first player choose a card from it, the secong player pick a card from it, and goes on to no card left from first pile.

3. The next player will pick another pile/pack and choose a new card from it.

```
4 players = Use 16 piles
3 players = Use 12 piles (or use 15 piles for stronger decks)
2 players = Use 8 piles (or use more piles for stronger decks, always even number for balanced drafting)
```

Remember that more piles takes longer for competitive building and drafting.

For experienced players, it is recommended 30 minutes for drafting and 15 minutes for deck building.

Some piles will not be used. That is ok. Leave it as secret, because it can make more challeging about the opponent deck content.

## Combat rule changes

To be defined
