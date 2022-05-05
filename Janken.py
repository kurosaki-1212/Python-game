# じゃんけん
class JankenGame:
    
    # 関数を挿入
    def action(self):

        # ランダム関数をインポートする
        import random

        print("じゃんけんゲーム")

        # 勝った回数　負けた回数　引き分けた回数
        win = lose = draw = 0

        # ０～２の値をランダムで出す
        while True:
            ai = random.randint(0, 2)

            # ０～２の値を入力してもらう
            while True:
                human = int(input("じゃんけん？（０：グー/１：チョキ/２：パー）"))
                
                # ０～２の値が入力されたときにループを抜ける
                if 0 <= human <= 2:
                    break

            # ランダムで出た数字でじゃんけんをだす
            print("私は", end="")
            if ai == 0:
                print("グー", end="")
            elif ai == 1:
                print("チョキ", end="")
            elif ai == 2:
                print("パー", end="")
            print("です。")

            # 勝敗の判定
            judgement = (human - ai + 3) % 3
            
            # 判定の結果を出力する
            if judgement == 0:
                print("引き分けです。")
                # drawに一つ追加する
                draw = draw + 1
            elif judgement == 1:
                print("あなたの負けです。")
                # loseに一つ追加する
                lose = lose + 1
            else:
                print("あなたの勝ちです。")
                # winに一つ追加する
                win = win + 1

            # もう一度やるか聞く
            again = int(input("もう一度やりますか？（０：はい/１：いいえ）："))
            if again == 1:
                break
            
        # 結果をまとめて出力する
        print("結果：", win, "勝", lose, "敗", draw, "分 でした")
        print("また来てください！")