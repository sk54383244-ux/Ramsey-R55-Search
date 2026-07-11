import random

# 정점 43개, 마지막 핀셋 타격 모드
num_nodes = 43
all_possible_pairs = [(i, j) for i in range(num_nodes) for j in range(i+1, num_nodes)]

# 핀셋 모드: 5000회만 빠르게 돌려 세션 종료 방지
def get_violations(edges):
    bad = []
    for _ in range(5000):
        nodes = random.sample(range(num_nodes), 5)
        edges_in_set = sum(1 for a in range(5) for b in range(a+1, 5) 
                           if (nodes[a], nodes[b]) in edges or (nodes[b], nodes[a]) in edges)
        if edges_in_set == 10 or edges_in_set == 0: bad.append(nodes)
    return bad

current_edges = set(random.sample(all_possible_pairs, len(all_possible_pairs) // 2))

print(f"🔥 [43개 최종 핀셋 타격] 마지막 승부수! 🔥")

for gen in range(1, 2001):
    violations = get_violations(current_edges)
    if not violations:
        print(f"\n🎉 대성공! 43개 정점 정복 완료!")
        break
    
    # 핀셋 타격: 가장 마지막에 발견된 지뢰의 간선만 타격
    target = violations[-1]
    pair = (target[random.randint(0,4)], target[random.randint(0,4)])
    if pair[0] != pair[1]:
        if pair in current_edges: current_edges.remove(pair)
        else: current_edges.add(pair)
    
    if gen % 200 == 0: print(f"🧬 진행중... 현재 지뢰 {len(violations)}개")

print(f"=== 탐색 종료 ===")
