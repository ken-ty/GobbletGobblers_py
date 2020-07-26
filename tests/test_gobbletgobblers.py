# coding=utf-8
import unittest
import gobbletgobblers as game


class TestState(unittest.TestCase):
    # 初期化がちゃんとできているか
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
            ((None, None, None, None),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0])),
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
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0])),
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

            # smallのみ
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0])),
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
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0])),
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
              [0, 0, 0, 0, 1, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0])),
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

            # small, large重なりあり
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]),
             ([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0])),
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

            # # small, large重なりあり色重なり
            (([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0]),
             ([1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 1, 0])),
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

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # my_xx_pieces, enemy_xx_pieces, ... , enemy_xx_pieces
            actual = state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces, state.my_visible_pieces, state.enemy_visible_pieces
            self.assertEqual(expect, actual)

    # 表示がちゃんとできているか
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

    # 合法手
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
