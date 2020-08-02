import evaluate_algorithm
import generate_node_all

print()
print("何をしますか")
print("1: ゲームAIの評価")
print("2: 盤面の列挙")
print("選択:", end="")
mode = input()
if mode not in {"1", "2"}:
    print("modeが正常に選択されませんでした")
elif mode == "1":
    evaluate_algorithm.main()
elif mode == "2":
    generate_node_all.main()
