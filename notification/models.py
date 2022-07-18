from django.db import models
import requests
from bs4 import BeautifulSoup

html = requests.get("https://cyber.wku.ac.kr/Cyber/ComBoard_V005/Content/list.jsp?gid=1115983888724&bid=1115985252888")
html.raise_for_status()
html.encoding='utf-8'
bsObject = BeautifulSoup(html.content, "html.parser")

print(bsObject.table.tbody)

'''class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)'''

    