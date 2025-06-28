import requests

# a = requests.get("https://solved.ac/api/v3/problem/show", params={"problemId":13705})
a = requests.get("https://solved.ac/api/v3/user/problem_stats", params={"handle" : "atopi0827"}).json()
print(a)