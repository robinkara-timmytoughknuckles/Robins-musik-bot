# Lista med musik och information om varje "song"
music = [
    # --- Dave ---
    {"title": "Trojan Horse", "artist": "Dave,Central Cee", "genre": "Uk rap", "album": "Split Decision", "year": "2023","duration": "3:56", "mood": "energetic", "likes": 0},
    {"title": "Funky Friday", "artist": "Dave,Fredo", "genre": "Uk rap", "album": "Singel", "year": "2018", "duration": "3.02", "mood": "playful", "likes": 0},
    {"title": "Lazarus", "artist": "Dave,Boj", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "3:24", "mood": "reflective", "likes": 0},
    {"title": "Clash", "artist": "Dave,Stormzy", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "4:12", "mood": "aggressive", "likes": 0},
    {"title": "Calling me out", "artist": "Dave", "genre": "Uk rap", "album": "Game Over", "year": "2017", "duration": "2:55", "mood": "confident", "likes": 0},
    {"title": "Six Paths", "artist": "Dave", "genre": "Uk rap", "album": "Six Paths", "year": "2016", "duration": "3:43", "mood": "ambitious", "likes": 0},
    {"title": "Both Sides Of A Smile", "artist": "Dave,James Blake", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "7:52", "mood": "sad", "likes": 0},
    {"title": "No Words", "artist": "Dave,MoStack", "genre": "Uk rap", "album": "Game Over", "year": "2017", "duration": "3:05", "mood": "upbeat", "likes": 0},
    {"title": "The Boy Who Played The Harp", "artist": "Dave", "genre": "Uk rap", "album": "The Boy Who Played The Harp", "year": "2025", "duration": "4:29", "mood": "reflective", "likes": 0},
    {"title": "Raindance", "artist": "Dave,Tems", "genre": "Uk rap", "album": "The Boy Who Played The Harp", "year": "2025", "duration": "3:29", "mood": "romantic", "likes": 0},
    {"title": "Starlight", "artist": "Dave", "genre": "Uk rap", "album": "single", "year": "2022", "duration": "3:10", "mood": "love", "likes": 0},
    {"title": "Scewface Capital", "artist": "Dave", "genre": "Uk rap", "album": "PSYCHODRAMA", "year": "2019 ", "duration": "4:03", "mood": "intense", "likes": 0},

    # --- Central Cee ---
    {"title": "6 For 6","artist": "Central Cee", "genre": "Uk rap", "album": "Wild West", "year": "2021", "duration": "2:08", "mood": "confident", "likes": 0},

    # --- Drake ---
    {"title": "KMT","artist": "Drake,Giggs", "genre": "Hip-Hop", "album": "More Life", "year": "2017", "duration": "2:42", "mood": "energetic", "likes": 0},
    {"title": "Never Recover","artist": "Lil Baby,Gunna,Drake", "genre": "Hip-Hop", "album": "Drip Harder", "year": "2018", "duration": "3:00", "mood": "energetic", "likes": 0},

    # --- Nemzzz ---
    {"title": "DILEMMA", "artist": "Nemzzz,Central Cee", "genre": "Hip-Hop", "album": "RENT'S DUE (DELUXE)", "year": "2025", "duration": "2:34", "mood": "chill", "likes": 0},
]

# Function that runs the music bot
def run_music_bot():

    # The program continues until the user types "no"
    while True:

        # Ask the user ONCE for their preferences
        genre = input("What genre do you want to listen to?\n").strip().lower()

        mood = input(
            "What mood do you want to listen to?\n"
            "(energetic, playful, reflective, aggressive, confident, ambitious, sad, upbeat, romantic, love, intense, chill)\n"
        ).strip().lower()

        recommendations = 0

        # Initialize variables before checking songs
        best_score = 0
        best_music = ""

        # List to keep track of matching songs (now stores FULL song dictionaries)
        scored_songs = []

        # Search through songs in the music list
        for song in music:

            # Start score at 0 for each song
            score = 0

            # Give points if genre matches
            if song["genre"].lower() == genre:
                score += 2

            # Give points if mood matches
            if song["mood"].lower() == mood:
                score += 2

            # Add matching FULL song to the list (not just title)
            if score > 0:
                scored_songs.append(song)

        # Sort songs by likes from highest to lowest
        # Songs the user liked before will appear first
        scored_songs.sort(key=lambda song: song["likes"], reverse=True)

        # Show the recommendations after checking ALL songs
        top3 = scored_songs[:3]

        if top3:
            print("Recommendations:")

            # Print the top 3 songs (now accessing title from song dictionary)
            for song in top3:
                print(f"{song['title']} (Likes: {song['likes']})")

        else:
            print("Sorry, no music found matching your preferences.")

        # Ask the user if they liked the recommendations
        liked_music = input("Did you like these recommendations? (yes/no)\n").strip().lower()

        # If the user liked the songs, increase their likes score
        if liked_music == "yes":
            # Increase likes for all recommended songs
            for song in top3:
                song["likes"] += 1
                print(f"{song['title']} likes increased to {song['likes']}")

            print("Great! The program remembered your preferences.")

        else:
            print("Okay! The program will try different songs next time.")

        # Ask if the user wants another recommendation
        user_choice = input("Do you want another recommendation? (yes/no)\n").strip().lower()

        # Exit the program if the user says no
        if user_choice == "no":
            print("Goodbye! Have a good day")
            break

# Start the program
run_music_bot()
