from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import getInsights

@api_view(['GET'])
def searchWithChatGPT(request):
    print(request)

    # get the query from the request
    query = request.GET.get('query')

    # query the index based on the query
    queryResponse = getInsights(query)

    # return a test string
    return Response({"insights": queryResponse})

