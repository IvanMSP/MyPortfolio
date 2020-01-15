# Std Libraries
from collections import OrderedDict

# Third-party Libraries
from rest_framework import pagination
from continuity_framework.response import EnvelopeResponse


class LimitOffsetPagination(pagination.LimitOffsetPagination):

    max_page_size = 20

    def get_paginated_response(self, data):
        return EnvelopeResponse(OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
