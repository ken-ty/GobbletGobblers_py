"""盤面の列挙
    盤面を列挙し、gmlファイルに出力する。
"""

import gobbletgobblers as game
import player_ai as ai  # ゲームAI.ミニマックスによる行動.ランダムな行動.

import networkx as nx


def main():
    print()
    print("盤面の列挙を行います。")
    print("出力するファイル名を打ち込んで下さい(.gml含む):", end="")
    filename = input()

    if not filename:
        print("filenameが正常に入力されませんでした")

    # 3目並べの状態を保持するクラス"State"を初期化する。
    state = game.State()
    # グラフの初期化
    G = nx.DiGraph()
    # コマの位置をbinaryでノードに加える
    G.add_node(state.get_pieces_for_binary())
    # ゲーム終了までループ。（Stateクラスのis_doneで確認）
    while not state.is_done():
        # 行動前の状態のbinary
        # binary_state = state.get_pieces_for_binary()
        #
        # # 行動の取得
        # action_modes = ("MiniMax", "Random")
        # action_mode = action_modes[0] if state.is_first_player() else action_modes[1]
        # action = ai.action(state, action_mode)
        #
        # # 行動を状態に反映させた次の状態に更新する。
        # state = state.next(action)

        print(state)
        print()
        # ノードの追加
        G.add_node(state.get_pieces_for_binary())
        # 枝の追加
        G.add_edge(binary_state, state.get_pieces_for_binary())

    # ネットワークの出力
    nx.readwrite.gml.write_gml(G, "output/" + filename)


if __name__ == "__main__":
    main()
