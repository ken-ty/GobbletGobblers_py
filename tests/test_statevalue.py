# coding=utf-8
import unittest
import gobbletgobblers as game
import statevalue as value


class TestMiniMax(unittest.TestCase):
    # 価値計算のテスト
    # 以下の条件で正しく価値を計算する(先手目線、後手には-1をかけて適用する)
    # - 勝ち盤面
    # - 負け盤面
    # - 引き分け盤面
    # - 手数がかかる盤面
    #   - 自分のコマを置いて勝ち
    #   - 相手がどこに置いても、次に自分がコマを置いて勝ち
    #   - 自分がどこに置いても、次に相手がコマを置いて負け
    def test_mini_max(self):
        patterns = [
            # 勝ち盤面
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   o--
            #   oo-
            #   o--
            #    ↓
            #
            # visible
            #   o--
            #   oo-
            #   o--
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]), 1),

            # 負け盤面
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   x--
            #   xx-
            #   x--
            #    ↓
            #
            # visible
            #   x--
            #   xx-
            #   x--
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 1, 0, 1, 0, 0]), -1),

            # 引き分け盤面
            #  small
            #   oxo
            #   xxo
            #   oox
            #  large
            #   oxo
            #   xxo
            #   oox
            #    ↓
            #
            # visible
            #   oxo
            #   xxo
            #   oox
            (([1, 0, 1, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1, 1, 1, 0],
              [0, 1, 0, 1, 1, 0, 0, 0, 1]), 0),

            # 自分のコマを置いて勝ち
            #  small
            #   x--
            #   xx-
            #   ---
            #  large
            #   o--
            #   oo-
            #   ---
            #    ↓
            #
            # visible
            #   o--
            #   oo-
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]), 1),

            # 相手がどこに置いても、次に自分がコマを置いて勝ち
            #  small
            #   x--
            #   x--
            #   ---
            #  large
            #   o--
            #   oo-
            #   ---
            #    ↓
            #
            # visible
            #   o--
            #   oo-
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]), 1),

            # 自分がどこに置いても、次に相手がコマを置いて負け
            #  small
            #   o--
            #   oo-
            #   ---
            #  large
            #   x--
            #   xx-
            #   ---
            #    ↓
            #
            # visible
            #   x--
            #   xx-
            #   ---
            (([1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 1, 0, 0, 0, 0]), -1),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 負けなら-1, 引き分けなら0 NegaMaxなので、-1をかける
            actual = value.mini_max(state)
            self.assertEqual(expect, actual)