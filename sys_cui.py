"""
Python学習日記アプリ

投稿の都度、そのときのタイムスタンプを含んだファイル名のテキストファイルを作る
例: 2024-08-29-1909.txt

log というディレクトリに保存する

その中に、引数で渡した文字列を投入する
"""

import sys
import datetime
import os


def main():
    # 引数がない場合はエラーを出力して終了
    if len(sys.argv) < 2:
        print("Usage: python main.py [text]")
        sys.exit(1)

    # 現在の日時を取得
    now = datetime.datetime.now()

    # ファイル名を生成秒単位までの日時をファイル名にする
    filename = now.strftime("%Y-%m-%d-%H%M%S") + ".txt"
    # filename = now.strftime("%Y-%m-%d-%H%M") + ".txt"

    # logディレクトリが存在しない場合は作成する
    if not os.path.exists('log'):
        os.makedirs('log')

    # ファイルパスを生成
    filepath = os.path.join('log', filename)

    # ファイルを書き込みモードで開く
    with open(filepath, "w") as f:
        # 引数で渡された文字列を書き込む
        f.write(sys.argv[1])

    print("Wrote to", filepath)


if __name__ == "__main__":
    main()
