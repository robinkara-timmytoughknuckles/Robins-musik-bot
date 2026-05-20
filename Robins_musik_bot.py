# Lista med musik och information om varje "song"
music = [
    # --- Dave ---
    {"title": "Trojan Horse", "artist": "Dave,Central Cee", "genre": "Uk rap", "album": "Split Decision", "year": "2023","duration": "3:56", "mood": "energetic"},
    {"title": "Funky Friday", "artist": "Dave,Fredo", "genre": "Uk rap", "album": "Singel", "year": "2018", "duration": "3.02", "mood": "playful"},
    {"title": "Lazarus", "artist": "Dave,Boj", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "3:24", "mood": "reflective"},
    {"title": "Clash", "artist": "Dave,Stormzy", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "4:12", "mood": "aggressive"},
    {"title": "Calling me out", "artist": "Dave", "genre": "Uk rap", "album": "Game Over", "year": "2017", "duration": "2:55", "mood": "confident"},
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

# Function that runs the music bot
def run_music_bot():
    # The program continues until the user types "no"
    while True:
        # Ask the user ONCE for their preferences (MOVED OUTSIDE the for loop)
        genre = input("What genre do you want to listen to?\n").strip().lower()
        mood = input("What mood do you want to listen to?\n(energetic, playful, reflective, aggressive, confident, ambitious, sad, upbeat, romantic, love, intense, chill)\n").strip().lower()
        
        recommendations = 0

        # Initialize best_score and best_music ONCE before checking all songs
        best_score = 0
        best_music = ""
        
        # Now search through ALL songs in the music list
        for song in music:
            # Start score at 0 for each song
            score = 0
            
            # Give points if genre matches
            if song["genre"].lower() == genre:
                score += 2
            
            # Give points if mood matches
            if song["mood"].lower() == mood:
                score += 2
            
            # Keep track of the song with the highest score
            if score >= 2:
                best_score = score
                best_music = song["title"]
                recommendations += 1
        # Show the recommendation after checking ALL songs
        if best_music:
            print("Recommendation:", best_music)
        else:
            print("Sorry, no music found matching your preferences.")
        
        # Ask the user if they want another recommendation
        user_choice = input("Do you want another recommendation? (yes/no)\n").strip().lower()
        
        # Exit the program if the user says "no"
        if user_choice == "no":
            print("Goodbye! Have a good day")
        if recommendations == 3:
            break

# Start the program
run_music_bot()
