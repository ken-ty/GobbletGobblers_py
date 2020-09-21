import gobbletgobblers as game


# 時計回りに90度回転
def rotate90(pieces):
    pieces = [pieces[6], pieces[3], pieces[0],
              pieces[7], pieces[4], pieces[1],
              pieces[8], pieces[5], pieces[2]]
    return pieces


# 時計回りに180度回転
def rotate180(pieces):
    pieces = [pieces[8], pieces[7], pieces[6],
              pieces[5], pieces[4], pieces[3],
              pieces[2], pieces[1], pieces[0]]
    return pieces


# 時計回りに270度回転
def rotate270(pieces):
    pieces = [pieces[2], pieces[5], pieces[8],
              pieces[1], pieces[4], pieces[7],
              pieces[0], pieces[3], pieces[6]]
    return pieces


# 縦に線対称
def vertical(pieces):
    pieces = [pieces[2], pieces[1], pieces[0],
              pieces[5], pieces[4], pieces[3],
              pieces[8], pieces[7], pieces[6]]
    return pieces


# 横に線対称
def horizontal(pieces):
    pieces = [pieces[6], pieces[7], pieces[8],
              pieces[3], pieces[4], pieces[5],
              pieces[0], pieces[1], pieces[2]]
    return pieces


# 左上から斜めに線対称
def upper_left(pieces):
    pieces = [pieces[0], pieces[3], pieces[6],
              pieces[1], pieces[4], pieces[7],
              pieces[2], pieces[5], pieces[8]]
    return pieces


# 右上から斜めに線対称
def upper_right(pieces):
    pieces = [pieces[8], pieces[5], pieces[2],
              pieces[7], pieces[4], pieces[1],
              pieces[6], pieces[3], pieces[0]]
    return pieces


# 時計回りに90度回転したStateを作成
def rotate90_state(state):
    my_small_pieces = rotate90(state.my_small_pieces)
    enemy_small_pieces = rotate90(state.enemy_small_pieces)
    my_large_pieces = rotate90(state.my_large_pieces)
    enemy_large_pieces = rotate90(state.enemy_large_pieces)
    convert_state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
    return convert_state


# 時計回りに180度回転したStateを作成
def rotate180_state(state):
    my_small_pieces = rotate180(state.my_small_pieces)
    enemy_small_pieces = rotate180(state.enemy_small_pieces)
    my_large_pieces = rotate180(state.my_large_pieces)
    enemy_large_pieces = rotate180(state.enemy_large_pieces)
    convert_state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
    return convert_state


# 時計回りに270度回転したStateを作成
def rotate270_state(state):
    my_small_pieces = rotate270(state.my_small_pieces)
    enemy_small_pieces = rotate270(state.enemy_small_pieces)
    my_large_pieces = rotate270(state.my_large_pieces)
    enemy_large_pieces = rotate270(state.enemy_large_pieces)
    convert_state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
    return convert_state


# 縦に線対称のStateを作成
def vertical_state(state):
    my_small_pieces = vertical(state.my_small_pieces)
    enemy_small_pieces = vertical(state.enemy_small_pieces)
    my_large_pieces = vertical(state.my_large_pieces)
    enemy_large_pieces = vertical(state.enemy_large_pieces)
    convert_state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
    return convert_state


# 横に線対称のStateを作成
def horizontal_state(state):
    my_small_pieces = horizontal(state.my_small_pieces)
    enemy_small_pieces = horizontal(state.enemy_small_pieces)
    my_large_pieces = horizontal(state.my_large_pieces)
    enemy_large_pieces = horizontal(state.enemy_large_pieces)
    convert_state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
    return convert_state


# 左上から斜めに線対称のStateを作成
def upper_left_state(state):
    my_small_pieces = upper_left(state.my_small_pieces)
    enemy_small_pieces = upper_left(state.enemy_small_pieces)
    my_large_pieces = upper_left(state.my_large_pieces)
    enemy_large_pieces = upper_left(state.enemy_large_pieces)
    convert_state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
    return convert_state


# 右上から斜めに線対称のStateを作成
def upper_right_state(state):
    my_small_pieces = upper_right(state.my_small_pieces)
    enemy_small_pieces = upper_right(state.enemy_small_pieces)
    my_large_pieces = upper_right(state.my_large_pieces)
    enemy_large_pieces = upper_right(state.enemy_large_pieces)
    convert_state = game.State(my_small_pieces, enemy_small_pieces, my_large_pieces, enemy_large_pieces)
    return convert_state


# 正規化したStateを作成
def normalize_state(state):
    """正規化したStateを作成する

    与えられたstateを90°, 180°, 270°回転対称、x軸, y軸対称, y=x, y=-xに線対称なstateを作成し、
    binaryに置き換えたときに最も小さくなるようなstateに変換する。
    Args:
        state: 変換したいコマの配置。

    Returns:
        state: 正規化したstate

    Examples:

        あらかじめstateを作成しておく。以下のように書くことで、正規化したstateを取得できる。
        state: 定義ずみのState型変数

        state = convert.normalize_state(state)
    """
    cand_states = [rotate90_state(state), rotate180_state(state), rotate270_state(state), vertical_state(state),
                   horizontal_state(state), upper_left_state(state), upper_right_state(state)]
    normalized_state = state
    binary_normalize_state = state.get_pieces_for_binary()
    for cand_state in cand_states:
        if binary_normalize_state > cand_state.get_pieces_for_binary():
            normalized_state = cand_state
            binary_normalize_state = cand_state.get_pieces_for_binary()
    return normalized_state


