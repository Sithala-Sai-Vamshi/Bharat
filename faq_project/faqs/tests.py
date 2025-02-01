from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import FAQ

class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )
    
    def test_get_faq_list(self):
        response = self.client.get("/api/faqs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_faq(self):
        data = {"question": "What is REST API?", "answer": "It is a web API architecture."}
        response = self.client.post("/api/faqs/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FAQ.objects.count(), 2)

    def test_update_faq(self):
        data = {"question": "Updated Django Question"}
        response = self.client.put(f"/api/faqs/{self.faq.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.faq.refresh_from_db()
        self.assertEqual(self.faq.question, "Updated Django Question")

    def test_delete_faq(self):
        response = self.client.delete(f"/api/faqs/{self.faq.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FAQ.objects.count(), 0)
