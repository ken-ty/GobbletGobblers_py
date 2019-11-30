# TicTacToe_py
pythonでTicTacToeを作成.

## ファイル構成
~~~
.
├─── README.md
├─── main.py       # シミュレーション.  
├─── player_ai.py  # ゲームAI.指定したアルゴリズムで行動を決定.  
├─── statevalue.py # 指定したアルゴリズムで状態価値を決定.  
└─── tictactoe.py  # クラスStateを定義.  
~~~

## 推奨環境
Anaconda Prompt を推奨します。
ただし、Pythonが実行できる環境であれば、なんでも構いません。

## 実行方法
1. Anaconda https://www.anaconda.com/ をインストール.
1. TicTacToe_pyをダウンロード.
1. Anaconda Prompt を実行
1. Promptに"python "と入力. (行末のスペースを忘れずに!)
1. ダウンロードしたTicTacToe_pyから、main.pyをAnaconda Promptにドラック&ドロップしてください.
1. Promptは以下のようになっているはずです。
   ~~~
   phtyon [パス]/main.py
   ~~~
   そのままEnterで実行できます.

1. main.pyを書き換えることで、MiniMaxプレイヤー同士のゲームを見ることができます!  
※ 書き換え済みverは、"players_are_MiniMax"ブランチからダウンロードできます.

### 参考文献

* 布留川英一(2019) 『AlphaZero 深層学習・強化学習・探索 人工知能プログラミング実践入門』 ボーンデジタル.  
  https://www.borndigital.co.jp/book/14383.html  

* 八谷大岳, 杉山将(2008) 『強くなるロボティック・ゲームプレイヤーの作り方　プレミアムブックス版』株式会社マイナビ出版.  
  https://book.mynavi.jp/supportsite/detail/9784839956738.html  
