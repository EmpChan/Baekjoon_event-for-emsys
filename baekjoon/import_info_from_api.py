import requests

def get_problem_info(nickname):
    try: 
        a = requests.get("https://solved.ac/api/v3/user/problem_stats", params={"handle" : nickname}).json()
        return a
    except:
        return "통신 에러..."
    
def top_100_problem_rating():
    try: 
        a = requests.get("https://solved.ac/api/v3/user/top_100", params={"handle" : "atopi0827"}).json()
        print(a)
        return a
    except:
        return "통신 에러..."
    
def user_handle_info():
    try: 
        a = requests.get("https://solved.ac/api/v3/user/show", params={"handle" : "atopi0827"}).json()
        print(a)
        return a
    except:
        return "통신 에러..."


#problem
#parmas 부분 parameter로 받아서 처리?
def problem_to_num():
    try: 
        a = requests.get("https://solved.ac/api/v3/problem/lookup", params={"handle" : "atopi0827"}).json()
        print(a)
        return a
    except:
        return "통신 에러..."

def num_to_problem(problem_num):
    try: 
        a = requests.get("https://solved.ac/api/v3/problem/lookup", params={"problemIds" : problem_num}).json()
        print(a)
        return a
    except:
        return "통신 에러..."

num_to_problem(1000)