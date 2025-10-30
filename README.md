Fake News Generator

Fake News Generator is a fun, interactive Python project that automatically generates fake, funny, or random news headlines using templates, random words, and user inputs.
It combines data from multiple JSON files (names, animals, objects, places, and actions) to produce unique, humorous headlines just like a small virtual newsroom powered by Python. Users can also create, save, and reuse their own custom templates to personalize the experience.

Features--->>>

Random News Creation-->
                      
Generates headlines from multiple categories:

1.Indian Sports
2.Foreign Sports
3.Indian Politics
4.Foreign Politics
5.Bollywood
6.Hollywood

When creating your own Custom Template:
Create your own news template using placeholders:
{name}, {place}, {thing}, {animal}, {state_of_movement}

Automatic Saving
All generated headlines are saved in Saved_news.txt

Template Storage
Custom templates are stored in templates2.json for reuse

Fully Offline
Works entirely with local JSON data

Command-Line Interface (CLI)
Simple and user-friendly terminal interaction

Project Structure
Fake-News-Generator/
│
├── file1.py               # Main program file  
├── names.json            # Stores categorized names  
├── animals.json          # Contains animal names  
├── places.json           # Includes Indian & non-Indian places  
├── randothing.json       # Random objects/things  
├── stateofmove.json      # Action/movement verbs  
├── templates.json        # Predefined news templates  
├── templates2.json       # User-created templates  
└── Saved_news.txt        # Stores all generated headlines  

How It Works

1.The user selects a category (e.g., Sports, Politics, etc.).

2.The program fetches random data (name, place, animal, object, movement) from JSON files.

3.It fills placeholders inside a random template to generate a headline.

4.The result is printed and saved in Saved_news.txt.

5.Users can also create their own templates for future use.

Example Output
PRESS '1' FOR NEWS
PRESS '0' FOR EXIT

1. INDIAN SPORTS NEWS
2. FOREIGN SPORTS NEWS
3. INDIAN POLITICAL NEWS
4. FOREIGN POLITICAL NEWS
5. BOLLYWOOD NEWS
6. HOLLYWOOD NEWS
7. CREATE YOUR OWN NEWS
8. VIEW ALL PAST NEWS


Sample Generated Headline:
"Virat Kohli seen running with a goat in Mumbai after losing his bat."

Another Example:
"Tom Cruise caught dancing with an elephant during a film shoot in Paris."

Installation & Usage

Clone this repository

git clone https://github.com/yourusername/Fake-News-Generator.git
cd Fake-News-Generator


Run the script
Make sure Python 3.10+ is installed (for match-case syntax).

python main.py


Follow on-screen instructions
Choose categories, create your own news, or view past saved headlines.

Tech Stack

Language: Python 3.10+

Libraries: json, random

Storage: Local JSON and text files

Author

Deepanshu Sharma
