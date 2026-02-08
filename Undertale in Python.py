#!/usr/bin/env python3
# Undertale Text Adventure Fork - Multilingual Edition
# Made with love for game modding enthusiasts

import sys
import time

# Language selection
print("Language/Language (EN/RU):")
lang_choice = input().strip().upper()
if lang_choice not in ["EN", "RU"]:
    lang_choice = "EN"

# Complete multilingual dialogue system
TEXTS = {
    "EN": {
        "name_prompt": "Name the fallen human:",
        "name_chara": "*The true name echoes in the dark.*",
        "name_flowey": "???: 'Don't try anything funny, you clown!'",
        "name_toriel": "???: '*gasp* I am shocked, my child.'",
        "name_jack": "Jack: 'Are you the creator? Heh, neat!'",
        "name_elliot": "Elliot: 'I am da main tester! Fear me!'",
        "name_gaster": "*Gaster was never here.*",
        "name_sans": "???: 'hey kid... wanna have a *bad time?*'",
        "confirm_name": "Are you sure? (Yes/No)",
        "final_chance": "Final chance! Choose wisely:",
        "wake_up": "*You awaken slowly... golden flowers cushion your fall.*\nThe cavern air tastes like dust and echoes.\n'{name}...' — a whisper in the stone? No, just imagination.\nYour back SCREAMS in pain, but petal-soft comfort fights the cold.\nAbove — impossible hole to surface world. Below — endless dark.\nSomething watches. Something hungry.",
        "get_up": "Get up? The fall hurt bad... (Yes/No)",
        "died_laziness": "*You lie forever on golden flowers...*\nYOU DIED. Cause: Eternal Laziness.",
        "enter_room": "*You stagger through massive stone archway.*\nA single sunflower sways in purple gloom.",
        "examine": "Examine the flower? (Yes/No)",
        "dont_run": "Voice whispers: 'Don't run away, {name}...'",
        "flowey_intro": "*step step... crinkle...*\nThe sunflower TURNS. Eyes black, teeth SHARP, smile WRONG.\n\"Howdy!\" — voice syrup-sweet, razor-edged.\n\"I'm FLOWEY! FLOW-EY! FLOW-EY THE FLOWER~♪\"\nPetals quiver. Dirt shifts beneath.\n\"You're new... FRESH... *deliciously* new...\"",
        "flowey_love": "\"Howdy, sunshine! New to the UNDERGROUND?\"\n\"*giggle* Someone REALLY oughta teach you how things WORK~\"\n\"Lucky for you... *I* know EVERYTHING!\"\n\"Ready for your WELCOME PARTY?\"\n*dirt explodes* FRIENDSHIP PELLETS! (¬‿¬)",
        "battle_system": "*Your chest BURSTS — red HEART hovers, trembling.*\n\"See that HEART? Very cute!\"\n\"That's your SOUL — culmination of your BEING!\"\n\"Down here, LOVE is DELIVERED... *differently.*\"\nFlowey's grin splits his face in half.\n\"Don't worry! You'll LOVE getting LOVE!\"",
        "pellets_fly": "WHITE PELLETS sprinkle around you!\n\"Here, catch some LOVE!\"\nThe pellets bounce toward you...",
        "dodge_prompt": "Dodge the 'friendship'? (Yes/No)",
        "know_too_much": "\"*eyes narrow* You know what's going on here, don't you?\"\n\"To think YOU were them... how STUPID of me!\"",
        "pellets_hit": "*Pellets SMASH into you!* HP now:",
        "died_pellets": "YOU DIED. Cause: 'Friendly' pellets.",
        "flowey_die": "\"You IDIOT! Who passes up FREE LOVE?!\"\n\"DIE! DIE! *DIE!*\"",
        "toriel_save": "*WHOOSH!* Fireball SLAMS ground! Flowers ash.",
        "toriel_dramatic": "Flowey SCREAMS — pixelated death-shriek — GONE.\n*thud thud* Heavy steps. Goat-height shadow.\n\"What HORROR! What FOUL creature DARE...\"\n\"...torture such poor, innocent YOUTH?!\"\nWarm paws lift you. Smells like butterscotch.\n\"Fear not, my child. TORIEL protects Ruins.\"",
        "toriel_heal": "*Toriel's paws glow warm.* HP restored:",
        "follow_toriel": "Follow Toriel to safety? (Yes/No)",
        "bad_choice": "Toriel sobs and vanishes into shadows.\nFlowey returns: 'Time to kill fake Frisk!'\n*Ground rumbles... reality glitches*\nJack: 'YOU DEAD, SON! Cause: Bad choice.'",
        "spike_puzzle": "*Sharp iron spikes block purple hall.*\n\"Look, child! A simple puzzle.\"\n\"Stay behind me — it's dangerous!\"\nTry alone anyway? (Yes/No)",
        "died_spikes": "*SPIKES pierce flesh.*\nYOU DIED. Cause: SPIKES, IDIOT!",
        "hallway_test": "\"Now, a test of independence!\"\n\"Walk this hallway alone. Simple, yes?\"\nToriel dashes ahead. Follow? (Yes/No)",
        "died_boredom": "*Footsteps echo... echo... echo...*\n*2 years later... 1 eternity later...*\nYOU DIED. Cause: Terminal Boredom.",
        "froggit_battle": "*HOP HOP SPLAT!* Green blob jiggles toward you.\n\"Froggit\" floats above — confused blinking eyes.\n*RIBBIT...?* (doesn't seem hostile... yet)\n\"Croak... human...? *stomach rumble*\"\nBATTLE MODE! SOUL locked!\n[Fight/Act/Mercy]",
        "fight_win": "*FIST SMASH!* Froggit explodes into glitter!\n*+3 EXP gained.* It flees crying.",
        "act_win": "*You croak back.* Froggit confused, hops away.\n*+1 EXP.* Peaceful resolution.",
        "mercy_win": "*You offer friendship.* Froggit blushes, leaves.\n*No EXP.* Pure pacifist.",
        "bad_battle": "*Froggit tongue-lash!* You take massive damage!\nYOU DIED. Cause: Bad battle choice.",
        "jack_interrupt": "*GLITCH SOUND* Reality breaks!\n\"Heya, {name}! Jack here. Seventh download?\"\n\"Play Undertale Fight Simulator — GitHub link!\"\n\"Don't trust flower, goat, or me. *maniac laugh*\"",
        "toriel_home": "*Cozy firelight. Smells like pie.*\n\"Welcome home, child... but stay forever safe.\"\nToriel smiles nervously.",
        "continue_sans": "END? Or find Sans for bad time? (Yes/No)",
        "sans_badtime": "*Purple hallway. Bones everywhere.*\nSans: 'hey kid... *bad time?*'\n*KRUSHT.* REAL END.",
        "jack_end": "Jack: 'Smart choice. Maybe I'll update this... maybe.'\n*Screen flickers mysteriously.*",
        "game_end": "THE END\n(Fork Edition - Modder's Cut)"
    },
    "RU": {
        "name_prompt": "Назови упавшего человека:",
        "name_chara": "*Истинное имя эхом отдаётся во тьме.*",
        "name_flowey": "???: 'Не шути так, клоун!'",
        "name_toriel": "???: '*ахинею* Я в шоке, дитя моё.'",
        "name_jack": "Jack: 'Ты создатель? Хех, прикольно!'",
        "name_elliot": "Elliot: 'Я главный тестер! Бойся меня!'",
        "name_gaster": "*Gaster никогда здесь не был.*",
        "name_sans": "???: 'эй, мелкий... хочешь *плохое время?*'",
        "confirm_name": "Точно? (Да/Нет)",
        "final_chance": "Последний шанс! Выбирай мудро:",
        "wake_up": "*Ты приходишь в себя... золотые цветы смягчили падение.*\nВоздух пещеры — пыльный, эхом отдаётся.\n'{name}...' — шёпот в камне? Нет, показалось.\nСпина ВОПИТ от боли, лепестки борются со стужей.\nНаверху — дыра к миру. Внизу — бездна тьмы.\nКто-то смотрит. Кто-то голодный.",
        "get_up": "Встать? Падение было болезненным... (Да/Нет)",
        "died_laziness": "*Ты лежишь вечно на золотых цветах...*\nТЫ УМЕР. Причина: Вечная Лень.",
        "enter_room": "*Ты шатаешься через массивную каменную арку.*\nОдинокий подсолнух качается в фиолетовой мгле.",
        "examine": "Осмотреть цветок? (Да/Нет)",
        "dont_run": "Голос шепчет: 'Не убегай, {name}...'",
        "flowey_intro": "*шаг шаг... хруст...*\nПодсолнух ПОВОРАЧИВАЕТСЯ. Глаза чёрные, зубы ОСТРЫЕ, улыбка НЕ ТАК.\n\"Приветик!\" — голос сладкий, как патока с бритвой.\n\"Я FLOWEY! FLOW-EY! FLOWEEEEEY ЦВЕТОЧЕЕЕК~♪\"\nЛепестки дрожат. Земля шевелится.\n\"Ты новенький... СВЕЖИЙ... *вкусный* новенький...\"",
        "flowey_love": "\"Эй, солнышко! Первый раз в ПОДЗЕМЕЛЬЕ?\"\n\"*хихи* Тебе ОЧЕНЬ-ОЧЕНЬ нужно знать правила!~\"\n\"Повезло тебе... *Я* знаю ВСЁ!\"\n\"Готов к ВЕЧЕРИНКЕ-ПРИВЕТСТВИЮ?\"\n*земля взрывается* ШАРИКИ ДРУЖБЫ! (¬‿¬)",
        "battle_system": "*ГРУДЬ разрывается — красное СЕРДЦЕ парит, дрожит.*\n\"Видишь это СЕРДЦЕ? Каааак миленько!\"\n\"Это твоя ДУША — вся СУТЬ твоего существования!\"\n\"У нас ЛЮБОВЬ передаётся... *по-другому.*\"\nУлыбка Flowey разрывает лицо пополам.\n\"Не бойся! Тебе ПОНРАВИТСЯ получать ЛЮБОВЬ!\"",
        "pellets_fly": "Белые шарики сыплются вокруг!\n\"Держи ЛЮБВИ!\"\nШарики прыгают к тебе...",
        "dodge_prompt": "Уклониться от 'дружбы'? (Да/Нет)",
        "know_too_much": "\"*глаза сужаются* Ты знаешь, что здесь происходит, верно?\"\n\"Думать, что ТЫ — это они... какая глупость с моей стороны!\"",
        "pellets_hit": "*Шарики СМАРЫВАЮТ тебя!* HP теперь:",
        "died_pellets": "ТЫ УМЕР. Причина: 'Дружеские' шарики.",
        "flowey_die": "\"Дурак! Кто отказывается от БЕСПЛАТНОЙ ЛЮБВИ?!\"\n\"УМИРАЙ! УМИРАЙ! *УМИРАЙ!*\"",
        "toriel_save": "*ШУУУХ!* Огненный шар БЬЁТ в землю! Цветы — пепел.",
        "toriel_dramatic": "Flowey ВИЗЖИТ — пиксельная агония — ИСЧЕЗ.\n*тук тук* Тяжёлые шаги. Тень козы.\n\"Какой УЖАС! Какая ПОДЛАЯ тварь посмела...\"\n\"...мучить бедное, невинное ДИТЯ?!!\"\nТёплые лапы поднимают. Запах ириса.\n\"Не бойся, дитя. TORIEL охраняет Руины.\"",
        "toriel_heal": "*Лапы Toriel светятся теплом.* HP восстановлен:",
        "follow_toriel": "Следовать за Toriel в безопасность? (Да/Нет)",
        "bad_choice": "Toriel рыдает и исчезает в тенях.\nВозвращается Flowey: 'Пора убить фальшивого Фриска!'\n*Земля дрожит... реальность глючит*\nJack: 'ТЫ МЁРТВ, СЫН! Причина: Плохой выбор.'",
        "spike_puzzle": "*Острые железные шипы блокируют фиолетовый зал.*\n\"Смотри, дитя! Простая головоломка.\"\n\"Иди за мной — опасно!\"\nПопробовать самому? (Да/Нет)",
        "died_spikes": "*ШИПЫ пронзают плоть.*\nТЫ УМЕР. Причина: ШИПЫ, ИДИОТ!",
        "hallway_test": "\"Теперь тест на независимость!\"\n\"Пройди этот коридор один. Просто, да?\"\nToriel убегает вперёд. Следовать? (Да/Нет)",
        "died_boredom": "*Шаги эхом... эхом... эхом...*\n*2 года спустя... 1 вечность спустя...*\nТЫ УМЕР. Причина: Терминальная Скука.",
        "froggit_battle": "*ПРЫГ ПРЫГ ХЛЯП!* Зелёная лягушка прыгает.\n\"Froggit\" парит — растерянные моргающие глаза.\n\"Квааа...?\" (не выглядит враждебным... пока)\n\"Кррок... человек...? *брюхо урчит*\"\nБОЕВАЯ СИСТЕМА! ДУША заблокирована!\n[Драка/Действие/Пощадить]",
        "fight_win": "*КУЛАК СМАРЫВАЕТ!* Froggit взрывается блёстками!\n*+3 ОПЫТА.* Убегает плача.",
        "act_win": "*Ты квакнешь в ответ.* Froggit в шоке, прыгает прочь.\n*+1 ОПЫТ.* Мирное разрешение.",
        "mercy_win": "*Ты предлагаешь дружбу.* Froggit краснеет, уходит.\n*Без ОПЫТА.* Чистый пацифист.",
        "bad_battle": "*Язык Froggit хлещет!* Массивный урон!\nТЫ УМЕР. Причина: Плохой выбор боя.",
        "jack_interrupt": "*ГЛЮЧНЫЙ ЗВУК* Реальность ломается!\n\"Эй, {name}! Это Джек. Седьмой запуск?\"\n\"Играй Undertale Fight Simulator — GitHub!\"\n\"Не верь цветку, козе, мне. *маньячный смех*\"",
        "toriel_home": "*Тёплый свет камина. Пахнет пирогом.*\n\"Добро пожаловать домой, дитя... оставайся вечно в безопасности.\"\nToriel нервно улыбается.",
        "continue_sans": "КОНЕЦ? Или найти Sans для плохого времени? (Да/Нет)",
        "sans_badtime": "*Фиолетовый коридор. Кости повсюду.*\nSans: 'эй, мелкий... *плохое время?*'\n*KRUSHT.* НАСТОЯЩИЙ КОНЕЦ.",
        "jack_end": "Jack: 'Умный выбор. Может обновлю... может.'\n*Экран мерцает загадочно.*",
        "game_end": "КОНЕЦ\n(Форк - Версия Моддера)"
    }
}

# Game state
texts = TEXTS[lang_choice]
MaxHP = 20
HP = MaxHP

# Name selection with special reactions
print(texts["name_prompt"])
Name = input().strip()

if Name == "Chara":
    print(texts["name_chara"])
    time.sleep(1)
elif Name == "Flowey":
    print(texts["name_flowey"])
elif Name == "Toriel":
    print(texts["name_toriel"])
elif Name == "Jack":
    print(texts["name_jack"])
elif Name == "Elliot":
    print(texts["name_elliot"])
elif Name in ["G", "Gaster"]:
    print(texts["name_gaster"])
    sys.exit(0)
elif Name == "Sans":
    print(texts["name_sans"])
    HP = 0

# Name confirmation
print(texts["confirm_name"])
if input().strip().lower() in ["no", "нет", "н"]:
    print(texts["final_chance"])
    Name = input().strip()

# Game start - Ruins awakening
print("\n" + texts["wake_up"].format(name=Name))
time.sleep(2)
print(texts["get_up"])
if input().strip().lower() in ["no", "нет", "н"]:
    print("\n" + texts["died_laziness"])
    input("\nPress Enter to exit...")
    sys.exit(0)

print(texts["enter_room"])
time.sleep(1)
print(texts["examine"])
if input().strip().lower() in ["no", "нет", "н"]:
    print("\n" + texts["dont_run"].format(name=Name))

# Flowey encounter - tutorial boss
print("\n" + texts["flowey_intro"])
time.sleep(3)
print(texts["flowey_love"])
time.sleep(2)
print(texts["battle_system"])
time.sleep(2)
print(texts["pellets_fly"])
print(texts["dodge_prompt"])
choice = input().strip().lower()

if choice in ["yes", "да", "д", "y"]:
    print("\n" + texts["know_too_much"])
    time.sleep(2)
else:
    print("\n" + texts["pellets_hit"], HP - 10)
    HP -= 10
    if HP <= 0:
        print(texts["died_pellets"])
        input("\nPress Enter to exit...")
        sys.exit(0)

print(texts["flowey_die"])
time.sleep(1)

# Toriel rescue
print(texts["toriel_save"])
time.sleep(1)
print(texts["toriel_dramatic"])
time.sleep(2)
if HP < MaxHP:
    print(texts["toriel_heal"], MaxHP)
    HP = MaxHP

# Follow or die
print(texts["follow_toriel"])
if input().strip().lower() in ["no", "нет", "н"]:
    print("\n" + texts["bad_choice"])
    input("\nPress Enter to exit...")
    sys.exit(0)

# Spike puzzle
print("\n" + texts["spike_puzzle"])
if input().strip().lower() in ["yes", "да", "д"]:
    print("\n" + texts["died_spikes"])
    input("\nPress Enter to exit...")
    sys.exit(0)

# Independence test
print(texts["hallway_test"])
if input().strip().lower() in ["no", "нет", "н"]:
    print("\n" + texts["died_boredom"])
    input("\nPress Enter to exit...")
    sys.exit(0)

# First battle - Froggit
print("\n" + texts["froggit_battle"])
action = input().strip().lower()

if action in ["fight", "драться", "др", "f"]:
    print(texts["fight_win"])
elif action in ["act", "действовать", "дей", "a"]:
    print(texts["act_win"])
elif action in ["mercy", "пощадить", "пщ", "m"]:
    print(texts["mercy_win"])
else:
    print("\n" + texts["bad_battle"])
    input("\nPress Enter to exit...")
    sys.exit(0)

# Jack easter egg + credits
print(texts["jack_interrupt"].format(name=Name))
time.sleep(2)
print(texts["toriel_home"])
time.sleep(1)

# True ending choice
print(texts["continue_sans"])
if input().strip().lower() in ["yes", "да", "д"]:
    print("\n" + texts["sans_badtime"])
else:
    print(texts["jack_end"])

print("\n" + texts["game_end"])
input("\nPress Enter to exit...")
