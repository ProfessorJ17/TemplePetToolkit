import random

# Options for Temple Pet Generator
gender_options = ["1=Male", "2=Female", "3=Other"]
zodiac_options = ["1=♈️ Aries", "2=♉️ Taurus", "3=♊️ Gemini", "4=♋️ Cancer", "5=♌️ Leo", "6=♍️ Virgo", "7=♎️ Libra", "8=♏️ Scorpio", "9=⛎ Ophiuchus", "10=♐️ Sagittarius", "11=♑️ Capricorn", "12=♒️ Aquarius", "13=♓️ Pisces"]
alignment_options = ["1=Good", "2=Evil", "3=Neutral"]
constellation_options = ["1=Andromeda 🧜‍♀️ Mermaid", "2=Apus: 🐦 Cardinal", "3=Aquila: 🦅 Eagle", "4=Camelopardalis: 🐫 Camel", "5=Canes Venatici: 🦮 Herd Dog", "6=Canis Major: 🐕 Dog", "7=Canis Minor: 🐶 Puppy", "8=Centaurus: 🐎 Man-Horse", "9=Cetus: 🐋 Whale", "10=Chamaeleon: 🦎 Chameleon", "11=Columba: 🕊️ Dove", "12=Corvus: 🐦‍⬛ Crow", "13=Crux: 🦗 Cicada/Locust", "14=Cygnus: 🦢 Swan", "15=Delphinus: 🐬 Dolphin", "16=Draco: 🐉 Dragon", "17=Equuleus: 🐴 Mule", "18=Felis: 🐈‍⬛ Black Cat", "19=Hercules: 🦍 Gorilla", "20=Hydra: 🐍 Snake", "21=Lacerta: 🐊 Crocodile", "22=Leo Minor: 🐱 Kitty", "23=Lepus: 🐇 Rabbit", "24=Lupus: 🐺 Wolf", "25=Lynx: 🐾 Lynx", "26=Monoceros: 🦄 Unicorn", "27=Musca: 🦟 Mosquito", "28=Pavo: 🦚 Peacock", "29=Phoenix: 🐦‍🔥 Phoenix", "30=Rana: 🐸 Frog", "31=Tigris: 🐅 Tiger", "32=Tucana: 🦜 Toucan", "33=Ursa Major: 🐻 Bear", "34=Ursa Minor: 🧸 Teddy Bear", "35=Volans: 𓅐 Vulture", "36=Vulpecula: 🦊 Fox"]
first_letter_options = ["1=A", "2=B", "3=C", "4=D", "5=E", "6=F", "7=G", "8=H", "9=I", "10=J", "11=K", "12=L", "13=M", "14=N", "15=O", "16=P", "17=Q", "18=R", "19=S", "20=T", "21=U", "22=V", "23=W", "24=X", "25=Y", "26=Z"]
color_options = ["1=Red", "2=Orange", "3=Yellow", "4=Chartreuse", "5=Green", "6=Spring Green", "7=Cyan", "8=Azure", "9=Blue", "10=Violet", "11=Magenta", "12=Rose", "13=Black", "14=White", "15=Gray"]
beast_options = ["1=Beast", "2=Bird", "3=Boss", "4=Bug", "5=Devil", "6=Zombie", "7=Slime", "8=Material", "9=Dragon"]
elemental_options = ["1=Grass", "2=Fire", "3=Water", "4=Lightning", "5=Psychic", "6=Fighting", "7=Darkness", "8=Metal", "9=Fairy", "10=Colorless", "11=Ice"]
type_options = ["1=Normal", "2=Poison", "3=Ground", "4=Flying", "5=Rock", "6=Ghost", "7=Steel", "8=Stellar"]
face_emoji_options = [
    "1=😀 grinning face", "2=😁 beaming face with smiling eyes", "3=😂 face with tears of joy", "4=🤣 rolling on the floor laughing",
    "5=😃 grinning face with big eyes", "6=😄 grinning face with smiling eyes", "7=😅 grinning face with sweat", "8=😆 grinning squinting face",
    "9=😉 winking face", "10=😊 smiling face with smiling eyes", "11=😋 face savoring food", "12=😎 smiling face with sunglasses",
    "13=😍 smiling face with heart-eyes", "14=😘 face blowing a kiss", "15=😗 kissing face", "16=😙 kissing face with smiling eyes",
    "17=😚 kissing face with closed eyes", "18=🤗 hugging face", "19=🤩 star-struck", "20=🤔 thinking face", "21=🤨 face with raised eyebrow",
    "22=😐 neutral face", "23=😑 expressionless face", "24=😶 face without mouth", "25=🙄 face with rolling eyes", "26=😏 smirking face",
    "27=😣 persevering face", "28=😥 sad but relieved face", "29=😮 face with open mouth", "30=🤐 zipper-mouth face", "31=😯 hushed face",
    "32=😪 sleepy face", "33=😫 tired face", "34=😴 sleeping face", "35=😌 relieved face", "36=😛 face with tongue", "37=😜 winking face with tongue",
    "38=😝 squinting face with tongue", "39=🤤 drooling face", "40=😒 unamused face", "41=😓 downcast face with sweat", "42=😔 pensive face",
    "43=😕 confused face", "44=🙃 upside-down face", "45=🤑 money-mouth face", "46=😲 astonished face", "47=☹️ frowning face",
    "48=🙁 slightly frowning face", "49=😖 confounded face", "50=😞 disappointed face", "51=😟 worried face", "52=😤 face with steam from nose",
    "53=😢 crying face", "54=😭 loudly crying face", "55=😦 frowning face with open mouth", "56=😧 anguished face", "57=😨 fearful face",
    "58=😩 weary face", "59=🤯 exploding head", "60=😬 grimacing face", "61=😰 anxious face with sweat", "62=😱 face screaming in fear",
    "63=😳 flushed face", "64=🤪 crazy face", "65=😵 dizzy face", "66=😠 angry face", "67=🤬 face with symbols on mouth", "68=😷 face with medical mask",
    "69=🤒 face with thermometer", "70=🤕 face with head-bandage", "71=🤢 nauseated face", "72=🤮 face vomiting", "73=🤧 sneezing face",
    "74=😇 smiling face with halo", "75=🤠 cowboy hat face", "76=🤡 clown face", "77=🤥 lying face", "78=🤫 shushing face", "79=🤭 face with hand over mouth",
    "80=🧐 face with monocle", "81=🤓 nerd face", "82=😈 smiling face with horns", "83=👿 angry face with horns"
]

# Define personality options globally
personality_1_options = {
    1: "WORTHWHILE", 2: "MAD", 3: "SCARED", 4: "JOYFUL", 5: "POWERFUL", 
    6: "PEACEFUL", 7: "HURT", 8: "HOSTILE", 9: "ANGRY", 10: "SELFISH", 
    11: "HATEFUL", 12: "CRITICAL", 13: "CONFUSED", 14: "REJECTED", 
    15: "HELPLESS", 16: "SUBMISSIVE", 17: "INSECURE", 18: "ANXIOUS", 
    19: "EXCITED", 20: "SENSUOUS", 21: "ENERGETIC", 22: "CHEERFUL", 
    23: "CREATIVE", 24: "HOPEFUL", 25: "AWARE", 26: "PROUD", 
    27: "RESPECTED", 28: "FAITHFUL", 29: "IMPORTANT", 30: "APPRECIATED"
}

personality_2_options = {
    1: "LOVING", 2: "TRUSTING", 3: "NURTURING", 4: "CONTENT", 
    5: "THOUGHTFUL", 6: "INTIMATE", 7: "LONELY", 8: "BORED", 
    9: "TIRED", 10: "GUILTY", 11: "ASHAMED", 12: "DEPRESSED", 
    13: "DISTANT", 14: "SARCASTIC", 15: "FRUSTRATED", 16: "JEALOUS", 
    17: "IRRITATED", 18: "SKEPTICAL", 19: "SLEEPY", 20: "THANKFUL", 
    21: "APATHETIC", 22: "ISOLATED", 23: "INFERIOR", 24: "STUPID", 
    25: "REMORSEFUL", 26: "SECURE", 27: "SERENE", 28: "RESPONSIVE", 
    29: "PENSIVE", 30: "RELAXED"
}

personality_3_options = {
    1: "BEWILDERED", 2: "DISCOURAGED", 3: "INSIGNIFICANT", 
    4: "INADEQUATE", 5: "EMBARRASSED", 6: "OVERWHELMED", 
    7: "DARING", 8: "FASCINATING", 9: "STIMULATING", 
    10: "AMUSED", 11: "PLAYFUL", 12: "OPTIMISTIC", 
    13: "SURPRISED"
}

def choose_option(options):
    for option in options:
        print(option)
    choice = input(f"Enter the number for your choice (1-{len(options)}): ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        choice = input(f"Invalid input. Please enter a number between 1 and {len(options)}: ")
    return options[int(choice) - 1].split('=')[1]

def choose_personality():
    print("\nChoose Personality Traits:")
    print("Personality 1:")
    for key, value in personality_1_options.items():
        print(f"{key}: {value}")
    personality_1 = input("Enter the number for your first personality trait (1-30): ")
    print("Personality 2:")
    for key, value in personality_2_options.items():
        print(f"{key}: {value}")
    personality_2 = input("Enter the number for your second personality trait (1-30): ")
    print("Personality 3:")
    for key, value in personality_3_options.items():
        print(f"{key}: {value}")
    personality_3 = input("Enter the number for your third personality trait (1-13): ")
    return personality_1, personality_2, personality_3

def generate_temple_pet():
    gender = choose_option(gender_options)
    zodiac = choose_option(zodiac_options)
    alignment = choose_option(alignment_options)
    constellation = choose_option(constellation_options)
    first_letter = choose_option(first_letter_options)
    color = choose_option(color_options)
    beast = choose_option(beast_options)
    elemental = choose_option(elemental_options)
    type_ = choose_option(type_options)
    face_emoji = choose_option(face_emoji_options)

    # Choose personality traits
    personality_1, personality_2, personality_3 = choose_personality()

    # Print chosen options
    print("\nChosen Options for Your Temple Pet:")
    print(f"Gender: {gender}")
    print(f"Zodiac: {zodiac}")
    print(f"Alignment: {alignment}")
    print(f"Constellation: {constellation}")
    print(f"First Letter of Name: {first_letter}")
    print(f"Color: {color}")
    print(f"Beast: {beast}")
    print(f"Elemental: {elemental}")
    print(f"Type: {type_}")
    print(f"Face Emoji: {face_emoji}")
    print("Personality Traits:", end=" ")
    print(f"{personality_1}= {personality_1_options[int(personality_1)]}, {personality_2}= {personality_2_options[int(personality_2)]}, {personality_3}= {personality_3_options[int(personality_3)]}")

# Generate temple pet
generate_temple_pet() 
