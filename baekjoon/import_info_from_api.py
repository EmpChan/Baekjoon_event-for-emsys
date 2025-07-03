import requests


def get_problem_info(handle):
    try: 
        problem_info = requests.get("https://solved.ac/api/v3/user/problem_stats", params={"handle" : handle}).json()
        return list(problem_info)
    except requests.exceptions.Timeout as err1:
        print("Timeout Error : ", err1)
    except requests.exceptions.ConnectionError as err2:
        print("Timeout Error : ", err2)
    except requests.exceptions.HTTPError as err3:
        print("Timeout Error : ", err3)
    except requests.exceptions.TooManyRedirects as err4:
        print("Timeout Error : ", err4)
    except requests.exceptions.RequestException as err5:
        print("Timeout Error : ", err5)
    
def top_100_problem(handle):
    try: 
        top_100 = requests.get("https://solved.ac/api/v3/user/top_100", params={"handle" : handle}).json()
        return top_100
    except requests.exceptions.Timeout as err1:
        print("Timeout Error : ", err1)
    except requests.exceptions.ConnectionError as err2:
        print("Timeout Error : ", err2)
    except requests.exceptions.HTTPError as err3:
        print("Timeout Error : ", err3)
    except requests.exceptions.TooManyRedirects as err4:
        print("Timeout Error : ", err4)
    except requests.exceptions.RequestException as err5:
        print("Timeout Error : ", err5)
    
def user_handle_info(handle):
    try: 
        user_info = requests.get("https://solved.ac/api/v3/user/show", params={"handle" : handle}).json()
        return user_info
    except requests.exceptions.Timeout as err1:
        print("Timeout Error : ", err1)
    except requests.exceptions.ConnectionError as err2:
        print("Timeout Error : ", err2)
    except requests.exceptions.HTTPError as err3:
        print("Timeout Error : ", err3)
    except requests.exceptions.TooManyRedirects as err4:
        print("Timeout Error : ", err4)
    except requests.exceptions.RequestException as err5:
        print("Timeout Error : ", err5)

#problem
def num_to_problem(problem_num):
    try: 
        problem = requests.get("https://solved.ac/api/v3/problem/lookup", params={"problemIds" : [1000]}).json()
        return problem
    except requests.exceptions.Timeout as err1:
        print("Timeout Error : ", err1)
    except requests.exceptions.ConnectionError as err2:
        print("Timeout Error : ", err2)
    except requests.exceptions.HTTPError as err3:
        print("Timeout Error : ", err3)
    except requests.exceptions.TooManyRedirects as err4:
        print("Timeout Error : ", err4)
    except requests.exceptions.RequestException as err5:
        print("Timeout Error : ", err5)