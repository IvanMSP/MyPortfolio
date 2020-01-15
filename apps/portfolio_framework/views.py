# Stdlib Libraries
from datetime import timedelta

# Django Core Libraries
from django.utils import timezone

# Third Party Libraries
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView as GenericView

# Own´s Libraries
from .mixins import *
from .response import EnvelopeResponse


class GenericAPIView(GenericView):
    serializer_response_class = None


class RetrieveView(RetrieveModelMixin, GenericAPIView):
    '''
        A view to retrieve a model instance
    '''

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ListView(ListModelMixin, GenericAPIView):
    '''
        A view to list a model objects
    '''

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateView(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateView(UpdateModelMixin, GenericAPIView):
    """
        Concrete view for updating a model instance
    """

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UpdateRetrieveView(UpdateView, RetrieveView):
    pass


class UpdateCreateView(CreateView, UpdateView):
    pass


class ListCreateView(CreateView, ListView):
    pass
