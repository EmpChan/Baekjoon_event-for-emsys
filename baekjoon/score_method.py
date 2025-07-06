from .models import *
from . import import_info_from_api as api

def basicScore(tier,problem_tier,count,isfirst=True):
    score=0
    problem_base_weight = [1,1,1.1,1.1]
    problem_additional_weight_upper_zero = [1.35,1.1,1,0.95]
    problem_additional_weight_under_zero = [0,0.9,1,1.05]
    minimum_score = [1,1,0.5,0.2]
    level = max(0,min((tier-3)//5,3))
    problem_score=problem_tier-tier**(problem_base_weight[level])
    if problem_score < 0:
        problem_score*=problem_additional_weight_under_zero[level]
    else:
        problem_score*=problem_additional_weight_upper_zero[level]
    score=max(minimum_score[level],problem_score+15) 
    
    return score*count + 5 if isfirst else 0 

#API 호출해서 점수 계산 함수
def apiScore(obj):
    part = EventParticipants.objects.filter(handle=obj.handle)
    info = api.get_problem_info(obj.handle)
    tier = (api.user_handle_info(obj.handle)["tier"])
    score=0
    is_first=True
    for item in info:
        score_obj = Solved.objects.get(pid=obj,tier=item["level"])
        score+=basicScore(int(tier),int(item["level"]),int(item["solved"]-score_obj.tier_solved_cnt),is_first)
        score_obj.tier_solved_cnt = item["solved"]
        score_obj.save()
        if score:
            is_first = False
    return score

def makeScore(pid,tiers):
    for i in tiers:
        solved_obj = Solved.objects.create(
            pid=pid,
            tier = i['level'],
            tier_solved_cnt= i['solved']
        ).save()

def updateScore():
    partcis = EventParticipants.objects.all()
    for i in partcis:
        print(i)
        score = Solved.objects.filter(pid=i)
        i.score+=apiScore(i)
        i.save()
        print(i)