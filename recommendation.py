import random

movies = {
    "happy": [
        "Zindagi Na Milegi Dobara", "Chennai Express", "3 Idiots",
        "Munna Bhai MBBS", "Hera Pheri", "Bhool Bhulaiyaa"
    ],
    "sad": [
        "Tamasha", "Rockstar", "Kabir Singh",
        "Kal Ho Naa Ho", "Sanam Teri Kasam", "Ae Dil Hai Mushkil"
    ],
    "motivated": [
        "Dangal", "MS Dhoni", "Lakshya",
        "Chak De India", "Super 30", "Mary Kom"
    ],
    "romantic": [
        "DDLJ", "Aashiqui 2", "Jab We Met",
        "Yeh Jawaani Hai Deewani", "Barfi", "Veer-Zaara"
    ],
    "thrill": [
        "Drishyam", "Andhadhun", "Kahaani",
        "Special 26", "Race", "Ek Villain"
    ]
}

print("\n\n🎭 Advanced Mood-Based Movie Recommendation System")
print("👉 Available moods: happy, sad, motivated, romantic, thrill")
print("👉 Type 'random' for surprise movie")
print("👉 Type 'search' to find similar movies")
print("👉 Type 'exit' to stop")

while True:
    user = input("\nEnter your choice: ").lower().strip()


    if user == "exit":
        print("👋 Enjoy your movie time!")
        break


    elif user == "random":
        all_movies = []
        for m_list in movies.values():
            all_movies.extend(m_list)
        print("\n🎲 Random Movie Suggestion:")
        print("👉", random.choice(all_movies))


    elif user == "search":
        name = input("Enter movie name: ").lower().strip()
        found = False

        for mood, m_list in movies.items():
            for m in m_list:
                if name == m.lower():
                    print(f"\n🎬 Because you like '{m}', try these:\n")
                    for rec in m_list:
                        if rec.lower() != name:
                            print("👉", rec)
                    found = True
                    break
            if found:
                break

        if not found:
            print("😅 Movie not found!")


    elif user in movies:
        print(f"\n🎬 Movies for '{user}' mood:\n")
        for movie in movies[user]:
            print("👉", movie)


    else:
        print("😅 Invalid input! Try again.")