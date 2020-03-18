from rest_framework.filters import BaseFilterBackend


class IsReceiverFilterBackend(BaseFilterBackend):
    """
    Filter that only allows users to see their received messages.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(receiver=request.user)


class MessageStatusFilterBackend(BaseFilterBackend):
    """
    Filter that only allows users to see messages with status from querystring.
    """
    def filter_queryset(self, request, queryset, view):
        message_status = request.query_params.get('message_status', None)
        return queryset.filter(message_status=message_status) if message_status else queryset
