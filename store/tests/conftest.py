from charset_normalizer import api
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest

@pytest.fixture
def api_client():
    return APIClient()