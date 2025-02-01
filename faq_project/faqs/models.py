# models.py
from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    question_hi = models.CharField(max_length=200, blank=True, null=True)
    question_bn = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.question
    
    def get_translated_faq(self, lang='en'):
        if lang == 'hi':
            return {"question": self.question_hi or self.question, "answer": self.answer}
        elif lang == 'bn':
            return {"question": self.question_bn or self.question, "answer": self.answer}
        else:
            return {"question": self.question, "answer": self.answer}
