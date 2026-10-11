import random

Vocaloid = ["Miku", "Rin", "Len", "Luka", "Kaito", "Meiko"]
Miku_songs = ["PPPP", "World is Mine", "Senbonzakura", "Tell Your World", "Rolling Girl"]
Rin_Songs = ["Meltdown", "Kokoro", "Daughter of Evil", "Iroha Uta", "Electric Angel"]
Len_Songs = ["Servant of Evil", "Fire◎Flower", "Butterfly on Your Right Shoulder", "Double Lariat", "Magnet"]
Luka_Songs = ["Dance with Me", "Heart of the City", "Rainbow", "Starlight", "Celestial"]
Kaito_Songs = ["Shadow of the Moon", "Midnight Sun", "Neon Dreams", "Electric Pulse", "Cosmic Drive"]
Meiko_Songs = ["Whisper of the Wind", "Echoes of Time", "Tidal Wave", "Stellar Glow", "Galaxy Ride"]

Vocaloid_escogido = random.choice (Vocaloid)


if Vocaloid_escogido == "Miku":
        print ("")
        print ("Opa, te salió Hatsune Miku :3.")
        print ("")
        print ("Aquí tienes algunas recomendaciones:")
        print ("")
        for i in range(len(Miku_songs)):
            print (f"{i+1}. {Miku_songs[i]}")

elif Vocaloid_escogido == "Rin":
        print ("")
        print ("Opa, te salió Kagamine Rin :3.")
        print ("")
        print ("Aquí tienes algunas recomendaciones:")
        print ("")
        for i in range(len(Rin_Songs)):
            print (f"{i+1}. {Rin_Songs[i]}")
            
    
elif Vocaloid_escogido == "Len":
        print ("")
        print ("Opa, te salió Kagamine Len :3.")
        print ("")
        print ("Aquí tienes algunas recomendaciones:")
        print ("")
        for i in range(len(Len_Songs)):
            print (f"{i+1}. {Len_Songs[i]}")
    
elif Vocaloid_escogido == "Luka":
        print ("")
        print ("Opa, te salió Megurine Luka :3.")
        print ("")
        print ("Aquí tienes algunas recomendaciones:")
        print ("")
        for i in range(len(Luka_Songs)):
            print (f"{i+1}. {Luka_Songs[i]}")


elif Vocaloid_escogido == "Kaito":
        print ("")
        print ("Opa, te salió Kaito :3.")
        print ("")
        print ("Aquí tienes algunas recomendaciones:")
        print ("")  
        for i in range(len(Kaito_Songs)):
            print (f"{i+1}. {Kaito_Songs[i]}")
    

elif Vocaloid_escogido == "Meiko":
        print ("")
        print ("Opa, te salió Meiko :3.")
        print ("")
        print ("Aquí tienes algunas recomendaciones:")
        print ("")
        for i in range(len(Meiko_Songs)):
            print (f"{i+1}. {Meiko_Songs[i]}")