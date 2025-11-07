import random
destinations={
    "beach":["maldieves","hawai","miami","kaza","mombassa"],
    "mountains":["Everest","Atlas","Atlas","kilijamro","Rocky"],
    "Cities":["paris","Casablanca","lagos","Dubai","Qatar"]
}
greeting=["hi","hello","hey"]

def chatbot():
    print("travelbot:hi!i am travelbot.type 'quit'to'exit'")
    while True:
        user=input("You:").strip().lower()
        if user=="quit":
            print("travelbot:goodbye :)")
            break
        elif any(g in user for g in greeting):
            print("travelbot:hello! do u like beaches,mountains or cities?")
        elif user in destinations:
            print(f"Travelbot:how about{random.choice(destinations[user])}?")
        elif "recommendation" or "suggestion" in user:
            category=random.choice(list(destinations.keys()))
            print(f"travelbot:i'd suggest{random.choice(destinations[category])}({category}).")
        else:
            print("travelbot:sorry i did not understand that.")
if __name__=="__main__":
    chatbot()