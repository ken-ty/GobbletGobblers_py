# coding=utf-8
import unittest
import gobbletgobblers as game


class TestState(unittest.TestCase):
    # 初期化のテスト
    # 以下の条件で正しく初期化ができる
    #   - 空
    #   - smallのみ
    #   - largeのみ
    #   - smallとlargeの重なりなし
    #   - smallとlargeの重なりあり
    #   - smallとlargeの重なりあり色重なりあり
    def test___init__(self):
        patterns = [
            # 空
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0])),

            # smallのみ
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0])),

            # largeのみ
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ox-
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0])),

            # small, large重なりなし
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ox-
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0])),

            # small, large重なりあり
            #  small
            #   ox-
            #   ---
            #   ox-
            #  large
            #   ---
            #   ox-
            #   ox-
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ox-
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]),
             ([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0])),

            # # small, large重なりあり色重なり
            #  small
            #   oxo
            #   --x
            #   ox-
            #  large
            #   --o
            #   oxx
            #   ox-
            #    ↓
            #
            # visible
            #   oxo
            #   oxx
            #   ox-
            (([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0]),
             ([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 1, 0])),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # my_xx_pieces, enemy_xx_pieces, ... , enemy_xx_pieces
            actual = state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces, state.my_visible_pieces, state.enemy_visible_pieces
            self.assertEqual(expect, actual)

    # コマのカウントのテスト
    # 以下の条件で正しくカウントができる
    # - 0つ
    # - 1つ
    # - 2つ
    # - 9つ
    def test_piece_count(self):
        patterns = [
            # 0つ
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], 0),
            # xx_xx_piece
            # ---
            # ---
            # ---

            # 1つ
            ([1, 0, 0, 0, 0, 0, 0, 0, 0], 1),
            # xx_xx_piece
            # o--
            # ---
            # ---

            # 2つ
            ([0, 0, 1, 0, 1, 0, 0, 0, 0], 2),
            # xx_xx_piece
            # --o
            # -o-
            # ---

            # 9つ
            ([1, 1, 1, 1, 1, 1, 1, 1, 1], 9),
            # xx_xx_piece
            # ooo
            # ooo
            # ooo
        ]

        for input_param, expect_param in patterns:
            pieces = input_param
            state = game.State()
            expect = expect_param  # expect_param == num of pieces
            actual = state.piece_count(pieces)
            self.assertEqual(expect, actual)

    # 勝敗判定のテスト
    # 以下の条件で正しく負けを判定できる
    # - visible上で(ここではsmallで)
    #   - 負けていない(空)
    #   - 負けていない(oなし、x揃わず)
    #   - 負けていない(o,x揃わず)
    #   - 勝っている(oが揃う,x揃わず=負けていない)
    #   - 縦並び(0,3,6)
    #   - 縦並び(1,4,7)
    #   - 縦並び(2,5,8)
    #   - 横並び(0,1,2)
    #   - 横並び2(3,4,5)
    #   - 横並び3(6,7,8)
    #   - 斜め並び1(0,4,8)
    #   - 斜め並び2(2,4,6)
    def test_is_lose(self):
        patterns = [
            # 負けていない(空)
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---
            ((None, None, None, None), False),

            # 負けていない(oなし、x揃わず)
            #  small
            #   -x-
            #   x-x
            #   -x-
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   -x-
            #   x-x
            #   -x-
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0], None, None), False),

            # 負けていない(o,x揃わず)
            #  small
            #   xox
            #   xox
            #   oxo
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   xox
            #   xox
            #   oxo
            (([0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1, 0, 1, 0], None, None), False),

            # 勝っている(oが揃う,x揃わず=負けていない)
            #  small
            #   xox
            #   ooo
            #   xox
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #  small
            #   xox
            #   ooo
            #   xox
            (([0, 1, 0, 1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0, 1, 0, 1], None, None), False),

            # 縦並び(0,3,6)
            #  small
            #   x--
            #   x--
            #   x--
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   x--
            #   x--
            #   x--
            ((None, [1, 0, 0, 1, 0, 0, 1, 0, 0], None, None), True),

            # 縦並び(1,4,7)
            #  small
            #   -x-
            #   -x-
            #   -x-
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   -x-
            #   -x-
            #   -x-
            ((None, [0, 1, 0, 0, 1, 0, 0, 1, 0], None, None), True),

            # 縦並び(2,5,8)
            #  small
            #   --x
            #   --x
            #   --x
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   --x
            #   --x
            #   --x
            ((None, [0, 0, 1, 0, 0, 1, 0, 0, 1], None, None), True),

            # 横並び(0,1,2)
            #  small
            #   xxx
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   xxx
            #   ---
            #   ---
            ((None, [1, 1, 1, 0, 0, 0, 0, 0, 0], None, None), True),

            # 横並び(3,4,5)
            #  small
            #   ---
            #   xxx
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   xxx
            #   ---
            ((None, [0, 0, 0, 1, 1, 1, 0, 0, 0], None, None), True),

            # 横並び(6,7,8)
            #  small
            #   ---
            #   ---
            #   xxx
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   xxx
            ((None, [0, 0, 0, 0, 0, 0, 1, 1, 1], None, None), True),

            # 斜め並び1(0,4,8)
            #  small
            #   x--
            #   -x-
            #   --x
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   x--
            #   -x-
            #   --x
            ((None, [1, 0, 0, 0, 1, 0, 0, 0, 1], None, None), True),

            # 斜め並び2(2,4,6)
            #  small
            #   --x
            #   -x-
            #   x--
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   --x
            #   -x-
            #   x--
            ((None, [0, 0, 1, 0, 1, 0, 1, 0, 0], None, None), True),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # is_lose()
            actual = state.is_lose()
            self.assertEqual(expect, actual)

    # 表示のテスト
    # 以下の条件で正しく表示ができる
    #   - 空
    #   - smallのみ
    #   - largeのみ
    #   - smallとlargeの重なりなし
    #   - smallとlargeの重なりあり
    #   - smallとlargeの重なりあり色重なりあり
    def test___str__(self):
        patterns = [
            # 空
            ((None, None, None, None),
             " small\n"  # small
             "  ---\n"  # ---
             "  ---\n"  # ---
             "  ---\n  "  # ---
             "\r large\n"  # large
             "  ---\n"  # ---
             "  ---\n"  # ---
             "  ---\n  "  # ---
             "\r   ↓\n\n"  # ↓

             "visible\n"  # visible
             "  ---\n"  # ---
             "  ---\n"  # ---
             "  ---\n  "),  # ---

            # smallのみ
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], None, None),
             " small\n"  # small
             "  ox-\n"  # ox-
             "  ---\n"  # ---
             "  ---\n  "  # ---
             "\r large\n"  # large
             "  ---\n"  # ---
             "  ---\n"  # ---
             "  ---\n  "  # ---
             "\r   ↓\n\n"  # ↓

             "visible\n"  # visible
             "  ox-\n"  # ox-
             "  ---\n"  # ---
             "  ---\n  "),  # ---

            # largeのみ
            ((None, None, [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]),
             " small\n"  # small
             "  ---\n"  # ---
             "  ---\n"  # ---
             "  ---\n  "  # ---
             "\r large\n"  # large
             "  ox-\n"  # ox-
             "  ---\n"  # ---
             "  ---\n  "  # ---
             "\r   ↓\n\n"  # ↓

             "visible\n"  # visible
             "  ox-\n"  # ox-
             "  ---\n"  # ---
             "  ---\n  "),  # ---

            # small, large重なりなし
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]),
             " small\n"  # small
             "  ox-\n"  # ox-
             "  ---\n"  # ---
             "  ---\n  "  # ---
             "\r large\n"  # large
             "  ---\n"  # ---
             "  ox-\n"  # ox-
             "  ---\n  "  # ---
             "\r   ↓\n\n"  # ↓

             "visible\n"  # visible
             "  ox-\n"  # ox-
             "  ox-\n"  # ox-
             "  ---\n  "),  # ---

            # small, large重なりあり
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]),
             " small\n"  # small
             "  ox-\n"  # ox-
             "  ---\n"  # ---
             "  ox-\n  "  # ox-
             "\r large\n"  # large
             "  ---\n"  # ---
             "  ox-\n"  # ox-
             "  ox-\n  "  # ox-
             "\r   ↓\n\n"  # ↓

             "visible\n"  # visible
             "  ox-\n"  # ox-
             "  ox-\n"  # ox-
             "  ox-\n  "),  # ox-

            # small, large重なりあり色重なり
            (([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0]),
             " small\n"  # small
             "  oxo\n"  # ox-
             "  --x\n"  # ---
             "  ox-\n  "  # ox-
             "\r large\n"  # large
             "  --o\n"  # ---
             "  oxx\n"  # ox-
             "  ox-\n  "  # ox-
             "\r   ↓\n\n"  # ↓

             "visible\n"  # visible
             "  oxo\n"  # ox-
             "  oxx\n"  # ox-
             "  ox-\n  "),  # ox-
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # expect_param == string
            actual = str(state)
            self.assertEqual(expect, actual)

    # 合法手探索のテスト
    # - 空いているマスにはおける
    # - 同じ大きさのコマがあるところにはおけない
    # - largeがある重なったマスにsmallはおけない
    # - smallがある重なったマスにlargeはおける
    def test_legal_actions(self):
        patterns = [
            ((None, None, None, None), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ---
            #   ---
            #   ---

            # smallのみ
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], None, None),
             [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---

            # largeのみ
            ((None, None, [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]),
             [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17]),
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ox-
            #   ---
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ---
            #   ---

            # small, large重なりなし
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]), [2, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17]),
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ox-
            #   ---
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ---

            # small, large重なりあり
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]), [2, 5, 8, 9, 10, 11, 14, 17])
            #  small
            #   ox-
            #   ---
            #   ox-
            #  large
            #   ---
            #   ox-
            #   ox-
            #    ↓
            #
            # visible
            #   ox-
            #   ox-
            #   ox-
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # expect_param == [0, 1, 2, 3, ... , 16, 17]
            actual = state.legal_actions()
            self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
