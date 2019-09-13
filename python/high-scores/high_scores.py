# return last added score
# this assumes the score is appended and not prepended
def latest(scores):
    return scores.pop()

# returns the highest score in the list
def personal_best(scores):
    return max(scores)

# returns list of three highest scores in the scores list
def personal_top_three(scores):
    # count scores in list
    if(len(scores) > 0):
        # handle three or more scores
        if(len(scores) >= 3):
            # get the highest, store it, remove it, repeat
            highest = max(scores)
            scores.remove(max(scores))
            secondHighest = max(scores) 
            scores.remove(max(scores))
            thirdHighest = max(scores)
            return [highest, secondHighest, thirdHighest]
        elif(len(scores) == 2):
            # handle only two scores 
            highest = max(scores)
            scores.remove(max(scores))
            secondHighest = max(scores)
            return [highest, secondHighest]
        elif(len(scores) == 1):
            # handle the only score
            return [max(scores)]
    else:
        return []
