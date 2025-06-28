import requests

def get_problem_info(handle):
    a = requests.get("https://solved.ac/api/v3/user/problem_stats", params={"handle" : "atopi0827"}).json()
    print(a)

    try: 
        a = requests.get("url~", params={"handle":"atopi0827"}).json()
        return a
    except:
        return "통신 에러..~"