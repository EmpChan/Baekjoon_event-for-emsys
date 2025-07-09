from .models import *
from . import import_info_from_api as api

def basicScore(tier,problem_tier,count,isfirst=True):
    score=0
    problem_base_weight = 1.5
    problem_lose = [0,0,3,8]
    minimum_score = [10,10,5,2]
    level = max(0,min((tier-3)//5,3))
    problem_score=(problem_tier-problem_lose[level]) 
    if problem_score < 0:
        problem_score = -(abs(problem_score)**1.5)
    else:
        problem_score **= 1.5
    score=max(minimum_score[level],problem_score+15) 
    w = 0
    if isfirst and count > 0:
       w=50 
    return score*count + w

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
    print(f'{pid} - well done')

def updateScore():
    partcis = EventParticipants.objects.all()
    for i in partcis:
        score = Solved.objects.filter(pid=i)
        print(f'{i} got a additional score : {score}')
        i.score+=apiScore(i)
        i.save()