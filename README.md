# Custom D&D Character Builder 

## Uses combination of Python, JSON, Javascript and HTML to gather, generate and display character data

### Python modules used to create various classes for different character data types
#### Python modules:
1. character_class.py --> creates basic DND character template
2. warlock_class.py --> creates Python class for DND warlock class
3. elf_class.py --> creates Python class for DND elf race
4. drow_class.py --> creates Python class for DND drow subrace
5. sage_class.py --> creates Python class for DND sage background
6. reaper_class.py --> creates Python class for custom Warlock patron called "The Reaper" (homebrew content)
7. charbuild_and_gameplay.py --> imports other modules, creates Python class with character name combining all other classes, instantiates the all-encompassing class, and compiles all data into JSON file ('soveliss-stats.json') when program runs. Additionally, there is a section to call methods/functions during game play, which updates the JSON file in real time


### Javascript modules used to interact with basic HTML pages for quick data lookup
#### Javascript modules:
1. lookup.js --> corresponding to lookup.html, a series of event listeners that will quickly display stats, to be used during game play for quick reference
2. all-stats.js --> corresponding to all-stats.html, simply parses JSON file ('soveliss-stats.json') and spits out all data on one page


### JSON files
1. soveliss-stats.json --> character stats data bank
2. formatted-spell-list.json --> all DND spells, which the Python modules use for reference and data gathering
3. formatted-invocations-list.json --> some Warlock invocations (more will be added in future), which the Python modules use for reference and data gathering


### Other files
1. styles.css --> very basic CSS file, basically just there to add margin spacing (I don't really care about making things pretty)
2. html files
3. game notes (for the campaign)



*Note: perhaps confusingly, a ***DND class*** refers to a character's "profession" (Wizard, Fighter, Bard, etc.), whereas a ***Python class*** is a blueprint for holding data and functions. So, Python classes were used to construct the DND class, race(s), background, etc.*