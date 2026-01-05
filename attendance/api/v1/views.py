from ...models import User,Employee,Department
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action, permission_classes
from django.db import IntegrityError, transaction
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from django.core.mail import send_mail
from django.conf import settings
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.viewsets import GenericViewSet
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from ...permissions import *
from django.core.cache import cache
from ...utils import *
from datetime import timedelta