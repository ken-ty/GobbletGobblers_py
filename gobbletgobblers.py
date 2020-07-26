"""三目並べの作成
"""


class State:
    """盤面の状態

  Attributes:
    __init__(self, my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)  : 初期化
    piece_count(self, pieces): 石の数の取得
    is_lose(self): 負けたかどうか
    is_draw(self): 引き分けかどうか
    is_done(self): ゲーム終了かどうか
    next(self, action): 次の状態の取得
    legal_actions(self): 合法手のリストの取得
    is_first_player(self): 先手かどうか
    __str__(self): 文字列表示
  """

    def __init__(self, my_small_pieces=None, enemy_small_pieces=None, my_large_pieces=None, enemy_large_pieces=None):
        """初期化

    Args:
      my_small_pieces (list): 自分の小さい石の場所
      enemy_small_pieces (list): 敵の小さい石の場所
      my_large_pieces (list): 自分の大きい石の場所
      enemy_large_pieces (list): 敵の大きい石の場所
      my_visible_pieces (list): 自分の見える石の場所
      enemy_visible_pieces (list): 敵の見える石の場所
    """
        # 石の配置
        self.my_small_pieces = my_small_pieces if my_small_pieces is not None else [0] * 9
        self.enemy_small_pieces = enemy_small_pieces if enemy_small_pieces is not None else [0] * 9
        self.my_large_pieces = my_large_pieces if my_large_pieces is not None else [0] * 9
        self.enemy_large_pieces = enemy_large_pieces if enemy_large_pieces is not None else [0] * 9
        self.my_visible_pieces = [0] * 9
        for i in range(9):
            self.my_visible_pieces[i] = (self.enemy_large_pieces[i] != 1 and self.my_small_pieces[i]) or \
                                        self.my_large_pieces[i]
        self.enemy_visible_pieces = [0] * 9
        for i in range(9):
            self.enemy_visible_pieces[i] = (self.my_large_pieces[i] != 1 and self.enemy_small_pieces[i]) or \
                                           self.enemy_large_pieces[i]

    @staticmethod
    def piece_count(pieces):
        """石の数の取得

    自分の石でも敵の石でも数えられる.

    Args:
      pieces (list): 石の場所

    Returns:
      int : 石の数
    """
        count = 0
        for i in pieces:
            if i == 1:
                count += 1
        return count

    def is_lose(self):
        """敗北判定

    Returns:
      bool: 負けているならTrue, そうでないならFalse.
    """

        def is_comp(x, y, dx, dy):
            """3並びかどうか

      x, y で指定したマスからdx,dy方向に合計3マスを調べる.
      x, yには、辺のマス(4以外)を指定.
      例：
        (x,y) = (0,3) のマス6から(dx,dy) = (1,-1)の方向、つまり、マス(6, 4, 2)を調べる.

      Args:
        x  (int): 探索開始座標x
        y  (int): 探索開始座標y
        dx (int): 探索方向dx
        dy (int): 探索方向dy

      Returns:
        bool: 3並びならTrue, そうでないならFalse.
      """
            for k in range(3):
                # 範囲外または敵の石がないなら負けてない
                if y < 0 or 2 < y or x < 0 or 2 < x or self.enemy_visible_pieces[x + y * 3] == 0:
                    return False
                # 次のマスの座標にする.
                x, y = x + dx, y + dy
            return True

        # 負けたかどうか
        # 斜めを確認
        if is_comp(0, 0, 1, 1) or is_comp(0, 2, 1, -1):
            # デバッグ:
            # print("斜めまけ")
            return True
        # 縦,横を確認
        for i in range(3):
            if is_comp(0, i, 1, 0):
                # デバッグ:
                # print("横まけ")
                return True
        for i in range(3):
            if is_comp(i, 0, 0, 1):
                # デバッグ:
                # print("縦まけ")
                return True

        # 負けてないならFalse
        return False

    def is_draw(self):
        """引分判定

    Returns:
      bool: 引き分けならTrue, そうでないならFalse.
    """
        return self.piece_count(self.my_small_pieces) + self.piece_count(self.enemy_small_pieces) + self.piece_count(
            self.my_large_pieces) + self.piece_count(self.enemy_large_pieces) == 9

    def is_done(self):
        """ゲーム終了判定

    Returns:
      bool: ゲーム終了ならTrue, そうでないならFalse
    """
        """debug:
    if self.is_lose():
      print("lose done")
    if self.is_draw():
      print("draw done")
    """
        return self.is_lose() or self.is_draw()

    def next(self, action):
        """次の状態の取得

    現在の状態stateに選択した行動actionを反映した、
    新しいStateを作成する。
    新しい局面では手番が入れ替わるため、
    my_xx_piecesとenemy_xx_piecesの返す順序を交換している。

    次のstateを作成するために使う。
    例: state = State(state.next( action ))

    Args:
      action (int): 次に置くマスを０～８, ９～１７で指定.

    Returns:
      (enemy_small_pieces, my_small_pieces, enemy_large_pieces, my_large_pieces) (State): 行動を反映させたenemy_xx_pieces, my_xx_piecesを返す.
    """
        my_small_pieces = self.my_small_pieces.copy()  # リストだからcopyを使用.
        my_large_pieces = self.my_large_pieces.copy()  # リストだからcopyを使用.
        if action < 9:
            my_small_pieces[action] = 1
        else:
            my_large_pieces[action - 9] = 1
        # enemy_piecesと更新したmy_piecesを入れ替えてStateを作成.
        return State(self.enemy_small_pieces, my_small_pieces, self.enemy_large_pieces, my_large_pieces)

    def legal_actions(self):
        """合法手のリストの取得

    Returns:
      actions: 合法手のリスト
    """
        actions = []
        for i in range(9):
            if self.my_small_pieces[i] == 0 and self.enemy_small_pieces[i] == 0 and self.my_large_pieces[i] == 0 and \
                    self.enemy_large_pieces[i] == 0:
                actions.append(i)
        for i in range(9):
            if self.my_large_pieces[i] == 0 and self.enemy_large_pieces[i] == 0:
                actions.append(i + 9)
        return actions

    def is_first_player(self):
        """先手かどうか

    Returns:
      bool: 先手ならTrue, 後手ならFalse.
    """
        return self.piece_count(self.my_small_pieces) + self.piece_count(self.my_large_pieces) == self.piece_count(
            self.enemy_small_pieces) + self.piece_count(self.enemy_large_pieces)

    def __str__(self):
        """文字列表示

    このインスタンスをprint()やstr()で表示させるときのフォーマットを指定.
    現在の局面を文字列でグラフィカルに表示する.

      Returns
        str: 盤の状態を文字列表示で定義.
    """
        # is_first_player()で、今が自分の番か敵の番かを確認し、局面を正しく表示する.
        ox = ('o', 'x') if self.is_first_player() else ('x', 'o')
        string = ' small\n  '
        for i in range(9):
            if self.my_small_pieces[i] == 1:
                string += ox[0]
            elif self.enemy_small_pieces[i] == 1:
                string += ox[1]
            else:
                string += '-'
            if i % 3 == 2:
                string += '\n  '

        string += '\r large\n  '
        for i in range(9):
            if self.my_large_pieces[i] == 1:
                string += ox[0]
            elif self.enemy_large_pieces[i] == 1:
                string += ox[1]
            else:
                string += '-'
            if i % 3 == 2:
                string += '\n  '

        string += '\r   ↓\n\n'
        string += 'visible\n  '
        for i in range(9):
            if self.my_visible_pieces[i] == 1:
                string += ox[0]
            elif self.enemy_visible_pieces[i] == 1:
                string += ox[1]
            else:
                string += '-'
            if i % 3 == 2:
                string += '\n  '
        return string
