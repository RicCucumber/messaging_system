from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from .models import Message
from .permissions import IsSenderOrReceiver
from .serializers import MessageSerializer, MessageCreateSerializer
from .filters import IsReceiverFilterBackend, MessageStatusFilterBackend


class MessageViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsSenderOrReceiver, IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [IsReceiverFilterBackend, MessageStatusFilterBackend]

    def create(self, request):
        serializer = MessageCreateSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def list(self, request):
        queryset = self.filter_queryset(self.queryset)
        serializer = self.serializer_class(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def details(self, request, pk):
        message = get_object_or_404(Message, pk=pk)
        self.check_object_permissions(request, message)
        data = {'message_status': 'READ'} if request.user == message.receiver else {}
        serializer = self.serializer_class(message, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        message_pk = kwargs['pk']
        message = get_object_or_404(Message, pk=message_pk)
        self.check_object_permissions(request, message)
        message.delete()
        return JsonResponse({'status': f'success. message {message_pk} has been deleted'}, status=204)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
