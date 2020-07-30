import gobbletgobblers as game  # クラスStateを定義.
import player_ai as ai  # ゲームAI.ミニマックスによる行動.ランダムな行動.
import networkx as nx

# パラメータ
EP_GAME_COUNT = 1  # 1評価当たりのゲーム数


def first_player_point(ended_state):
    """先手プレイヤーのポイント
    """
    # 1:先手勝利, 0: 先手敗北, 0.5, 引分け
    if ended_state.is_lose():
        return 0 if ended_state.is_first_player() else 1
    return 0.5


def play(action_modes):
    """1ゲームの実行
    """
    # 3目並べの状態を保持するクラス"State"を初期化する。
    state = game.State()
    G = nx.DiGraph()
    # コマの位置をタプルでノードに加える
    G.add_node((tuple(state.my_small_pieces), tuple(state.enemy_small_pieces), tuple(state.my_large_pieces),
                tuple(state.enemy_large_pieces)))
    print("number of nodes:", G.number_of_nodes())
    print(G.nodes())
    print("number of edges:", G.number_of_edges())
    print(G.edges())
    print("sparse adjacency matrix:")
    print(nx.adjacency_matrix(G))
    print("dence adjacency matrix:")
    print(nx.adjacency_matrix(G).todense())

    # ゲーム終了までループ。（Stateクラスのis_doneで確認）
    while not state.is_done():
        # 行動の取得
        action_mode = action_modes[0] if state.is_first_player() else action_modes[1]
        action = ai.action(state, action_mode)

        # 行動を状態に反映させた次の状態に更新する。
        state = state.next(action)

        print(state)
        print()
        G.add_node((tuple(state.my_small_pieces), tuple(state.enemy_small_pieces), tuple(state.my_large_pieces),
                    tuple(state.enemy_large_pieces)))
        print(G.nodes())
        print()

    # 先手プレイヤーのポイントを返す
    return first_player_point(state)


def evaluate_algorithm_of(label, action_modes):
    """任意のアルゴリズムの評価
    """
    # 複数回の対戦を繰り返す
    total_point = 0
    total_win = 0
    total_lose = 0
    total_draw = 0
    point = 0
    for i in range(EP_GAME_COUNT):
        # 1ゲームの実行
        # 交互に先手後手を入れ替えている。
        if i % 2 == 0:
            point = play(action_modes)
        else:
            point = 1 - play(list(reversed(action_modes)))
        # win,lose,drawをカウントする
        total_point += point
        if point == 1:
            total_win += 1
        elif point == 0.5:
            total_draw += 1
        elif point == 0:
            total_lose += 1
        # 出力
        print("\rEvaluate {}/{} ".format(i + 1, EP_GAME_COUNT), end='')
    print('')

    # 平均ポイントの計算
    average_point = total_point / EP_GAME_COUNT
    print(label.format(average_point), end='')
    print(' (win {}, lose {}, draw {})'.format(total_win, total_lose, total_draw))


# ミニマックスVSミニマックス
action_modes = ("MiniMax", "MiniMax")
evaluate_algorithm_of('MiniMax_VS_MiniMax {:.3f}', action_modes)

# ミニマックスVSランダム
# action_modes = ("MiniMax", "Random")
# evaluate_algorithm_of('MiniMax_VS_Random {:.3f}', action_modes)


# # ランダムVSランダム
# action_modes = ("Random", "Random")
# evaluate_algorithm_of('Random_VS_Random {:.3f}', action_modes)
