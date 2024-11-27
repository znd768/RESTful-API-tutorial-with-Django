from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rental.models import Offer
from rental.serializers import OfferSerializer


@api_view(['GET', 'POST'])
def offer_list(request):
    if request.method == 'GET':
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def offer_detail(request, pk):
    try:
        offer = Offer.objects.get(pk=pk)
    except Offer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OfferSerializer(offer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OfferSerializer(offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)