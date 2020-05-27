def latest(scores):
    if not scores:
        return "There's no score in the ranking..."
    
    return scores[-1] ## I'm assuming that when you put a new score in the list, you will use append method


def personal_best(scores):
    if not scores:
        return "There's no score in the ranking..."
    
    return max(scores)


def personal_top_three(scores):
    if not scores:
        return "There's no score in the ranking..."
    if len(scores) <= 3:
        return sorted(scores, reverse=True)[:len(scores)]
    
    return sorted(scores, reverse=True)[:3]
