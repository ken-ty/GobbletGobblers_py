# GobbletGobblers_py

[![license](https://img.shields.io/github/license/kentokura/GobbletGobblers_py?style=social)](./LICENSE)


## このリポジトリについて

GobbletGobblers_pyはGobbletGobblersの解析を行うCUIを作成しています。
ただし、ゲームは簡単の為に以下のルールで行います。

* 一度おいたコマを動かすことはできない
* コマは大と小のみである

### 派生元リポジトリ

このリポジトリは[TicTacToe_py](https://github.com/kentokura/TicTacToe_py)の派生です。  
派生元のリポジトリではpythonでGobbletGobblers_pyの必勝法を調査しています。
必勝法である「ゲーム木の全探索」を、NegaMax法で実装したプレイヤーに対して、対戦結果を確認しています。



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
1. [リリース](XXXXX <!-- https://github.com/kentokura/TicTacToe_py/releases -->)からバージョンを選んでGobbletGobblers_pyをダウンロード.
1. Anaconda Prompt を実行
1. Promptに"python "と入力. (行末のスペースを忘れずに!)
1. ダウンロードしたGobbletGobblers_pyから、main.pyをAnaconda Promptにドラック&ドロップしてください.
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

