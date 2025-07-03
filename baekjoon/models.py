from django.db import models

class EventParticipants(models.Model):
    handle = models.CharField() #유저 핸들
    score = models.IntegerField() # score

    def __str__(self): #핸들과 pid 출력,,,
        return f"{self.handle} ({self.pid})"

class Solved(models.Model):
    pid = models.ForeignKey(EventParticipants, on_delete=models.CASCADE) #모델 연결 / event_participants <-> Solved
    tier = models.IntegerField() #문제의 티어
    tier_solved_cnt = models.IntegerField() #해당 티어의 문제를 푼 개수

    def __str__(self): #유저 id - 문제 티어 - 푼 개수 출력
        return f"{self.pid.pid} - Tier {self.tier} - {self.tier_solved_cnt}개"