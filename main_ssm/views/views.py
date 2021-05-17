from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class Test(APIView):
    def get(self, request):
        res = {
            "Piyush":"Hello world this is Piyush Kumar"
        }
        return Response(res, status=status.HTTP_200_OK)
