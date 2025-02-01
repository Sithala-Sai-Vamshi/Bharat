from django.db import models
from django.core.cache import cache

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    question_hi = models.CharField(max_length=200, blank=True, null=True)
    question_bn = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.question
    
    def get_translated_faq(self, lang='en'):
        """Retrieve translated FAQ with caching support."""
        cache_key = f"faq_{self.id}_lang_{lang}"  

        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        if lang == 'hi':
            translation = {"question": self.question_hi or self.question, "answer": self.answer}
        elif lang == 'bn':
            translation = {"question": self.question_bn or self.question, "answer": self.answer}
        else:
            translation = {"question": self.question, "answer": self.answer}

        cache.set(cache_key, translation, timeout=3600)

        return translation
