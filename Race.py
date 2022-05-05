# レースゲーム
class RaceGame:

    # ランダム関数とタイム関数をインポートする
    def action(self):
        import random
        import time

        print("レースゲーム")

        while True:
            # ３台の車の初期値を0にする
            wheel_1 = 0
            wheel_2 = 0
            wheel_3 = 0

            # ゴールまでの距離を入力してもらう
            goal = int(input("ゴールまでの値を入力してください："))

            # ３台の車の名前を入力してもらう
            car_1 = input("一台目の車の名前を入力してください：")
            car_2 = input("二台目の車の名前を入力してください：")
            car_3 = input("三台目の車の名前を入力してください：")

            # 指定された文字が入力されるまでループする
            while True:
                predict = input("どれが勝つでしょう？：" + " " + car_1 + " : " +  car_2 + " : " + car_3 + "  :")
                if predict == car_1 or predict == car_2 or predict == car_3:
                    break

            # 入力された馬の名前を出す
            print("レース開始です！")
            print("あなたが選んだ馬は", predict, "です")

            # １～５までの数字をランダムにだしゴールの距離まで入力する
            while wheel_1 <= goal and wheel_2 <= goal and wheel_3 <= goal:
                wheel_1 += wheel_1 + random.randint(1, 5)
                wheel_2 += wheel_2 + random.randint(1, 5)
                wheel_3 += wheel_3 + random.randint(1, 5)

                # ランダムに出した数字の数だけ前に進める
                print(car_1 + "：" + "{= " * wheel_1 + "⛟")
                print(car_2 + "：" + "{= " * wheel_2 + "⛟")
                print(car_3 + "：" + "{= " * wheel_3 + "⛟")
                print("")

                # 処理を一時停止する
                time.sleep(1)

            # if分で１位の車を変数に挿入させる
            if wheel_2 < wheel_1 and wheel_3 < wheel_1:
                    winner = car_1
            elif car_1 < car_2 and car_3 < car_2:
                    winner = car_2
            elif car_1 < car_3 and car_2 < car_3:
                    winner = car_3

            # １位になった馬と入力された車の名前を出力する
            if winner == predict:
                print("一位になったのは", winner, "です！")
                print("あなたの", predict, "は勝利しました！")
                print("おめでとうございます！")
            else:
                print("一位になったのは", winner, "です")
                print("あなたの", predict, "は敗北しました")
                print("残念でした…")

            # もう一度やるか聞く
            again = int(input("もう一度やりますか？（０：はい/１：いいえ）　："))
            if again == 1:
                    break

        print("また来てください！")