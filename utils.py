def compute_score(solution, need):
    sol_kw = set(k.lower() for k in solution["keywords"])
    need_kw = set(k.lower() for k in need["keywords"])
    overlap = len(sol_kw & need_kw)
    max_possible = min(len(sol_kw), len(need_kw))
    if max_possible == 0:
        return 0
    return round(overlap / max_possible, 2)


def score_label(s):
    if s >= 0.6:
        return "high", "Strong match"
    if s >= 0.3:
        return "medium", "Partial match"
    return "low", "Weak match"


def stars(n, max_n=5):
    return "⭐" * n + "☆" * (max_n - n)
