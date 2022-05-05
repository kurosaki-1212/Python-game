try:
    # ファイルをインポートする
    import Janken, Number, Item, Year, Race

    # ファイルの中のクラスを呼び出す
    janken = Janken.JankenGame()

    number = Number.NumberGame(50)

    item = Item.Lucky()

    year = Year.Nengou()
    
    race = Race.RaceGame()

    while True:

        # 遊ぶ内容を選んでもらう
        print("何で遊びますか？")
        print("１：じゃんけん")
        print("２：数当てゲーム")
        print("３：明日のラッキーアイテム")
        print("４：西暦から和暦を調べます")
        print("５：レースゲーム")
        print("０：終了します")

        # 選んだ値を入力してもらう
        choice = int(input("数字を入れてください！"))

        # １だった場合「じゃんけん」をやる
        if choice == 1:
            janken.action()

        # ２だった場合「数当てゲーム」をやる
        elif choice == 2:
            number.action()

        # ３だった場合「明日のラッキーアイテム」をやる
        elif choice == 3:
            item.action()

        # ４だった場合「西暦から和暦を調べる」をやる
        elif choice == 4:
            year.action()

        # ５だった場合「レースゲーム」をやる
        elif choice == 5:
            race.action()

        # ０だった場合処理を終了する
        elif choice == 0:
            print("また遊びましょう！")
            break

# 文字が入力されたときの例外処理
except ValueError:
    print("指定された数字を入力してください")

# 処理が終了したときの出力
finally:
    print("お疲れ様でした！")