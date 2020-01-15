# coding: utf8

# Third-party Libraries
from rest_framework import (mixins, status)
from rest_framework.response import Response

# Own´s Libraries
from accounts.models import User
from continuity_framework.response import EnvelopeResponse


class TokenMixin(object):
    """
        Retrieve a user instance related to
        the provided token or returns None
    """
    def get_request_user(self, request, *args, **kwargs):
        if request.method == 'POST':
            token = self.request.POST.get('token')
        elif request.method == 'GET':
            token = self.request.GET.get('token')
        else:
            token = None
        if token is not None:
            try:
                user = User.objects.get(token=token)
            except User.DoesNotExist:
                return None
        else:
            return None
        return user


class RetrieveModelMixin(mixins.RetrieveModelMixin, TokenMixin):
    """
        Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if self.serializer_response_class is not None:
            serializer = self.serializer_response_class(instance, context=self.context)
        return EnvelopeResponse(serializer.data)


class ListModelMixin(mixins.ListModelMixin, TokenMixin):
    """
        List a queryset
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        if self.serializer_response_class is not None:
            serializer = self.serializer_response_class(queryset, many=True, context=self.context)
        return EnvelopeResponse(serializer.data)


class CreateModelMixin(mixins.CreateModelMixin):
    """
        Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if self.serializer_response_class is not None:
            serializer = self.serializer_response_class(serializer.instance, context=self.context)
        return EnvelopeResponse(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class UpdateModelMixin(mixins.UpdateModelMixin):
    """
        Update a model instance
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)  # NOQA
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        if self.serializer_response_class is not None:
            serializer = self.serializer_response_class(instance, context=self.context)
        return EnvelopeResponse(serializer.data)
