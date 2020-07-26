# coding=utf-8
import unittest
import gobbletgobblers as game


class TestState(unittest.TestCase):

    # 表示がちゃんとできているか
    def test___str__(self):
        patterns = [
            # 空
            ((None, None, None, None),
             " small\n"     #  small
             "  ---\n"      #   ---
             "  ---\n"      #   ---
             "  ---\n  "    #   ---
             "\r large\n"   #  large
             "  ---\n"      #   ---
             "  ---\n"      #   ---
             "  ---\n  "    #   ---
             "\r   ↓\n\n"   #    ↓

             "visible\n"    # visible
             "  ---\n"      #   ---
             "  ---\n"      #   ---
             "  ---\n  "),  #   ---

            # smallのみ
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], None, None),
             " small\n"     #  small
             "  ox-\n"      #   ox-
             "  ---\n"      #   ---
             "  ---\n  "    #   ---
             "\r large\n"   #  large
             "  ---\n"      #   ---
             "  ---\n"      #   ---
             "  ---\n  "    #   ---
             "\r   ↓\n\n"   #    ↓

             "visible\n"    # visible
             "  ox-\n"      #   ox-
             "  ---\n"      #   ---
             "  ---\n  "),  #   ---

            # small, large重なりなし
            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]),
             " small\n"     #  small
             "  ox-\n"      #   ox-
             "  ---\n"      #   ---
             "  ---\n  "    #   ---
             "\r large\n"   #  large
             "  ---\n"      #   ---
             "  ox-\n"      #   ox-
             "  ---\n  "    #   ---
             "\r   ↓\n\n"   #    ↓

             "visible\n"    # visible
             "  ox-\n"      #   ox-
             "  ox-\n"      #   ox-
             "  ---\n  "),  #   ---

            # small, large重なりあり
            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]),
             " small\n"     #  small
             "  ox-\n"      #   ox-
             "  ---\n"      #   ---
             "  ox-\n  "    #   ox-
             "\r large\n"   #  large
             "  ---\n"      #   ---
             "  ox-\n"      #   ox-
             "  ox-\n  "    #   ox-
             "\r   ↓\n\n"   #    ↓

             "visible\n"    # visible
             "  ox-\n"      #   ox-
             "  ox-\n"      #   ox-
             "  ox-\n  "),  #   ox-

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

    # 表示がちゃんとできているか
    def test_legal_actions(self):
        patterns = [
            ((None, None, None, None),),
            #  small
            #   ---
            #   ---
            #   ---
            #  large
            #   ---
            #   ---
            #   ---
            #    ↓
            # visible
            #   ---
            #   ---
            #   ---

            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], None, None),
             " small\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "
             "\r large\n"
             "  ---\n"
             "  ---\n"
             "  ---\n  "
             "\r   ↓\n\n"
             "visible\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "),  # smallのみ

            (([1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0]),
             " small\n"
             "  ox-\n"
             "  ---\n"
             "  ox-\n  "
             "\r large\n"
             "  ---\n"
             "  ox-\n"
             "  ox-\n  "
             "\r   ↓\n\n"
             "visible\n"
             "  ox-\n"
             "  ox-\n"
             "  ox-\n  "),  # small, large重なりあり

            (([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0]),
             " small\n"
             "  ox-\n"
             "  ---\n"
             "  ---\n  "
             "\r large\n"
             "  ---\n"
             "  ox-\n"
             "  ---\n  "
             "\r   ↓\n\n"
             "visible\n"
             "  ox-\n"
             "  ox-\n"
             "  ---\n  "),  # small, large重なりなし
        ]
        for input_param, expect_param in patterns:
            my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces = input_param
            state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
            expect = expect_param  # expect_param == string
            actual = str(state)
            self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
