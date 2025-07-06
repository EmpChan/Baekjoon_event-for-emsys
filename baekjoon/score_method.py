from .models import *
from . import import_info_from_api as api
#점수 계산
def basicScore(tier,problem_tier,count,isfirst=True):
    score=None
    if tier >=18:#플레 3이상
        problem_score=problem_tier-tier**(1.2)
        if problem_score<0:
            problem_score*=1.2
        else:
            problem_score*=0.8
        score=max(0.2,problem_score+(25 if isfirst else 15)) 
    elif tier>=13:#골드 3이상
        problem_score=problem_tier-tier**(1.2)
        score=max(0.5,problem_score+(25 if isfirst else 15)) 
    elif tier>=8:#실버 3이상
        problem_score=problem_tier-tier**1
        if problem_score<0:
            problem_score*=0.8
        else:
            problem_score*=1.2
        score=max(1,problem_score+(25 if isfirst else 15)) 
    else: # 그 이하
        problem_score=problem_tier-tier**1
        if problem_score<0:
            problem_score=0
        else:
            problem_score*=1.5
        score=max(1,problem_score+(25 if isfirst else 15)) 
    
    return score*count

#API 호출해서 점수 계산 함수
def apiScore(handle):
    part = EventParticipants.objects.filter(handle=part)
    info = api.get_problem_info(handle)
    tier = (api.user_handle_info(handle)["tier"])
    score=0
    for item in info:
        score+=basicScore(tier,item["level"],item["solved"])
        score_obj = Solved.objects.filter(pid=part.pk,tier=item["level"])
        score_obj.tier_solved_cnt = item["solved"]
        score_obj.save()
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
        score = Solved.objects.filter(pid=i.pk)
        if score is None:
            makeScore(i.pk, api.get_problem_info(i.handle))
        else:
            i.score=apiScore(i.handle)
            i.save()
        
        