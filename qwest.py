import pprint
from bs4 import BeautifulSoup
import requests
import json
import re

class abbreviation:
    informations = ""
    allergens = ""
    additives = ""
    def encode(self):
        return [self.informations, self.allergens, self.additives]

class dish:
    name = ""
    labels = ""
    price_student = ""
    price_guest = ""
    def encode(self):
        return [self.name, self.labels, self.price_student, self.price_guest]

class dayplan:
    date = ""
    dishes = []
    def encode(self):
        return [self.date, [i.encode() for i in self.dishes]]

class fullplan:
    dayplans = []
    abbreviations = abbreviation()
    def __init__(self, dayplan, abbreviation):
        self.dayplans=dayplan
        self.abbreviations= abbreviation
    def encode(self):
        return [[i.encode() for i in self.dayplans], self.abbreviations.encode()]

def fetch_website():
    r = requests.get("https://q-we.st/speiseplan/")
    return r.text

def get_soup(ingredients):
    return BeautifulSoup(ingredients, 'html.parser')

def get_dishes(unparsedItems):

    dishlist = []

    # Skip the first entry it only contains information about the displayed values
    for x in range(1, len(unparsedItems)):

        tmp_dish = dish()

        # Extract Name And Allergens and Labels
        #   Hirtenpfanne Griechischer Art V,a,a1,g,
        dishtext = tp_items[x].findNext("span", "live_speiseplan_item_title").text

        # Allergens and Labels are at the end of string - so we flip it, match, cut and reverse it, idk
        match = re.match('.*?\s', dishtext[::-1])

        #   Restore the original Order: | V,a,a1,g,|
        tmp_dishlabels = match[0][::-1]

        # The Name of the dish is the description without the labels
        tmp_dish.name = dishtext.replace(match[0][::-1], "")

        # Remove the Seperator Space and occasional |,| at the end
        #   | V,a,a1,g,| -> |V,a,a1,g|
        tmp_dishlabels.replace(" ", "")
        if (tmp_dishlabels.endswith(',')):
            tmp_dishlabels = tmp_dishlabels[:-1]

        tmp_dish.labels = tmp_dishlabels

        # Extract Prices for Guests and Students (seperated by a '|')
        pricetext = tp_items[x].findNext("span", "live_speiseplan_item_price").text
        match = re.findall('([0-9]{1,2}\,[0-9]{2}\s€)', pricetext)
        # Feiertage = 0
        if len(match) < 2:
            return dishlist

        tmp_dish.price_student = match[0]
        tmp_dish.price_guest = match[1]

        dishlist.append(tmp_dish)

    return dishlist

# Plan Container
sp_container = get_soup(fetch_website()).find("div", "live_speiseplan_content")

# Single Days | len(sp_header) -> amount of days found
sp_header = sp_container.findAll("div", "live_speiseplan_single_day_header")
if len(sp_header) < 1:
    raise Exception("Could not find Entries")

# All Day Plans
tmp_dayplans = []

for x in range(0, len(sp_header)):

    tmp_dayplan = dayplan()

    # Get the Date from the Title
    tp_datecontainer = sp_header[x].find("span", "live_speiseplan_title").text
    match = re.search('[0-9]{2}\.[0-9]{2}\.[0-9]{4}', tp_datecontainer)
    tmp_dayplan.date = match.group()

    # Get the Dishes Container
    tp_itemcontainer = sp_header[x].find_next_sibling("div")
    tp_items = tp_itemcontainer.findAll("div", "live_speiseplan_item")

    # Extract Dishes
    tmp_dayplan.dishes = get_dishes(tp_items)

    # Add Dayplan to list
    tmp_dayplans.append(tmp_dayplan)

# Allergene ETC
tmp_abbreviations = abbreviation()
tmp_abbreviations.informations = get_soup(fetch_website()).find("div", "kennzeichen informations").text
tmp_abbreviations.allergens = get_soup(fetch_website()).find("div", "kennzeichen allergene").text
tmp_abbreviations.additives = get_soup(fetch_website()).find("div", "kennzeichen zusatzstoffe").text

# Final Fullplan
plan = fullplan(tmp_dayplans, tmp_abbreviations)
#plan.abbreviations = tmp_abbreviations
#plan.dayplans = tmp_dayplans

class CustomEnc(json.JSONEncoder):
    def default(self, o):
        try:
            listtemp = o.encode()
        except TypeError:
            pass
        else:
            return list(listtemp)
        return json.JSONEncoder.default(self, o)


# JSON Encode
jsondata = json.dumps(plan, cls=CustomEnc)

# Write to File
with open("data6.json", "w") as outfile:
    outfile.write(jsondata)

