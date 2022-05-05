# 明日のラッキーアイテム
class Lucky:

    # 関数を挿入
    def action(self):

        # ランダム関数をインポートする
        import random

        print("明日のラッキーアイテム")

        # リストを作りランダムで出す
        while True:
            ai = random.choice(["赤", "青", "黄", "緑", "紫", "黒", "白", "桃", "橙", "茶"])

            # 明日の持ち物を入力してもらう
            while True:
                motimono = input("明日身に付けるものはなんですか？：")
                break

            # ランダムに出た色と入力された持ち物を出力する
            print("明日のラッキーアイテムは", ai, "色の", motimono)

            # もう一度やるか聞く
            again = int(input("もう一度やりますか？（０：はい/１：いいえ）："))
            if again == 1:
                break

        print("また来てください！")