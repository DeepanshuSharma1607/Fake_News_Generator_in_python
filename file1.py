import random
import json

class News:
    @staticmethod
    # get random name
    def get_random_name(category_number):
        match category_number:
            case 1: category_key = "sports_indian"
            case 2: category_key = "sports_foreign"
            case 3: category_key = "politics_indian"
            case 4: category_key = "politics_foreign"
            case 5: category_key = "actors_bollywood"
            case 6: category_key = "actors_hollywood"
            case _: 
                print("Invalid category number.")
                return None

        with open("names.json", "r") as file:
            names = json.load(file)
            return random.choice(names[category_key])

    # get random thing 
    @staticmethod  
    def get_random_thing():
        with open("randothing.json", "r") as file:
            things = json.load(file)
            return random.choice(things)
        
    # get random name of animal
    @staticmethod  
    def get_random_animal():
        with open("animals.json", "r") as file:
            animals = json.load(file)
            return random.choice(animals["animals"])

    # get random state of movement like running, working, dancing etc 
    @staticmethod  
    def get_random_movement():
        with open("stateofmove.json", "r") as file:
            movements = json.load(file)
            return random.choice(movements)
        
    # any random place
    @staticmethod  
    def get_random_place(num):
        with open("places.json", "r") as file:
            places = json.load(file)
            if num % 2 == 1:
                return random.choice(places["Indian"])
            else:
                return random.choice(places["Not Indian"])


# choosing template for fake news
class NewsTemplate:
    @staticmethod
    def display_and_save_news(news_data, num):
        with open("templates.json", "r") as file:
            template_data = json.load(file)

        name = news_data[0]
        thing = news_data[1]
        animal = news_data[2]
        movement = news_data[3]
        place = news_data[4]

        if num <= 2:
            template = random.choice(template_data["sports_template"])
        elif 2 < num <= 4:
            template = random.choice(template_data["political_template"])
        else:
            template = random.choice(template_data["actors_fun"])
        
        news_text = template.format(
            name=name,
            thing=thing,
            animal=animal,
            state_of_movement=movement,
            place=place
        )
        
        with open("Saved_news.txt", "a") as file:
            file.write(news_text + "\n\n")
        
        print("\n" + "=" * 100)
        print("!!!...BREAKING NEWS")
        print("=" * 100)
        print(news_text)
        print("=" * 100 + "\n")


class OwnNews:
    @staticmethod
    def create_your_own_news(data):
        try:
            choice = int(input("ENTER 1 TO CREATE YOUR OWN NEWS\nPRESS 2 TO VIEW RANDOM NEWS\nENTER HERE: "))
        except ValueError:
            print("Invalid input! Please enter a number (1 or 2).")
            return

        if len(data) != 5:
            print("Data must contain 5 items: name, thing, animal, state_of_movement, place.")
            return

        name, thing, animal, movement, place = data

        if choice == 1:
            print("\nCREATE YOUR FAKE NEWS TEMPLATE")
            print("!!!")
            print("Use placeholders: {name}, {place}, {animal}, {thing}, {state_of_movement}\n")
            print("Example: Rally at {place} ends early as {animal} climbs stage to give speech.\n")

            template = input("ENTER YOUR TEMPLATE: ")

            try:
                final_news = template.format(
                    name=name,
                    thing=thing,
                    animal=animal,
                    state_of_movement=movement,
                    place=place
                )
            except KeyError as e:
                print(f"Missing placeholder: {e}. Please include all placeholders correctly.")
                return

            print("\n" + "=" * 100)
            print(final_news)
            print("\n" + "=" * 100)
            
            try:
                with open("templates2.json", "r") as file:
                    templates = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                templates = {"game_data": []}

            if "game_data" not in templates:
                templates["game_data"] = []

            templates["game_data"].append(final_news)

            with open("templates2.json", "w") as file:
                json.dump(templates, file, indent=2)

            with open("Saved_news.txt", "a") as f:
                f.write(final_news + "\n")

        elif choice == 2:
            print("\nHere's a random funny news headline for you:\n")
            try:
                with open("templates2.json", "r") as file:
                    templates = json.load(file)
                    if "game_data" not in templates or not templates["game_data"]:
                        print("No saved templates found.")
                        return
                    random_template = random.choice(templates["game_data"])
            except (FileNotFoundError, json.JSONDecodeError):
                print("No templates file found.")
                return

            print()
            print(random_template.format(
                name=name,
                thing=thing,
                animal=animal,
                state_of_movement=movement,
                place=place
            ))
            print()
        else:
            print("Invalid choice! Please enter 1 or 2.")


def main():
    while True:
        try:
            main_choice = int(input("PRESS '0' FOR EXIT\nPRESS '1' FOR NEWS\n"))
        except ValueError:
            print("Invalid input! Please enter 0 or 1.")
            continue

        if main_choice == 0:
            print("\n" + "=" * 100)
            print("AAJ KI MUKHYA SAMACHAR YAHI SAMAAPT HOTI HAI !! DHANYABAAD !!")
            print("=" * 100 + "\n")
            break

        print("0. EXIT\n1. INDIAN SPORTS NEWS\n2. FOREIGN SPORTS NEWS\n3. INDIAN POLITICAL NEWS"
              "\n4. FOREIGN POLITICAL NEWS\n5. BOLLYWOOD NEWS\n6. HOLLYWOOD NEWS\n"
              "7. CREATE YOUR OWN NEWS\n8. VIEW ALL PAST NEWS")

        try:
            category_choice = int(input("PLEASE CHOOSE YOUR CATEGORY: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if category_choice == 0:
            print("\n" + "=" * 100)
            print("AAJ KI MUKHYA SAMACHAR YAHI SAMAAPT HOTI HAI !! DHANYABAAD !!")
            print("=" * 100 + "\n")
            return

        if 1 <= category_choice <= 6:
            try:
                num = int(input("ENTER HOW MANY NEWS YOU WANT TO SEE: "))
            except ValueError:
                print("Invalid number entered.")
                continue

            while num > 0:
                name = News.get_random_name(category_choice)
                if not name:
                    break
                random_thing = News.get_random_thing()
                animal = News.get_random_animal()
                movement = News.get_random_movement()
                place = News.get_random_place(category_choice)
                NewsTemplate.display_and_save_news(
                    [name, random_thing, animal, movement, place],
                    category_choice
                )
                num -= 1

        elif category_choice == 7:
            name = input("ENTER NAME: ")
            random_thing = input("ENTER ANY RANDOM THING: ")
            animal = input("ENTER ANIMAL: ")
            movement = input("WHAT THEY ARE DOING: ")
            place = input("ENTER RANDOM PLACE: ")
            details = [name, random_thing, animal, movement, place]
            OwnNews.create_your_own_news(details)
                
        elif category_choice == 8:
            try:
                with open("Saved_news.txt", "r") as file:
                    data = file.read().strip()
                    if data:
                        print(data)
                    else:
                        print("No saved news found.")
            except FileNotFoundError:
                print("Saved_news.txt not found.")
        else:
            print("ENTER VALID NUMBER.") 


if __name__ == "__main__":        
    main()
