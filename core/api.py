from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializer import SearchSerializer
from .gpt_util import GPTUtil


class SearchAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            result = GPTUtil.search_query(serializer.data)
            return Response(result,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)