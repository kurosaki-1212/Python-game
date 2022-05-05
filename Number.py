# 数当てゲーム
class NumberGame:
    
    # __init__を使って初期値を０にする
    def __init__(self, max_num :int):
        self.max_num = max_num
    
    # 関数を挿入
    def action(self):

        # ランダム関数をインポートする
        import random

        while True:

            # 名前を変更する
            max = self.max_num

            # 入力できる回数を指定する
            max_count = 20

            # formatで数を当てはめる
            print("１～{}の数を{}回以内で当ててください。".format(max, max_count))

            # 入力回数の初期値を１にする
            count = 1

            # ランダムで１～maxまでの値を一つだす
            answer = random.randint(1, max)
            
            # カウントが１０を超えるまでループする
            while count <= max_count:
                print(count, "回目　いくつでしょう？：", end="")

                # 値を入力してもらう
                num = int(input())
                
                # 既定の範囲じゃなかった場合繰り返す
                if num < 1 or num > max:
                    continue

                # 入力した数字がランダムな数字と合っていた場合
                if num == answer:
                    print("正解です！", count, "回で当たりました！")
                    break

                # 入力した数字がランダムな数字より小さかった場合
                elif num > answer:
                    print("もっと小さな数です。")
                    
                # 入力した値がランダムな数字より大きかった場合
                elif num < answer:
                    print("もっと大きな数です")

                # 入力した値がランダムな数字と違かった場合カウントを一つ増やす
                count = count + 1
            
            # カウントが１０を超えてしまった場合答えを出力する
            else:
                print("残念…  正解は", answer, "でした。")

            # もう一度やるか聞く
            again = int(input("もう一度やりますか？（０：はい/１：いいえ）："))
            if again == 1:
                break

        print("また来てください！")