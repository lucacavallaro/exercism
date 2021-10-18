def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores)[-1:-4:-1] # or sorted(scores, reverse=True)[0:3]