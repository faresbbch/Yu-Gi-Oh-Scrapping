# Yu-Gi-Oh! Cards Dataset – Codebook  

## Metadata
- *Date of Data Collection:* February 12th, 2026
- *Date of publication:* February 12th, 2026 
- *Data Source:* https://ygoprodeck.com/api-guide/  
- *Author:* Fares Blibeche

## Overview:
This repository contains a dataset of all existing Yu-Gi-Oh! cards extracted from the public API provided by YGOPRODeck.

- **`all_ygo_cards.csv`** contains information on **13,616 cards**.  
  Each row represents a unique card and includes a variety of attributes describing its characteristics, effects, and gameplay mechanics.

- **`images_file/`** contains `.jpg` images for each Yu-Gi-Oh! card.  
  File names follow the format: `card_identifier.jpg`.
  
The card image folder is not included in this repository because it exceeds GitHub’s recommended file size limits and would make the repository too heavy to store and clone efficiently. The complete image dataset is available on Kaggle: [https://www.kaggle.com/datasets/faresbbch/all-yu-gi-oh-cards]


## Data Dictionary:

- **`id`** – Identifier of each card (corresponds to a number)

- **`name`** – The name of the card.

- **`desc`** – The full description or effect text written on the card.

- **`atk`** – The attack points of the card. Applies to Monster cards only.

- **`defe`** – The defense points of the card. Applies to Monster cards only.

- **`attribute`** – The attribute of the card (e.g., DARK, LIGHT, EARTH, etc.). Applies to Monster cards.

- **`type`** – Also known as "Race" in TCG/OCG (e.g., Spellcaster, Warrior, Zombie, Dragon, etc.). Applies to both Monster and Spell/Trap cards, depending on context.

- **`frametype`** – The visual frame used in the card’s design (e.g., normal, effect, ritual, fusion, synchro, xyz, link, spell, trap, etc.). Indicates the card category at a glance.

- **`level`** – The level of the monster (or "Rank" for XYZ monsters), represented by the number of stars. Applies only to non-Link monsters.

- **`card_sets`** – List of card sets in which the card was released
