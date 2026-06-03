# Lista med musik och information om varje "song" 
music = [
    # --- Dave ---
    {"title": "Trojan Horse", "artist": "Dave,Central Cee", "genre": "Uk rap", "album": "Split Decision", "year": "2023","duration": "3:56", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Funky Friday", "artist": "Dave,Fredo", "genre": "Uk rap", "album": "Singel", "year": "2018", "duration": "3.02", "mood": "playful", "likes": 0, "dislikes": 0},
    {"title": "Lazarus", "artist": "Dave,Boj", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "3:24", "mood": "reflective", "likes": 0, "dislikes": 0},
    {"title": "Clash", "artist": "Dave,Stormzy", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "4:12", "mood": "aggressive", "likes": 0, "dislikes": 0},
    {"title": "Calling me out", "artist": "Dave", "genre": "Uk rap", "album": "Game Over", "year": "2017", "duration": "2:55", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "Six Paths", "artist": "Dave", "genre": "Uk rap", "album": "Six Paths", "year": "2016", "duration": "3:43", "mood": "ambitious", "likes": 0, "dislikes": 0},
    {"title": "Both Sides Of A Smile", "artist": "Dave,James Blake", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "7:52", "mood": "sad", "likes": 0, "dislikes": 0},
    {"title": "No Words", "artist": "Dave,MoStack", "genre": "Uk rap", "album": "Game Over", "year": "2017", "duration": "3:05", "mood": "upbeat", "likes": 0, "dislikes": 0},
    {"title": "The Boy Who Played The Harp", "artist": "Dave", "genre": "Uk rap", "album": "The Boy Who Played The Harp", "year": "2025", "duration": "4:29", "mood": "reflective", "likes": 0, "dislikes": 0},
    {"title": "Raindance", "artist": "Dave,Tems", "genre": "Uk rap", "album": "The Boy Who Played The Harp", "year": "2025", "duration": "3:29", "mood": "romantic", "likes": 0, "dislikes": 0},
    {"title": "Starlight", "artist": "Dave", "genre": "Uk rap", "album": "single", "year": "2022", "duration": "3:10", "mood": "love", "likes": 0, "dislikes": 0},
    {"title": "Scewface Capital", "artist": "Dave", "genre": "Uk rap", "album": "PSYCHODRAMA", "year": "2019 ", "duration": "4:03", "mood": "intense", "likes": 0, "dislikes": 0},
    {"title": "Sprinter", "artist": "Dave,Central Cee", "genre": "Uk rap", "album": "Split Decision", "year": "2023", "duration": "3:49", "mood": "playful", "likes": 0, "dislikes": 0},
    {"title": "UK Rap", "artist": "Dave,Central Cee", "genre": "Uk rap", "album": "Split Decision", "year": "2023", "duration": "3:18", "mood": "playful", "likes": 0, "dislikes": 0},
    {"title": "System", "artist": "Dave,Wizkid", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "3:01", "mood": "love", "likes": 0, "dislikes": 0},
    {"title": "Thiago Silva", "artist": "Dave,AJ Tracey", "genre": "Uk rap", "album": "Thiago Silva - Single", "year": "2016", "duration": "3:21", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Law Of Attraction", "artist": "Dave,Snoh Aalegra", "genre": "Uk rap", "album": "We're All Alone In This Together", "year": "2021", "duration": "3:01", "mood": "romantic", "likes": 0, "dislikes": 0},
    {"title": "Calling Me Out", "artist": "Dave", "genre": "Uk rap", "album": "Game Over", "year": "2017", "duration": "2:55", "mood": "playful", "likes": 0, "dislikes": 0},

    # --- Central Cee ---
    {"title": "6 For 6","artist": "Central Cee", "genre": "Uk rap", "album": "Wild West", "year": "2021", "duration": "2:08", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "One Up", "artist": "Central Cee", "genre": "Uk rap", "album": "No More Leaks", "year": "2022", "duration": "2:40", "mood": "intense", "likes": 0, "dislikes": 0},
    {"title": "Wagwan", "artist": "Central Cee", "genre": "Uk rap", "album": "All Roads Lead Home", "year": "2026", "duration": "2:07", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "Bolide Noir", "artist": "Central Cee,JRK 19", "genre": "Uk rap", "album": "Bolide Noir", "year": "2024", "duration": "2:50", "mood": "intense", "likes": 0, "dislikes": 0},

    # --- Drake ---
    {"title": "KMT","artist": "Drake,Giggs", "genre": "Hip-Hop", "album": "More Life", "year": "2017", "duration": "2:42", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Never Recover","artist": "Drake,Lil Baby,Gunna", "genre": "Hip-Hop", "album": "Drip Harder", "year": "2018", "duration": "3:00", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Over The Top", "artist": "Drake,Smiley", "genre": "Hip-Hop", "album": "Over The Top (Single)", "year": "2021", "duration": "2:33", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "First Person Shooter", "artist": "Drake,J. Cole", "genre": "Hip-Hop", "album": "For All the Dogs", "year": "2023", "duration": "4:07", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "Jimmy Cooks", "artist": "Drake,21 Savage", "genre": "Hip-Hop", "album": "Honestly, Nevermind", "year": "2022", "duration": "3:38", "mood": "aggressive", "likes": 0, "dislikes": 0},
    {"title": "Family Matters", "artist": "Drake", "genre": "Hip-Hop", "album": "Single", "year": "2024", "duration": "7:36", "mood": "aggressive", "likes": 0, "dislikes": 0},
    {"title": "Landed", "artist": "Drake", "genre": "Hip-Hop", "album": "Dark Lane Demo Tapes", "year": "2020", "duration": "2:43", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "Look Alive", "artist": "Drake,BlocBoy JB", "genre": "Hip-Hop", "album": "Simi", "year": "2018", "duration": "3:01", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Broke Boys", "artist": "Drake,21 Savage", "genre": "Hip-Hop", "album": "Her Loss", "year": "2022", "duration": "3:45", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "Free Smoke", "artist": "Drake", "genre": "Hip-Hop", "album": "More Life", "year": "2017", "duration": "3:38", "mood": "aggressive", "likes": 0, "dislikes": 0},
    {"title": "No Long Talk", "artist": "Drake,Giggs", "genre": "Hip-Hop", "album": "More Life", "year": "2017", "duration": "2:22", "mood": "aggressive", "likes": 0, "dislikes": 0},
    {"title": "National Treasure", "artist": "Drake", "genre": "Hip-Hop", "album": "ICEMAN", "year": "2026", "duration": "4:12", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "Plot Twist", "artist": "Drake", "genre": "Hip-Hop", "album": "ICEMAN", "year": "2026", "duration": "?", "mood": "intense", "likes": 0, "dislikes": 0},
    # --- Nemzzz ---
    {"title": "DILEMMA", "artist": "Nemzzz,Central Cee", "genre": "Hip-Hop", "album": "RENT'S DUE (DELUXE)", "year": "2025", "duration": "2:34", "mood": "chill", "likes": 0, "dislikes": 0},
    {"title": "Taste", "artist": "Nemzzz,D-Block Europe", "genre": "Uk rap", "album": "Single", "year": "2024", "duration": "2:45", "mood": "chill", "likes": 0, "dislikes": 0},
    {"title": "DILEMMA", "artist": "Nemzzz,Central Cee", "genre": "Hip-Hop", "album": "RENT'S DUE (DELUXE)", "year": "2025", "duration": "2:34", "mood": "chill", "likes": 0, "dislikes": 0},
    {"title": "Art", "artist": "Nemzzz,Latto", "genre": "Hip-Hop", "album": "Single", "year": "2024", "duration": "2:56", "mood": "confident", "likes": 0, "dislikes": 0},
    {"title": "Stop It", "artist": "Nemzzz", "genre": "Uk rap", "album": "DO NOT DISTURB", "year": "2024", "duration": "2:18", "mood": "chill", "likes": 0, "dislikes": 0},
    {"title": "Sample", "artist": "Nemzzz", "genre": "Uk rap", "album": "RENT'S DUE", "year": "2024", "duration": "2:09", "mood": "chill", "likes": 0, "dislikes": 0},
    {"title": "GEEKIN", "artist": "Nemzzz,Lil Yachty", "genre": "Hip-Hop", "album": "Single", "year": "2026", "duration": "?", "mood": "chill", "likes": 0, "dislikes": 0},

    # --- Gunna ---
    {"title": "Hakuna Matata", "artist": "Gunna", "genre": "Hip-Hop", "album": "Drip Season 3", "year": "2018", "duration": "3:08", "mood": "chill", "likes": 0, "dislikes": 0},
    {"title": "Drip Too Hard", "artist": "Gunna, Lil Baby", "genre": "Hip-Hop", "album": "Drip Harder", "year": "2018", "duration": "2:25", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Sold Out Dates", "artist": "Gunna,Lil Baby", "genre": "Hip-Hop", "album": "Drip Season 3", "year": "2018", "duration": "2:46", "mood": "confident", "likes": 0, "dislikes": 0},

    # --- Giggs ---
    {"title": "Straight Murder", "artist": "Giggs,Dave", "genre": "Uk rap", "album": "Now Or Never", "year": "2013", "duration": "3:36", "mood": "aggressive", "likes": 0, "dislikes": 0},
    {"title": "Incredible Sauce", "artist": "Giggs,Dave", "genre": "Uk rap", "album": "Zero Tolerance", "year": "2023", "duration": "4:03", "mood": "intense", "likes": 0, "dislikes": 0},
    {"title": "Man Don't Care", "artist": "Giggs,Drake", "genre": "Uk rap", "album": "Landlord", "year": "2016", "duration": "3:28", "mood": "confident", "likes": 0, "dislikes": 0},

    #--- Roddy Rich ---
    {"title": "The Box", "artist": "Roddy Ricch", "genre": "Hip-Hop", "album": "Please Excuse Me for Being Antisocial", "year": "2019", "duration": "3:16", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Feed the Streets 2 (Intro)", "artist": "Roddy Ricch", "genre": "Hip-Hop", "album": "Feed Tha Streets II", "year": "2018", "duration": "2:50", "mood": "reflective", "likes": 0, "dislikes": 0},
    {"title": "Ballin'", "artist": "Roddy Ricch", "genre": "Hip-Hop", "album": "Perfect Ten", "year": "2019", "duration": "3:50", "mood": "confident", "likes": 0, "dislikes": 0},

    #--- Travis Scott ---
    {"title": "Escape Plan", "artist": "Travis Scott", "genre": "Hip-Hop", "album": "Single", "year": "2021", "duration": "2:29", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Sicko Mode", "artist": "Travis Scott,Drake", "genre": "Hip-Hop", "album": "Astroworld", "year": "2018", "duration": "5:12", "mood": "energetic", "likes": 0, "dislikes": 0},
    {"title": "Kick Out", "artist": "Travis Scott", "genre": "Hip-Hop", "album": "JACKBOYS 2", "year": "2025", "duration": "2:50", "mood": "energetic", "likes": 0, "dislikes": 0},
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

        # Sort songs by likes and dislikes
        # Songs with more likes appear first
        # Songs with more dislikes appear last
        # This creates a ranking: likes - dislikes (higher score = better recommendation)
        #I used co pilot for this part and from what I learend it that the lambda function is a way to sort the songs based on their likes and dislikes.
        scored_songs.sort(key=lambda song: song["likes"] - song["dislikes"], reverse=True)

        # Show the recommendations after checking all songs
        top3 = scored_songs[:3]

        if top3:
            print("Recommendations:")

            # Print the top 3 songs with likes and dislikes
            for song in top3:
                print(f"{song['title']} by {song['artist']} (Likes: {song['likes']}, Dislikes: {song['dislikes']})")

        else:
            print("Sorry, no music found matching your preferences.")

        # Ask the user if they liked the recommendations
        liked_music = input("Did you like these recommendations? (yes/no)\n").strip().lower()

        # If the user liked the songs, increase their likes score
        if liked_music == "yes":
            # Increase likes for all recommended songs
            for song in top3:
                song["likes"] += 1
                print(f"{song['title']} by {song['artist']} likes increased to {song['likes']}")

            print("Great! The program remembered your preferences.")

        # If the user disliked the songs, increase their dislikes score
        elif liked_music == "no":
            # Increase dislikes for all recommended songs
            for song in top3:
                song["dislikes"] += 1
                print(f"{song['title']} by {song['artist']} dislikes increased to {song['dislikes']}")

            print("Okay! The program will try different songs next time.")

        # Ask if the user wants another recommendation
        user_choice = input("Do you want another recommendation? (yes/no)\n").strip().lower()

        # Exit the program if the user says no
        if user_choice == "no":
            print("Goodbye! Have a good day")
            break

# Start the program
run_music_bot()
