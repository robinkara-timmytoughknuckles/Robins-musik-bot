genre = input("What genre do you want to listen to?\n").strip().lower()
mood = input("What mood do you want to listen to?\n(energetic, playful, reflective, aggressive, confident, ambitious, sad, upbeat, romantic, love, intense, chill)\n").strip().lower()

music = [
    # --- Dave ---
    {"title": "Trojan Horse", "artist": "Dave,Central Cee", "genre": "Hip-Hop", "album": "Split Decision", "year": "2023","duration": "3:56", "mood": "energetic"},
    {"title": "Funky Friday", "artist": "Dave,Fredo", "genre": "Uk rap", "album": "Singel", "year": "2018", "duration": "3.02", "mood": "playful"},
    {"title": "Lazarus", "artist": "Dave,Boj", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "3:24", "mood": "reflective"},
    {"title": "Clash", "artist": "Dave,Stormzy", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "4:12", "mood": "aggressive"},
    {"title": "Calling me out", "artist": "Dave", "genre": "Hip-Hop", "album": "Game Over", "year": "2017", "duration": "2:55", "mood": "confident"},
    {"title": "Six Paths", "artist": "Dave", "genre": "Uk rap", "album": "Six Paths", "year": "2016", "duration": "3:43", "mood": "ambitious"},
    {"title": "Both Sides Of A Smile", "artist": "Dave,James Blake", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "7:52", "mood": "sad"},
    {"title": "No Words", "artist": "Dave,MoStack", "genre": "Uk rap", "album": "Game Over", "year": "2017", "duration": "3:05", "mood": "upbeat"},
    {"title": "The Boy Who Played The Harp", "artist": "Dave", "genre": "Uk rap", "album": "The Boy Who Played The Harp", "year": "2025", "duration": "4:29", "mood": "reflective"},
    {"title": "Raindance", "artist": "Dave,Tems", "genre": "Uk rap", "album": "The Boy Who Played The Harp", "year": "2025", "duration": "3:29", "mood": "romantic"},
    {"title": "Starlight", "artist": "Dave", "genre": "Uk rap", "album": "single", "year": "2022", "duration": "3:10", "mood": "love"},
    {"title": "Scewface Capital", "artist": "Dave", "genre": "Uk rap", "album": "PSYCHODRAMA", "year": "2019 ", "duration": "4:03", "mood": "intense"},

    # --- Central Cee ---
    {"title": "6 For 6","artist": "Central Cee", "genre": "Uk rap", "album": "Wild West", "year": "2021", "duration": "2:08", "mood": "confident"},

    # --- Drake ---
    {"title": "KMT","artist": "Drake,Giggs", "genre": "Hip-Hop", "album": "More Life", "year": "2017", "duration": "2:42", "mood": "energetic"},
    {"title": "Never Recover","artist": "Lil Baby,Gunna,Drake", "genre": "Hip-Hop", "album": "Drip Harder", "year": "2018", "duration": "3:00", "mood": "energetic"},

    # --- Nemzzz ---
    {"title": "DILEMMA", "artist": "Nemzzz,Central Cee", "genre": "Hip-Hop", "album": "RENT'S DUE (DELUXE)", "year": "2025", "duration": "2:34", "mood": "chill"},
]

def run_music_bot():
    best_score = 0
    best_music = ""

    while True:
        for music in music:
            score = 0
            if music["genre"] == genre:
                score += 2
            if music["mood"] == mood:
                score += 2
            if score > best_score:
                best_score = score
                best_music = music["title"]
        print("Recommendation:", best_music)
        break



#run_jadgpt function is the main function that runs the chatbot, it welcomes the user and then enters a loop where it takes user input and finds a response until the user says a farewell word, at which point it says goodbye and exits the loop
#def run_Jadgpt():
 #   print("=" * 50)
  #  print("Welcome to JadGPT! Type 'exit' to quit.")
   # print("=" * 50)
   #
#    farewell_words = ["exit", "quit", "goodbye", "bye", "see you later", "farewell","later", "cya", "see ya", "peace out", "take care"]
#
 #   while True:
  #      user_input = input("\nYou: ").strip()
   #     
    #    if not user_input:
     #       continue
     #
   #     response = find_response(user_input)
   #
       # if response is not None:
        #    print(f"\nJadGPT: {response}")

       # if any(word in user_input.lower() for word in farewell_words):
        #    print("\nJadGPT: Goodbye! Have a great day!")
         #   break
#if __name__ == "__main__":
    #start the chatbot
 #   run_Jadgpt()