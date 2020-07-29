# coding=utf-8
import unittest
import gobbletgobblers as game
import state_convert as convert


class TestSymmetryPieces(unittest.TestCase):
    # 時計回りに90度回す
    # - 空
    # - コマあり1
    # - コマあり2
    def test_rotate90(self):
        patterns = [
            # 空
            #  piece
            #   ---
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]),

            # コマあり1
            #  piece
            #   o--
            #   ---
            #   ---
            #  convert_piece
            #   --o
            #   ---
            #   ---
            ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]),

            # コマあり2
            #  piece
            #   ---
            #   ---
            #   --o
            #  convert_piece
            #   ---
            #   ---
            #   o--
            ([0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0]),
        ]
        for input_param, expect_param in patterns:
            xx_xx_pieces = input_param
            expect = expect_param  # 回転後のpieces
            actual = convert.rotate90(xx_xx_pieces)
            self.assertEqual(expect, actual)

    # 時計回りに180度回す
    # - 空
    # - コマあり1
    # - コマあり2
    def test_rotate180(self):
        patterns = [
            # 空
            #  piece
            #   ---
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]),

            # コマあり1
            #  piece
            #   -o-
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   -o-
            ([0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]),

            # コマあり2
            #  piece
            #   --o
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   o--
            ([0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]),
        ]
        for input_param, expect_param in patterns:
            xx_xx_pieces = input_param
            expect = expect_param  # 回転後のpieces
            actual = convert.rotate180(xx_xx_pieces)
            self.assertEqual(expect, actual)

    # 時計回りに270度回す
    # - 空
    # - コマあり1
    # - コマあり2
    def test_rotate270(self):
        patterns = [
            # 空
            #  piece
            #   ---
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]),

            # コマあり1
            #  piece
            #   o--
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   o--
            ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]),

            # コマあり2
            #  piece
            #   ---
            #   ---
            #   --o
            #  convert_piece
            #   --o
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0]),
        ]
        for input_param, expect_param in patterns:
            xx_xx_pieces = input_param
            expect = expect_param  # 回転後のpieces
            actual = convert.rotate270(xx_xx_pieces)
            self.assertEqual(expect, actual)

    # 縦に線対称
    # - 空
    # - コマあり1
    # - コマあり2
    def test_vertical(self):
        patterns = [
            # 空
            #  piece
            #   ---
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]),

            # コマあり1
            #  piece
            #   o--
            #   ---
            #   o--
            #  convert_piece
            #   --o
            #   ---
            #   --o
            ([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1]),

            # コマあり2
            #  piece
            #   ---
            #   ---
            #   --o
            #  convert_piece
            #   ---
            #   ---
            #   o--
            ([0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0]),
        ]
        for input_param, expect_param in patterns:
            xx_xx_pieces = input_param
            expect = expect_param  # 回転後のpieces
            actual = convert.vertical(xx_xx_pieces)
            self.assertEqual(expect, actual)

    # 横に線対称
    # - 空
    # - コマあり1
    # - コマあり2
    def test_horizontal(self):
        patterns = [
            # 空
            #  piece
            #   ---
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]),

            # コマあり1
            #  piece
            #   o-o
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   o-o
            ([1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1]),

            # コマあり2
            #  piece
            #   ---
            #   ooo
            #   ---
            #  convert_piece
            #   ---
            #   ooo
            #   ---
            ([0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0]),
        ]
        for input_param, expect_param in patterns:
            xx_xx_pieces = input_param
            expect = expect_param  # 回転後のpieces
            actual = convert.horizontal(xx_xx_pieces)
            self.assertEqual(expect, actual)

    # 左上から斜めに線対称
    # - 空
    # - コマあり1
    # - コマあり2
    def test_upper_left(self):
        patterns = [
            # 空
            #  piece
            #   ---
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]),

            # コマあり1
            #  piece
            #   -oo
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   o--
            #   o--
            ([0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0]),

            # コマあり2
            #  piece
            #   o--
            #   -o-
            #   --o
            #  convert_piece
            #   o--
            #   -o-
            #   --o
            ([1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1]),
        ]
        for input_param, expect_param in patterns:
            xx_xx_pieces = input_param
            expect = expect_param  # 回転後のpieces
            actual = convert.upper_left(xx_xx_pieces)
            self.assertEqual(expect, actual)

    # 右上から斜めに線対称
    # - 空
    # - コマあり1
    # - コマあり2
    def test_upper_right(self):
        patterns = [
            # 空
            #  piece
            #   ---
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   ---
            #   ---
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]),

            # コマあり1
            #  piece
            #   oo-
            #   ---
            #   ---
            #  convert_piece
            #   ---
            #   --o
            #   --o
            ([1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1]),

            # コマあり2
            #  piece
            #   --o
            #   -o-
            #   o--
            #  convert_piece
            #   --o
            #   -o-
            #   o--
            ([0, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0, 0]),
        ]
        for input_param, expect_param in patterns:
            xx_xx_pieces = input_param
            expect = expect_param  # 回転後のpieces
            actual = convert.upper_right(xx_xx_pieces)
            self.assertEqual(expect, actual)


class TestSymmetryPiecesState(unittest.TestCase):
    # 時計回りに90度回転したStateを作成
    # - 空
    # - コマあり1
    # - コマあり2
    def test_rotate90_state(self):
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
            #
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0])),

            # コマあり1
            #  small
            #   o-x
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   x-o
            #
            #  small
            #   --o
            #   ---
            #   --x
            #  large
            #   x--
            #   ---
            #   o--
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 0, 0]),
             ([0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0])),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.rotate90_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)

    # 時計回りに180度回転したStateを作成
    # - 空
    # - コマあり1
    # - コマあり2
    def test_rotate180_state(self):
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
            #
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0])),

            # コマあり1
            #  small
            #   o-x
            #   ---
            #   ---
            #  large
            #   ---
            #   --o
            #   --x
            #
            #  small
            #   ---
            #   ---
            #   x-o
            #  large
            #   x--
            #   o--
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0])),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.rotate180_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)

    # 時計回りに270度回転したStateを作成
    # - 空
    # - コマあり1
    # - コマあり2
    def test_rotate270_state(self):
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
            #
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0])),

            # コマあり1
            #  small
            #   ox-
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #
            #  small
            #   ---
            #   ---
            #   o--
            #  large
            #   ---
            #   ---
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0])),

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.rotate270_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
