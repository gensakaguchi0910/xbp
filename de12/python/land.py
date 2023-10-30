
difficulty_levels = {
    1:{"反片":"はんぺん","蒲鉾":"かまぼこ"},
    2: {"御手洗団子": "みたらしだんご", "玉蜀黍": "とうもろこし"},
    3: {"鹿尾菜": "ひじき", "陸蓮根": "おくら"},
    }

def quiz(difficulty):

    words = difficulty_levels.get(difficulty, {})

    if not words:
        print("その難易度は存在しません。")
        return

    
    for word, reading in words.items():
        user_input = input(f"{word} の読み方は？ ")

        if user_input == reading:
            print("正解です！")
        else:
            print(f"残念、正解は {reading} でした。")

for difficulty in range(1, 4):
    print(f"\n難易度 {difficulty}:")
    quiz(difficulty)


