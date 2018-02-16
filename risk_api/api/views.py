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
        serializer = self.serializer_class(risk_type)
        return Response(serializer.data)


class RiskTypeList(APIView):

    authentication_classes = ()
    permission_classes = ()
    queryset = None
    serializer_class = RiskTypeSerializer

    def get(self, request, format=None):
        risk_types = RiskType.objects.all()
        serializer = self.serializer_class(risk_types, many=True)
        return Response(serializer.data)
