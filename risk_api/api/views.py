from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import RiskType
from api.serializers import RiskTypeSerializer


class RiskTypeDetail(APIView):

    authentication_classes = ()
    permission_classes = ()
    queryset = None
    serializer_class = RiskTypeSerializer

    def get(self, request, pk, format=None):
        risk_type = RiskType.objects.get(pk=pk)
        serializer = self.serializer_class(instance=risk_type)
        return Response(serializer.data)
