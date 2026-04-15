import csv
import requests
import pandas as pd
import time
import json

API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
API_URL_FOR_CARD = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name="
API_IMAGES_URL = "https://images.ygoprodeck.com/images/cards/"
IMAGES_PATH = "images_file"
WAIT_TIME = 0.055

# Data extraction from the API
response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json().get("data", [])  # Get the card list

    # Open a new CSV file in writing mode
    with open("all_ygo_cards.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["id", "name", "desc", "atk", "defe", "attribute", "type", "frametype", "level", "card_sets"])

        # Fill the file
        for card in data:
            temp_rep = requests.get(f"{API_URL_FOR_CARD}{card.get("name")}")
            if temp_rep.status_code == 200:
                card_data = temp_rep.json().get("data", [])[0]  # Get the data of one card
                
                card_sets_raw = card_data.get("card_sets", [])
                card_sets_clean = " | ".join(
					s.get("set_name", "")
					for s in card_sets_raw
					if s.get("set_name")
                    )
                
                print(card_sets_clean)
                # Write the next CSV line 
                writer.writerow([card.get("id"),
                                card.get("name"), 
                                card_data.get("desc", None), 
                                card_data.get("atk", None),
                                card_data.get("defe", None),
                                card_data.get("attribute", None),
                                card_data.get("race", None),
                                card_data.get("frameType", None),
                                card_data.get("level", None),
                                card_sets_clean
                                ])
            
            # Request to the image api 
            temp_url = f"{API_IMAGES_URL}{card.get("id")}.jpg"
            temp_rep = requests.get(temp_url)
            if temp_rep.status_code == 200:
                with open(f"{IMAGES_PATH}/{card.get("id")}.jpg", "wb") as f:
                    f.write(temp_rep.content)
            time.sleep(WAIT_TIME)