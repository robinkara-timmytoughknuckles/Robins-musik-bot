
# Lista med musik och information om varje låt
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

# Funktion som kör musik-boten
def run_music_bot():
        # Programmet fortsätter tills användaren skriver nej
    while True:
         # Går igenom alla låtar i listan
        for song in music:
            # ger värde till score och music som kommer att användas senare
            best_score = 0
            best_music = ""
            # Frågar användaren vilken genre hen vill lyssna på och vilken mood
            genre = input("What genre do you want to listen to?\n").strip().lower()
            mood = input("What mood do you want to listen to?\n(energetic, playful, reflective, aggressive, confident, ambitious, sad, upbeat, romantic, love, intense, chill)\n").strip().lower()
            #sätter score till 0
            score = 0
            # Ger poäng om genre matchar
            if song["genre"] == genre:
                score += 2  
            # Ger poäng om mood matchar
            if song["mood"] == mood:
                score += 2
            if score > best_score:
                best_score = score
                best_music = song["title"]
            # Skriver ut rekommendationen
            if best_music:
                print("Recommendation:", best_music)
            else: 
                print("Sorry, no music found matching your preferences.")
            # Frågar om användaren vill fortsätta
            user_choice= input("Do you want another recommendation? (yes/no)\n").strip().lower()
            # Avslutar programmet om användaren skriver no
            if user_choice == "no":
                print("Goodbye! Have a good day")
                break
#startar programmet      
run_music_bot()
