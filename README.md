# TicTacToe_py
[![license](https://img.shields.io/github/license/kentokura/TicTacToe_py)](./LICENSE)

pythonでTicTacToeの必勝法を調査する。  
必勝法である「ゲーム木の全探索」を、NegaMax法で実装したプレイヤーに対して、対戦結果を確認した。
* 同じアルゴリズムのプレイヤーと対戦
* ランダムに行動するプレイヤーと対戦

100回ずつ対戦し、勝ちなら1,負けなら0, 引分けなら0.5をカウントした。つまり、全勝なら100,全敗なら0,全部引分なら50になる。


## ファイル構成
~~~
.
├─── README.md
├─── main.py       # シミュレーション.  
├─── player_ai.py  # プレイヤー.指定したアルゴリズムで行動を決定.  
├─── statevalue.py # 指定したアルゴリズムで状態価値を決定.  
└─── tictactoe.py  # ゲームの状態のクラスStateを定義.  
~~~

## 推奨環境
Anaconda Prompt を推奨します。
ただし、Pythonが実行できる環境であれば、なんでも構いません。

## 実行方法
1. [Anaconda](https://www.anaconda.com/)をインストール.
1. [リリース](https://github.com/kentokura/TicTacToe_py/releases)からバージョンを選んでTicTacToe_pyをダウンロード.
1. Anaconda Prompt を実行
1. Promptに"python "と入力. (行末のスペースを忘れずに!)
1. ダウンロードしたTicTacToe_pyから、main.pyをAnaconda Promptにドラック&ドロップしてください.
1. Promptは以下のようになっているはずです。
   ~~~
   phtyon [パス]/main.py
   ~~~
   そのままEnterで実行できます.

### 参考文献

* 布留川英一(2019) 『AlphaZero 深層学習・強化学習・探索 人工知能プログラミング実践入門』 ボーンデジタル.  
  https://www.borndigital.co.jp/book/14383.html  

* 八谷大岳, 杉山将(2008) 『強くなるロボティック・ゲームプレイヤーの作り方　プレミアムブックス版』株式会社マイナビ出版.  
  https://book.mynavi.jp/supportsite/detail/9784839956738.html  
  
* 伊藤 毅志 , 保木 邦仁 , 三宅 陽一郎 (2018)『ゲーム情報学概論- ゲームを切り拓く人工知能』 コロナ社.  

### LICENSE

[MIT License](./LICENSE)

