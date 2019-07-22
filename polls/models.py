from django.db import models

# 모델 클래스 선언 - Model 클래스 상속
class Question(models.Model):
    question_txt = models.CharField(max_length=200)     # 질문
    pub_date = models.DateTimeField('date published') # 날짜

    def __str__(self):
        return self.question_txt


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키 설정
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

"""
    __str__ : 객체를 문자열로 표현할 때 사용하는 함수
            나중에 Admin 사이트에서 테이블명을 출력하는데 그 때 사용
"""
