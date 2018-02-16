from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from api.models import RiskType
from api.serializers import RiskTypeSerializer


class GetRiskType(APITestCase):
    fixtures = ['sample_data']

    def setUp(self):
        self.client = APIClient()

    def test_get_risk_type(self):
        response = self.client.get('/risk_type/1/')
        risk_type = RiskType.objects.get(pk=1)
        serializer = RiskTypeSerializer(risk_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
