"""
import random

def is_chest_found():
    possibilities = ["chest", "nothing found"]
    result = random.choices(possibilities, [60, 40])
    return result

def chest_color():
    possibilities = ["zielona", "pomarańczowa", "fioletowa", "złota"]
    result = random.choices(possibilities, [75, 20, 4, 1])
    return result


def gold_amount(chest_color):
    if chest_color == "zielona":
        print("Znalazałeś 1000 jednostek złota!")
        return 1000
    elif chest_color == "pomarańczowa":
        print("Znalazłeś 4000 jednostek złota!")
        return 4000
    elif chest_color == "fioletowa":
        print("Znalazłeś 9000 jednostek złota!")
        return 9000
    else:
        print("Znalazłeś 16000 jednostek złota!")
        return 16000

moves = 0
gold_sum = 0

while moves < 5:
    moves += 1
    is_chest_founded = is_chest_found()
    if "chest" in is_chest_founded:
        founded_color = chest_color()
        if "zielona" in founded_color:
            gold_sum += gold_amount("zielona")
        elif "pomarańczowa" in founded_color:
            gold_sum += gold_amount("pomarańczowa")
        elif "fioletowa" in founded_color:
            gold_sum += gold_amount("fioletowa")
        else:
            gold_sum += gold_amount("złota")
    else:
        print("W tym ruchu nic nie znaleziono...")

print("Suma znalezionego złota w tej grze to: ", gold_sum)
            
"""        
import random
from enum import Enum

def approximate_reward_value(value, percent_range):
    lowest_value = int(value - (percent_range / 100) * value)
    highest_value = int(value + (percent_range / 100) * value)
    return random.randint(lowest_value, highest_value)

Event = Enum("Event", ["Chest", "Nothing"])

events_dictionary = {
                      Event.Chest : 0.6,
                      Event.Nothing : 0.4
                      }

event_list = list(events_dictionary.keys())
event_probability = list(events_dictionary.values())

Color = Enum("Color", {"Green" : "Green",
                       "Orange" : "Orange",
                       "Purple": "Purple",
                       "Gold": "Gold"
                       })

colors_dictionary = {
                      Color.Green : 0.75,
                      Color.Orange : 0.2,
                      Color.Purple : 0.04,
                      Color.Gold : 0.01
                      }

color_list = list(colors_dictionary.keys())
color_probability = list(colors_dictionary.values())

"""
reward_dictionary = {
                     Color.Green : 1000,
                     Color.Orange : 4000,
                     Color.Purple : 9000,
                     Color.Gold : 16000
                     }
"""

reward_dictionary = {color_list[reward]: (reward + 1)**2 * 1000
                    for reward in range(len(color_list))
                      }
#print(reward_dictionary)



game_lenght = 5
gold_aquired = 0


print("Welcome in my game called KOMNATA")
print("""You have 5 steps to make.
See how much gold you can aquire!""")
while game_lenght > 0:
    answear = input("Do you want to move forward? ")
    if answear == "yes":
        print("Ok, let's see what you got...")
        drawn_event = random.choices(event_list, event_probability)[0]
        if drawn_event == Event.Chest:
            print("You have drawned a chest")
            drawn_color = random.choices(color_list, color_probability)[0]
            print("Color of your chest is:", drawn_color.value)
            gamer_reward = approximate_reward_value(reward_dictionary[drawn_color], 10)
            print("You aquired", gamer_reward, "gold.")
            gold_aquired += gamer_reward
        elif drawn_event == Event.Nothing:
            print("This time you found nothing...")
    else:
        print("You don't have any other options, just type that yes")
        continue
    game_lenght -= 1
print("Totally you aquired", gold_aquired, "gold.")





    
