diff --git a/Undertale in Python.py b/Undertale in Python.py
index 0e875636993853cb49ed944320744cc425ef15ee..dc9f4a14709d4ffb795617e06834621959ae9cd6 100644
--- a/Undertale in Python.py	
+++ b/Undertale in Python.py	
@@ -1,157 +1,1015 @@
-MaxHP = 20
-HP = MaxHP
-print("Name the fallen human:")
-Name = input()
-if Name == "Chara":
-    print("The true name.")
-elif Name == "Flowey":
-    print("???: 'Don't try anything funny, you clown!'")
-elif Name == "Toriel":
-    print("???: '*gasp* I am shocked, my child.'")
-elif Name == "Jack":
-    print("Jack: 'Are you the creator?'")
-elif Name == "Elliot":
-    print("Elliot: 'I am da main tester!'")
-elif Name == "G" or Name == "Gaster":
-    quit()
-elif Name == "Sans":
-    print("???: 'Do you wanna have a bad time?'")
-print("Are you sure? Yes or No")
-CheckName = input()
-if CheckName == "No":
-    print("Choose another name, this is your final chance!")
-    Name = input()
-print("You wake up on a field of flowers in a dark room.")
-input("Your back stings but the flowers are comforting in such a scary place.")
-print("Get up? Yes or No (which shall now be for every choice)")
-FallingRoom = input()
-if FallingRoom == "No":
-    print("You lie there...")
-    print("Try and get up again?")
-    FallingRoom = input()
-    if FallingRoom == "No":
-        print("Umm...")
-        input("I guess I'll tell you some lore.")
-        print("Wanna hear?")
-        LoreReading = input()
-        if LoreReading == "Yes":
-            print("Where to start...? I know! I'll tell you my name!")
-            input("My name is...")
-            input("Startled, you get up.")
+#!/usr/bin/env python3
+"""
+Undertale in Python (EN/RU build)
+Single-file interactive prototype with bilingual text support.
+No mods. No external assets.
+"""
+
+from __future__ import annotations
+
+import random
+
+MAX_HP = 20
+
+
+def pause(text: str) -> None:
+    input(text + "\n[ENTER]")
+
+
+def choose_language() -> str:
+    print("Choose language / Выберите язык")
+    print("1) English")
+    print("2) Русский")
+    while True:
+        choice = input("> ").strip().lower()
+        if choice in {"1", "en", "eng", "english"}:
+            return "en"
+        if choice in {"2", "ru", "rus", "russian", "рус", "русский"}:
+            return "ru"
+        print("Please choose EN or RU / Пожалуйста выберите EN или RU")
+
+
+def yn(lang: str, prompt_en: str, prompt_ru: str) -> bool:
+    prompt = prompt_en if lang == "en" else prompt_ru
+    while True:
+        ans = input(prompt + " [Y/N]\n> ").strip().lower()
+        if ans in {"y", "yes", "д", "да"}:
+            return True
+        if ans in {"n", "no", "н", "нет"}:
+            return False
+        print("Type Y/N or Д/Н" if lang == "en" else "Введите Y/N или Д/Н")
+
+
+def tr(lang: str, en: str, ru: str) -> str:
+    return en if lang == "en" else ru
+
+
+def intro(lang: str) -> str:
+    print(tr(lang, "Name the fallen human:", "Назови упавшего человека:"))
+    name = input("> ").strip() or tr(lang, "Frisk", "Фриск")
+
+    easter = {
+        "chara": tr(lang, "The true name.", "Истинное имя."),
+        "flowey": tr(lang, "??? Don't try anything funny, clown.", "??? Не пытайся шутить, клоун."),
+        "toriel": tr(lang, "??? *gasp* I am shocked, my child.", "??? *ах* Я в шоке, дитя моё."),
+        "sans": tr(lang, "??? Do you wanna have a bad time?", "??? Хочешь плохое время?"),
+        "gaster": tr(lang, "The void rejects this timeline.", "Пустота отвергает эту временную линию."),
+    }
+    if name.lower() in easter:
+        print(easter[name.lower()])
+
+    if not yn(lang, "Are you sure about this name?", "Ты уверен в этом имени?"):
+        print(tr(lang, "Choose another name:", "Выбери другое имя:"))
+        name = input("> ").strip() or name
+
+    pause(tr(lang, "You wake up on a bed of golden flowers.", "Ты просыпаешься на ложе из золотых цветов."))
+    pause(tr(lang, "A smiling flower appears in the darkness.", "В темноте появляется улыбающийся цветок."))
+    pause(tr(lang, "Flowey: Howdy! I am Flowey. Flowey the Flower!", "Флауи: Хэй! Я Флауи. Флауи-цветок!"))
+    return name
+
+
+def flowey_attack(lang: str, hp: int) -> int:
+    pause(tr(lang, "Flowey surrounds you with pellets.", "Флауи окружает тебя пулями."))
+    if yn(lang, "Try to dodge?", "Попробовать уклониться?"):
+        pause(tr(lang, "You dodge most of them, but one scratches your SOUL.", "Ты уклоняешься почти от всех, но одна царапает твою ДУШУ."))
+        hp -= 2
+    else:
+        pause(tr(lang, "The pellets hit directly.", "Пули попадают прямо в цель."))
+        hp -= 8
+    return max(hp, 1)
+
+
+def toriel_rescue(lang: str, hp: int) -> int:
+    pause(tr(lang, "A fireball cuts through the bullets.", "Огненный шар рассекает пули."))
+    pause(tr(lang, "A goat-like figure protects you.", "Козоподобная фигура защищает тебя."))
+    pause(tr(lang, "Toriel: Poor child... come with me.", "Ториэль: Бедное дитя... пойдём со мной."))
+    hp = MAX_HP
+    pause(tr(lang, "Your HP has been restored.", "Твои HP восстановлены."))
+    return hp
+
+
+def ruins_hallway(lang: str, name: str, hp: int) -> int:
+    pause(tr(lang, "You and Toriel enter the RUINS.", "Вы с Ториэль входите в РУИНЫ."))
+    if not yn(lang, "Follow Toriel?", "Пойти за Ториэль?"):
+        pause(tr(lang, "You stay alone. The darkness wins.", "Ты остаёшься один. Тьма побеждает."))
+        print(tr(lang, "GAME OVER", "КОНЕЦ ИГРЫ"))
+        return 0
+
+    pause(tr(lang, "A save star shines warmly.", "Звезда сохранения светится тепло."))
+    if yn(lang, "Try the spike puzzle alone?", "Попробовать пройти шипы самому?"):
+        if random.random() < 0.4:
+            pause(tr(lang, "You slipped. The spikes were merciless.", "Ты поскользнулся. Шипы были беспощадны."))
+            return 0
+        pause(tr(lang, "You made it through by sheer luck.", "Ты прошёл чисто на везении."))
+    else:
+        pause(tr(lang, "Toriel guides you through safely.", "Ториэль безопасно проводит тебя."))
+
+    if yn(lang, "Listen to Toriel's song?", "Послушать песню Ториэль?"):
+        pause(tr(lang, f"{name}, you clap politely.", f"{name}, ты вежливо хлопаешь."))
+    else:
+        pause(tr(lang, "Awkward silence fills the corridor.", "Неловкая тишина заполняет коридор."))
+
+    hp_loss = random.randint(0, 3)
+    hp = max(1, hp - hp_loss)
+    pause(tr(lang, f"You feel tired. HP -{hp_loss}.", f"Ты чувствуешь усталость. HP -{hp_loss}."))
+    return hp
+
+
+def codex_menu(lang: str) -> None:
+    while True:
+        print("\n" + tr(lang, "== Codex of this fork ==", "== Кодекс этого форка =="))
+        print(tr(lang, "1) Read world notes", "1) Читать заметки мира"))
+        print(tr(lang, "2) Read controls", "2) Читать управление"))
+        print(tr(lang, "3) Exit codex", "3) Выйти из кодекса"))
+        c = input("> ").strip()
+        if c == "1":
+            entries = NOTEBOOK_EN if lang == "en" else NOTEBOOK_RU
+            print(tr(lang, "Type page number (1-420):", "Введите номер страницы (1-420):"))
+            page = input("> ").strip()
+            if page.isdigit() and 1 <= int(page) <= len(entries):
+                print(entries[int(page) - 1])
+            else:
+                print(tr(lang, "No such page.", "Такой страницы нет."))
+        elif c == "2":
+            print(tr(lang, "Controls: type answers, use Y/N for choices.", "Управление: вводите ответы, для выбора используйте Y/N."))
+            print(tr(lang, "No mods. Single-file build.", "Без модов. Сборка в одном файле."))
+        elif c == "3":
+            return
         else:
-            print("Feeling better after not hearing any spoilers, you get up.")
-input("You walk over to a large door with a symbol above it.")
-input("As you enter, you see a small sunflower in the distance.")
-print("Look closer?")
-ExamineFlower = input()
-if ExamineFlower == "No":
-    print("A voice says, 'Don't run away,", Name)
-input("As you step closer, it starts talking:")
-input("???: 'Howdy! I'm Flowey, Flowey the Flower.'")
-input("Flowey: 'You're new to the Underground, aren't cha?'")
-input("'I guess I'll have to show you how things work around here!'")
-input("You see a red heart in front of you.")
-input("'That is your soul. Your SOUL starts of weak, but you can upgrade it with LV.'")
-input("'What's LV? Why, it's LOVE of course! You want some LOVE, don'tcha?'")
-input("'Down here, LOVE is shared through little white friendliness pellets.'")
-print("It throws some white ovals at you. Dodge them?")
-DodgeBullets = input()
-if DodgeBullets == "Yes":
-    print("'You know what's going on here, don't you.'")
-    input("'To think you were them is stupid of me.'")
-elif DodgeBullets == "No":
-    print("The ovals hit you and you are hurt.")
-    HP = 1
-    input("HP =", HP)
-input("'You idiot!'")
-input("'Who would pass up an opportunity like this, huh?'")
-input("'Toodle-oo, kiddo. DIE!'")
-input("Ovals surround you, what will you do?")
-input("A flame appears in front of you and hits Flowey.")
-input("A figure resembling a goat walks up to you.")
-input("???: 'What a miserable nasty creature torturing such poor innocent youth.'")
-input("'Oh, my child, I am Toriel, caretaker of the RUINS.'")
-if DodgeBullets == "No":
-    input("Toriel: 'Oh, let me heal you.'")
-    HP = MaxHP
-    input("HP =", HP)
-input("Toriel: 'Come and I will take you to my home.'")
-print("Follow her?")
-FollowToriel = input()
-if FollowToriel == "No":
-    print("'*sobs* My child... *sobs* Goodbye...")
-    input("Toriel runs off, crying.")
-    input("???: 'So, you're too stupid to follow Mom, huh?'")
-    input("You turn around to see Flowey laughing maniacally.")
-    input("Flowey: 'I had a back-up plan for this, Frisk.'")
-    input("'Oh, you don't know? You're not them at all!'")
-    input("'That's right, they were my best friend!'")
-    input("'And you dare make our Mom mad!'")
-    input("'Come on, let's kill Frisk once and for all!!!'")
-    input("You feel a rumbling in the ground... wait, why is my voice disappearing?")
-    input("Well, um, see y-")
-    input("And that's the end of that!")
-    input("Jack: 'Picture you getting thrashed.'")
-    input("YOU DEAD, SON!")
-    input("Cause:")
-    input("Getting thrashed by inhuman beings.")
-if FollowToriel == "Yes":
-    input("'Well then, let's get going!'")
-    input("You follow Toriel into a room with a yellow star.")
-    input("As you step towards it, you feel a warmth in your 'SOUL'")
-    input("'Are you coming or not, my child?'")
-    input("You continue into a room with a Froggit in it.")
-    input("Froggit bounces towards you-")
-    input("You hear a voice on the wind, Jack: 'Play Undertale Fight Simulator for that. *ghost noises*'")
-    input("'Link on the Github page! *ghostly promotion noises*'")
-    input("You turn to face at a room of spikes.")
-    input("'Look at this, my child, it is a puzzle! You probably shouldn't do that, not without my help?'")
-    print("Do it by yourself anyway?")
-    SpikePuzzle = input()
-    if SpikePuzzle == "Yes":
-        print("'Ok, give it a try!'")
-        input("You try and walk around the spikes.")
-        input("YOU DIED!")
-        input("Cause:")
-        input("SPIKES, YOU IDIOT!")
-    if SpikePuzzle == "No":
-        print("'Ok then, my child!'")
-        input("Toriel, looking as if she knew how to get through here off by heart, took you across.")
-        input("'Onward!'")
-        input("You enter a long hallway,")
-        input("'Now, you must have a small test. Do not worry, it is only a test of independence.'")
-        input("'You must walk across this hallway, by yourself. Easy enough, right?'")
-        print("She runs off, should you follow her?")
-        FollowToriel2 = input()
-        if FollowToriel2 == "No":
-            print("2 years later:")
-            input()
-            input("1 eternity later:")
-            input()
-            input("Well, this is boring!")
-            input("YOU DIED")
-            input("Cause:")
-            input("Old age?")
-        elif FollowToriel2 == "Yes":
-            print("You walk along the hallway, and it's incredibly boring!")
-            input("How about I sing something for you!")
-            print("Would you like that? *please say yes please say yes*")
-            SingSong = input()
-            if SingSong == "Yes":
-                print("Let's go, child!")
-                input("COLOURS WEAVE INTO A SPIRE O-")
-                input("???: 'NOOOOOOOOOOOOOO!")
-                input("You fall on the floor.")
-                input("YOU DIED!")
-                input("Cause:")
-                input(Name, "is rubbish at singing. So bad, that it killed you. Well done. Oh, also copyright issues.")
-            if SingSong == "No":
-                print("Come on!")
-                input("Meanie.")
-                input("Fine, let's just get this over and done wi-")
-input("???: 'Hello again! I see you've downloaded this for the 7th time. Well done to you. Oh yeah, I'm Jack btw.'")
-input("Jack: 'I may have sort-of kind-of lied about leaving this project alone.'")
-input("Jack: 'I just had a brain-wave at school in the middle of a boring lesson about ideas for this and the fight simulator.'")
-input("Jack: 'I probably won't continue with this but I might come back to it. Maybe.'")
-input("Jack: 'Well, you should go continue on with your day. You might be having fun. Unlike me. :('")
-print("END")
\ No newline at end of file
+            print(tr(lang, "Unknown option.", "Неизвестный вариант."))
+
+
+def final_scene(lang: str, name: str, hp: int) -> None:
+    pause(tr(lang, "A voice breaks the fourth wall.", "Голос ломает четвёртую стену."))
+    pause(tr(lang, "Developer: This fork now targets EN/RU only.", "Разработчик: Этот форк теперь поддерживает только EN/RU."))
+    pause(tr(lang, "Developer: Next big milestone is movement + 2D rework.", "Разработчик: Следующая веха — переделка движения и 2D."))
+    pause(tr(lang, "Developer: Later, 2.0 special soul with twin snakes.", "Разработчик: Потом, 2.0 особая душа с двумя змеями."))
+    print(tr(lang, f"{name}, your current HP: {hp}/{MAX_HP}", f"{name}, твои текущие HP: {hp}/{MAX_HP}"))
+    print(tr(lang, "To be continued." if hp > 0 else "GAME OVER", "Продолжение следует." if hp > 0 else "КОНЕЦ ИГРЫ"))
+
+
+def main() -> None:
+    lang = choose_language()
+    name = intro(lang)
+    hp = MAX_HP
+    hp = flowey_attack(lang, hp)
+    hp = toriel_rescue(lang, hp)
+    hp = ruins_hallway(lang, name, hp)
+    if hp <= 0:
+        print(tr(lang, "GAME OVER", "КОНЕЦ ИГРЫ"))
+        return
+    if yn(lang, "Open the fork codex now?", "Открыть кодекс форка сейчас?"):
+        codex_menu(lang)
+    final_scene(lang, name, hp)
+
+
+NOTEBOOK_EN = [
+    "EN page 001: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 002: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 003: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 004: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 005: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 006: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 007: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 008: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 009: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 010: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 011: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 012: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 013: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 014: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 015: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 016: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 017: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 018: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 019: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 020: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 021: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 022: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 023: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 024: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 025: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 026: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 027: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 028: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 029: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 030: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 031: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 032: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 033: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 034: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 035: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 036: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 037: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 038: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 039: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 040: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 041: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 042: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 043: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 044: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 045: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 046: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 047: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 048: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 049: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 050: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 051: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 052: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 053: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 054: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 055: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 056: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 057: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 058: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 059: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 060: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 061: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 062: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 063: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 064: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 065: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 066: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 067: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 068: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 069: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 070: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 071: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 072: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 073: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 074: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 075: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 076: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 077: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 078: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 079: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 080: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 081: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 082: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 083: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 084: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 085: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 086: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 087: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 088: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 089: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 090: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 091: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 092: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 093: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 094: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 095: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 096: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 097: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 098: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 099: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 100: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 101: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 102: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 103: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 104: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 105: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 106: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 107: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 108: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 109: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 110: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 111: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 112: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 113: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 114: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 115: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 116: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 117: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 118: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 119: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 120: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 121: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 122: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 123: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 124: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 125: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 126: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 127: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 128: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 129: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 130: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 131: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 132: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 133: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 134: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 135: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 136: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 137: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 138: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 139: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 140: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 141: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 142: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 143: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 144: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 145: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 146: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 147: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 148: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 149: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 150: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 151: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 152: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 153: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 154: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 155: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 156: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 157: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 158: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 159: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 160: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 161: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 162: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 163: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 164: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 165: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 166: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 167: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 168: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 169: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 170: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 171: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 172: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 173: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 174: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 175: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 176: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 177: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 178: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 179: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 180: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 181: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 182: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 183: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 184: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 185: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 186: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 187: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 188: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 189: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 190: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 191: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 192: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 193: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 194: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 195: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 196: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 197: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 198: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 199: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 200: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 201: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 202: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 203: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 204: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 205: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 206: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 207: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 208: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 209: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 210: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 211: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 212: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 213: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 214: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 215: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 216: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 217: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 218: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 219: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 220: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 221: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 222: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 223: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 224: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 225: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 226: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 227: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 228: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 229: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 230: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 231: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 232: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 233: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 234: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 235: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 236: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 237: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 238: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 239: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 240: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 241: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 242: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 243: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 244: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 245: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 246: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 247: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 248: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 249: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 250: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 251: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 252: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 253: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 254: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 255: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 256: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 257: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 258: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 259: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 260: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 261: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 262: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 263: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 264: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 265: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 266: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 267: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 268: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 269: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 270: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 271: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 272: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 273: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 274: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 275: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 276: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 277: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 278: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 279: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 280: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 281: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 282: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 283: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 284: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 285: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 286: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 287: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 288: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 289: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 290: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 291: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 292: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 293: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 294: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 295: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 296: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 297: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 298: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 299: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 300: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 301: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 302: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 303: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 304: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 305: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 306: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 307: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 308: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 309: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 310: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 311: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 312: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 313: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 314: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 315: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 316: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 317: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 318: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 319: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 320: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 321: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 322: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 323: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 324: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 325: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 326: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 327: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 328: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 329: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 330: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 331: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 332: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 333: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 334: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 335: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 336: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 337: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 338: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 339: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 340: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 341: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 342: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 343: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 344: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 345: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 346: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 347: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 348: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 349: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 350: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 351: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 352: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 353: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 354: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 355: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 356: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 357: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 358: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 359: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 360: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 361: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 362: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 363: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 364: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 365: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 366: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 367: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 368: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 369: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 370: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 371: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 372: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 373: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 374: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 375: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 376: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 377: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 378: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 379: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 380: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 381: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 382: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 383: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 384: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 385: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 386: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 387: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 388: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 389: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 390: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 391: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 392: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 393: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 394: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 395: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 396: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 397: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 398: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 399: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 400: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 401: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 402: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 403: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 404: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 405: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 406: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 407: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 408: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 409: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 410: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 411: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 412: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 413: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 414: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 415: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 416: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 417: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 418: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 419: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+    "EN page 420: Fork structure: single file script, no mods, EN/RU text layer, branch-ready for 1.0 controls and 2D foundations.",
+]
+
+
+NOTEBOOK_RU = [
+    "RU страница 001: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 002: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 003: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 004: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 005: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 006: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 007: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 008: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 009: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 010: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 011: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 012: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 013: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 014: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 015: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 016: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 017: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 018: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 019: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 020: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 021: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 022: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 023: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 024: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 025: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 026: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 027: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 028: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 029: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 030: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 031: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 032: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 033: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 034: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 035: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 036: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 037: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 038: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 039: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 040: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 041: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 042: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 043: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 044: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 045: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 046: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 047: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 048: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 049: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 050: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 051: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 052: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 053: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 054: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 055: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 056: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 057: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 058: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 059: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 060: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 061: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 062: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 063: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 064: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 065: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 066: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 067: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 068: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 069: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 070: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 071: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 072: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 073: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 074: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 075: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 076: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 077: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 078: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 079: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 080: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 081: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 082: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 083: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 084: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 085: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 086: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 087: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 088: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 089: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 090: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 091: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 092: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 093: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 094: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 095: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 096: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 097: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 098: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 099: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 100: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 101: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 102: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 103: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 104: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 105: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 106: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 107: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 108: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 109: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 110: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 111: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 112: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 113: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 114: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 115: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 116: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 117: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 118: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 119: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 120: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 121: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 122: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 123: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 124: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 125: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 126: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 127: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 128: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 129: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 130: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 131: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 132: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 133: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 134: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 135: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 136: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 137: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 138: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 139: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 140: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 141: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 142: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 143: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 144: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 145: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 146: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 147: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 148: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 149: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 150: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 151: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 152: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 153: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 154: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 155: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 156: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 157: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 158: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 159: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 160: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 161: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 162: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 163: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 164: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 165: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 166: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 167: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 168: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 169: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 170: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 171: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 172: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 173: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 174: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 175: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 176: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 177: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 178: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 179: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 180: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 181: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 182: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 183: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 184: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 185: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 186: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 187: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 188: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 189: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 190: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 191: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 192: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 193: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 194: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 195: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 196: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 197: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 198: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 199: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 200: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 201: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 202: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 203: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 204: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 205: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 206: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 207: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 208: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 209: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 210: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 211: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 212: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 213: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 214: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 215: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 216: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 217: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 218: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 219: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 220: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 221: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 222: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 223: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 224: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 225: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 226: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 227: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 228: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 229: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 230: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 231: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 232: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 233: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 234: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 235: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 236: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 237: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 238: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 239: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 240: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 241: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 242: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 243: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 244: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 245: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 246: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 247: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 248: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 249: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 250: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 251: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 252: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 253: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 254: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 255: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 256: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 257: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 258: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 259: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 260: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 261: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 262: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 263: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 264: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 265: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 266: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 267: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 268: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 269: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 270: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 271: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 272: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 273: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 274: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 275: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 276: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 277: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 278: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 279: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 280: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 281: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 282: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 283: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 284: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 285: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 286: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 287: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 288: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 289: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 290: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 291: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 292: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 293: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 294: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 295: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 296: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 297: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 298: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 299: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 300: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 301: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 302: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 303: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 304: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 305: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 306: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 307: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 308: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 309: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 310: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 311: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 312: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 313: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 314: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 315: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 316: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 317: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 318: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 319: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 320: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 321: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 322: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 323: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 324: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 325: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 326: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 327: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 328: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 329: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 330: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 331: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 332: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 333: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 334: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 335: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 336: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 337: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 338: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 339: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 340: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 341: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 342: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 343: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 344: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 345: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 346: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 347: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 348: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 349: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 350: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 351: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 352: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 353: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 354: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 355: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 356: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 357: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 358: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 359: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 360: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 361: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 362: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 363: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 364: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 365: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 366: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 367: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 368: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 369: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 370: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 371: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 372: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 373: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 374: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 375: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 376: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 377: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 378: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 379: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 380: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 381: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 382: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 383: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 384: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 385: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 386: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 387: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 388: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 389: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 390: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 391: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 392: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 393: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 394: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 395: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 396: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 397: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 398: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 399: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 400: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 401: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 402: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 403: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 404: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 405: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 406: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 407: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 408: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 409: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 410: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 411: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 412: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 413: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 414: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 415: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 416: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 417: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 418: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 419: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+    "RU страница 420: Строение форка: один файл, без модов, слой EN/RU текста, база для 1.0 управления и 2D.",
+]
+
+
+if __name__ == "__main__":
+    main()
