from rest_framework import status
from card.models import FlashCard
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from card.serializers import (
    CreateFlashCardSerializer,
    UpdateFlashCardSerializer,
    ListFlashCardSerializer,
)

class CreateFlashCardView(APIView):

    permission_class = (IsAuthenticated,)

    def post(self, request):
        serializer = CreateFlashCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UpdateFlashCardView(APIView):

    permission_class = (IsAuthenticated,)


    def put(self, request, id):
        flash_card = get_object_or_404(FlashCard, id=id)
        serializer = UpdateFlashCardSerializer(
            data=request.data,
            instance=flash_card,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteFlashCardView(APIView):

    permission_class = (IsAuthenticated,)

    def delete(self, request, id):
        flash_card = get_object_or_404(FlashCard, id=id)
        flash_card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListFlashCardView(APIView):

    permission_class = (IsAuthenticated,)

    def get(self, request, user_id):
        all_flash_card_user = get_list_or_404(FlashCard, user__id=user_id)
        serializer = ListFlashCardSerializer(all_flash_card_user, many=True)
        return Response(serializer.data)
