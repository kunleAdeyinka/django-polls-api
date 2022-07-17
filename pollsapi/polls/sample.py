from .serializers import PollSerializer

from .models import Poll

poll_serializer = PollSerializer(
    date={"question": "Mojito or Caipirinha?", "created_by": 1}
)

poll_serializer.is_valid()

poll = poll_serializer.save()
poll_pk = poll.pk
print(poll_pk)

Poll.objects.get(poll_pk).question
