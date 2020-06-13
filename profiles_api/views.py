from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api view"""

    def get(self,request,format=None):
        """returns a list of api view feature """

        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,delete,put,delete)',
            'Is similar to traditional DjangoView',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
