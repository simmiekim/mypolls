from django.contrib import admin

from .models import Question, Choice
# 현재 폴더에 models 모듈에서(models.py) Question, Choice 가져오기

# Question, Choice 한 화면에서 변경하기
class ChoiceInline(admin.StackedInline):
    model = Choice
    # extra = 2

# class ChoiceInline(admin.TabularInline):  # 테이블형식으로 보여주기
#     model = Choice
#     extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    # list_display = ('question_txt', 'pub_date') # 리스트 형식 출력

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

