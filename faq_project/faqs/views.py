from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
import logging

logger = logging.getLogger(__name__)

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")
        faqs = FAQ.objects.all()
        data = [
            {
                "id": faq.id,
                **faq.get_translated_faq(lang)
            }
            for faq in faqs
        ]
        return Response(data)

    def post(self, request):
        logger.debug(f"Incoming POST request data: {request.data}")
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Invalid data provided: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FAQDetailView(APIView):
    def get(self, request, pk):
        try:
            faq = FAQ.objects.get(pk=pk)
            lang = request.GET.get("lang", "en")
            data = {
                "id": faq.id,
                **faq.get_translated_faq(lang)
            }
            return Response(data)
        except FAQ.DoesNotExist:
            logger.error(f"FAQ with id {pk} not found.")
            return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            faq = FAQ.objects.get(pk=pk)
        except FAQ.DoesNotExist:
            logger.error(f"FAQ with id {pk} not found.")
            return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)

        # If FAQ exists, attempt to update
        serializer = FAQSerializer(faq, data=request.data, partial=False)  # Full update; change to `True` if partial update needed
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.error(f"Invalid data provided: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            faq = FAQ.objects.get(pk=pk)
            faq.delete()
            return Response({"message": "FAQ deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except FAQ.DoesNotExist:
            logger.error(f"FAQ with id {pk} not found.")
            return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)
