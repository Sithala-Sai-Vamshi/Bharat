from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_faq(self, lang):
        if lang == "hi":
            return {
                "question": self.question_hi if self.question_hi else self.question,
                "answer": self.answer_hi if self.answer_hi else self.answer,
            }
        elif lang == "bn":
            return {
                "question": self.question_bn if self.question_bn else self.question,
                "answer": self.answer_bn if self.answer_bn else self.answer,
            }
        return {
            "question": self.question,
            "answer": self.answer,
        }

    def __str__(self):
        return self.question[:50]

from googletrans import Translator

def save(self, *args, **kwargs):
    translator = Translator()
    if not self.question_hi:
        self.question_hi = translator.translate(self.question, src='en', dest='hi').text
    if not self.answer_hi:
        self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text

    if not self.question_bn:
        self.question_bn = translator.translate(self.question, src='en', dest='bn').text
    if not self.answer_bn:
        self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text

    super().save(*args, **kwargs)

