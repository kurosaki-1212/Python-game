# 西暦から和暦を調べる
class Nengou:

    # 関数を挿入
    def action(self):
        while True:

            # 西暦を入力してもらう
            int_input = int(input("西暦を入力してください。\n"))


            # 明治時代の場合
            # 明治時代の西暦を指定する
            if(int_input >= 1868 and int_input <=1911):
                str_nengo = "明治"

                # 入力してもらった値から1867年を引く
                int_year = int_input - 1867

                # 入力してもらった値から1867年を引いたときに１になった場合の処理
                if int_year == 1:
                    int_lastYear = int_input - 1864
                    str_lastYear = "慶応"
                    # 明治元年（慶応）を出力する
                    print("西暦", int_input , "年は", str_nengo, "元年（", str_lastYear, int_lastYear ,"年）です。\n",sep='')
                
                else:
                    # 明治時代の和暦を出力する
                    print("西暦", int_input , "年は", str_nengo, int_year, "年です。\n",sep='')


            # 大正時代の場合
            # 大正時代の値を指定する
            elif(int_input >=1912 and int_input <=1925):
                str_nengo = "大正"

                # 入力してもらった値から1911年を引く
                int_year = int_input - 1911

                # 入力してもらった値から1911年を引いたときに１になった場合の処理
                if(int_year == 1):
                    int_lastYear = int_input - 1867
                    str_lastYear = "明治"
                    # 大正元年（明治）を出力する
                    print("西暦", int_input , "年は", str_nengo, "元年（", str_lastYear, int_lastYear ,"年）です。\n",sep='')
                
                else:
                    # 大正時代の和暦を出力する
                    print("西暦", int_input , "年は", str_nengo, int_year, "年です。\n",sep='')


            # 昭和時代の場合
            # 昭和時代の値を指定する
            elif(int_input >=1926 and int_input <=1988):
                str_nengo = "昭和"

                # 入力してもらった値から1925年を引く
                int_year = int_input - 1925

                # 入力してもらった値から1925年を引いた時に１になった場合の処理
                if(int_year == 1):
                    int_lastYear = int_input - 1911
                    str_lastYear = "大正"
                    # 昭和元年（大正）を出力する
                    print("西暦", int_input , "年は", str_nengo, "元年（", str_lastYear, int_lastYear ,"年）です。\n",sep='')
                
                else:
                    # 昭和時代の和暦を出力する
                    print("西暦", int_input , "年は", str_nengo, int_year, "年です。\n",sep='')

            # 平成時代の場合
            # 平成時代の西暦を指定する
            elif(int_input >=1989 and int_input <=2018):
                str_nengo = "平成"

                # 入力してもらった値から1988年を引く
                int_year = int_input - 1988

                # 入力してもらった値から1988年を引いたときに１になった場合の処理
                if(int_year == 1):
                    int_lastYear = int_input - 1925
                    str_lastYear = "昭和"
                    # 平成元年（昭和）を出力する
                    print("西暦", int_input , "年は", str_nengo, "元年（", str_lastYear, int_lastYear ,"年）です。\n",sep='')
                
                else:
                    # 平成時代の和暦を出力する
                    print("西暦", int_input , "年は", str_nengo, int_year, "年です。\n",sep='')


            # 令和時代の場合
            # 令和時代の西暦を指定する
            elif(int_input >=2019):
                str_nengo = "令和"

                # 入力してもらった値から2018年を引く
                int_year = int_input - 2018

                # 入力してもらった値から2018年を引いたときに１になった場合の処理
                if(int_year == 1):
                    int_lastYear = int_input - 1988
                    str_lastYear = "平成"
                    # 令和元年（平成）を出力する
                    print("西暦", int_input , "年は", str_nengo, "元年（", str_lastYear, int_lastYear ,"年）です。\n",sep='')
                
                else:
                    # 令和時代の和暦を出力する
                    print("西暦", int_input , "年は", str_nengo, int_year, "年です。\n",sep='')


            # 明治時代より前の時代は例外として扱う
            else:
                if(int_input < 1868):
                    print("西暦", int_input , "年は、かなり古い時代です。\n",sep='')


            # もう一度やるか聞く
            again = int(input("もう一度やりますか？（０：はい/１：いいえ）："))
            if again == 1:
                break

        print("また来てください！")