import math
import import_info_from_api as api
#점수 계산
def Basic_Score(tier,problem_tier,count,isfirst=True):
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
def ApiScore(nickname):
    info = api.get_problem_info(nickname)
    tier = (api.user_handle_info(nickname)["tier"])
    score=0
    for item in info:
        score+=Basic_Score(tier,item["level"],item["solved"])
    return score
