# messaging_system

python3.7

API endpoints:
POST /messages/new/ - create new message
GET /messages/ - list all messages
GET /messages?message_status=(READ|UNREAD) - list messages by status
GET /messages/{{message_id}}/ - read message
DELETE /messages/{{message_id}}/ - delete message
