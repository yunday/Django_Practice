from django.contrib import admin
# from .models import Question, Choice
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,               {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]    # 포인트는 inline! Question안에서 편집되게함
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 열에 정보 표기하는것
    list_filter = ['pub_date'] # 변경 목록 필터링 가능하게 해줌
    search_fields = ['question_text']   # question_text로 검색가능하게 해줌

admin.site.register(Question, QuestionAdmin)
