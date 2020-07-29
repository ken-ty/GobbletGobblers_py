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
            #   x--
            #   -o-
            #
            #  small
            #   ---
            #   x--
            #   o--
            #  large
            #   ---
            #   --o
            #   -x-
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0])),

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.rotate270_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)

    # 縦に線対称のStateを作成
    # - 空
    # - コマあり1
    def test_vertical_state(self):
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
            #   x--
            #   -o-
            #
            #  small
            #   -xo
            #   ---
            #   ---
            #  large
            #   ---
            #   --x
            #   -o-
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0]),
             ([0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0])),

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.vertical_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)

    # 横に線対称のStateを作成
    # - 空
    # - コマあり1
    def test_horizontal_state(self):
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
            #   x--
            #   -o-
            #
            #  small
            #   ---
            #   ---
            #   ox-
            #  large
            #   -o-
            #   x--
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0])),

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.horizontal_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)

    # 左上から斜めに線対称のStateを作成
    # - 空
    # - コマあり1
    def test_upper_left_state(self):
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
            #   x--
            #   -o-
            #
            #  small
            #   o--
            #   x--
            #   ---
            #  large
            #   -x-
            #   --o
            #   ---
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0]),
             ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0])),

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.upper_left_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)

    # 右上から斜めに線対称のStateを作成
    # - 空
    # - コマあり1
    def test_upper_right_state(self):
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
            #   x--
            #   -o-
            #
            #  small
            #   ---
            #   --x
            #   --o
            #  large
            #   ---
            #   o--
            #   -x-
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0]),
             ([0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0])),

        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 変換後の盤面をもつstateのxx_xx_pieces
            state = convert.upper_right_state(state)
            actual = (state.my_small_pieces, state.enemy_small_pieces, state.my_large_pieces, state.enemy_large_pieces)
            self.assertEqual(expect, actual)


class TestNormalizeState(unittest.TestCase):
    # 正規化(対称で最も小さい盤面に変換)したStateを作成
    # - 空
    # - my_small_pieces
    #   - 中央
    #   - 角
    #   - 辺
    # - enemy_small_pieces
    #   - 中央
    #   - 角
    #   - 辺
    # - my_large_pieces
    #   - 中央
    #   - 角
    #   - 辺
    # - enemy_large_pieces
    #   - 中央
    #   - 角
    #   - 辺
    # - my_small_piecesとenemy_small_pieces(それぞれrotate180, rotate270で最も小さくなるが、組み合わせだとrotate180が最小)
    # - my_large_piecesとenemy_large_pieces(それぞれhorizontal, rotate90で最も小さくなるが、組み合わせだとhorizontalが最小)
    # - my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces(組み合わせだとupper_leftが最小)
    def test_normalize_state(self):
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
             0b_000_000_000_000_000_000_000_000_000_000_000_000),

            # my_small_pieces(中央)
            #  small
            #   ---
            #   -o-
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   -o-
            #   ---
            (([0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_ 000_010_000 _000_000_000_000_000_000_000_000_000
             0b_000_010_000_000_000_000_000_000_000_000_000_000),

            # my_small_pieces(角)
            #  small
            #   o--
            #   ---
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   ---
            #   --o
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_ 100_000_000 _000_000_000_000_000_000_000_000_000
             0b_000_000_001_000_000_000_000_000_000_000_000_000),

            # my_small_pieces(辺)
            #  small
            #   -o-
            #   ---
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   ---
            #   -o-
            (([0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_ 010_000_000 _000_000_000_000_000_000_000_000_000
             0b_000_000_010_000_000_000_000_000_000_000_000_000),

            # enemy_small_pieces(中央)
            #  small
            #   ---
            #   -x-
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   -x-
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_ 000_010_000 _000_000_000_000_000_000
             0b_000_000_000_000_010_000_000_000_000_000_000_000),

            # enemy_small_pieces(角)
            #  small
            #   x--
            #   ---
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   ---
            #   --x
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_ 100_000_000 _000_000_000_000_000_000
             0b_000_000_000_000_000_001_000_000_000_000_000_000),

            # enemy_small_pieces(辺)
            #  small
            #   -x-
            #   ---
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   ---
            #   -x-
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_ 010_000_000 _000_000_000_000_000_000
             0b_000_000_000_000_000_010_000_000_000_000_000_000),

            # my_large_pieces(中央)
            #  large
            #   ---
            #   -o-
            #   ---
            # normalize_pieces
            #  large
            #   ---
            #   -o-
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_000_000_000_ 000_010_000 _000_000_000
             0b_000_000_000_000_000_000_000_010_000_000_000_000),

            # my_large_pieces(角)
            #  large
            #   o--
            #   ---
            #   ---
            # normalize_pieces
            #  large
            #   ---
            #   ---
            #   --o
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_000_000_000_ 100_000_000 _000_000_000
             0b_000_000_000_000_000_000_000_000_001_000_000_000),

            # my_large_pieces(辺)
            #  large
            #   -o-
            #   ---
            #   ---
            # normalize_pieces
            #  large
            #   ---
            #   ---
            #   -o-
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_000_000_000_ 010_000_000 _000_000_000
             0b_000_000_000_000_000_000_000_000_010_000_000_000),

            # enemy_large_pieces(中央)
            #  large
            #   ---
            #   -x-
            #   ---
            # normalize_pieces
            #  large
            #   ---
            #   -x-
            #   ---
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0],),  # 0b_000_000_000_000_000_000_000_000_000_ 000_010_000
             0b_000_000_000_000_000_000_000_000_000_000_010_000),

            # enemy_large_pieces(角)
            #  large
            #   x--
            #   ---
            #   ---
            # normalize_pieces
            #  large
            #   ---
            #   ---
            #   --x
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_000_000_000_000_000_000_ 100_000_000
             0b_000_000_000_000_000_000_000_000_000_000_000_001),

            # enemy_large_pieces(辺)
            #  large
            #   -x-
            #   ---
            #   ---
            # normalize_pieces
            #  large
            #   ---
            #   ---
            #   -x-
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0]),  # 0b_000_000_000_000_000_000_000_000_000_010_000_000
             0b_000_000_000_000_000_000_000_000_000_000_000_010),

            # my_small_piecesとenemy_small_pieces(それぞれrotate180, rotate270で最も小さくなるが、組み合わせだとrotate180が最小)
            #  small
            #   o--
            #   x--
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   ---
            #   -xo
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]),  # 0b_ 100_000_000 _ 000_100_000 _000_000_000_010_000_000
             0b_000_000_001_000_000_010_000_000_000_000_000_000),

            # my_large_piecesとenemy_large_pieces(それぞれhorizontal, rotate90で最も小さくなるが、組み合わせだとhorizontalが最小)
            #  large
            #   -oo
            #   --x
            #   ---
            # normalize_pieces
            #  large
            #   ---
            #   --x
            #   -oo
            (([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0]),  # 0b_000_000_000_000_000_000 _011_000_000 _ 000_001_000
             0b_000_000_000_000_000_000_000_000_011_000_001_000),

            # my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces(組み合わせだとupper_leftが最小)
            #  small
            #   --x
            #   --o
            #   --o
            #  large
            #   -oo
            #   --x
            #   ---
            # normalize_pieces
            #  small
            #   ---
            #   ---
            #   xoo
            #  large
            #   ---
            #   o--
            #   ox-
            (([0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0]),  # 0b_ 000_001_001 _ 001_000_000 _ 011_000_000 _ 000_001_000
             0b_000_000_011_000_000_100_000_100_100_000_000_010),
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # 正規化したstateのpiecesのbinary表現
            state = convert.normalize_state(state)
            actual = state.get_pieces_for_binary()
            self.assertEqual(bin(expect), bin(actual))


if __name__ == '__main__':
    unittest.main()
