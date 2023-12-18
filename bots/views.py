import logging

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from bots import services
from schedules import models as api_models

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(message)s",
    level=logging.ERROR,
)


class HoraroAPIView(GenericAPIView):
    queryset = api_models.Schedule.objects.all().select_related("group")

    schema = None
    _telegram_service = services.Telegram()

    def post(self, request, *args, **kwargs):
        data = self.request.data
        try:
            self._telegram_service.handle(data)
        except Exception:
            logging.exception(
                "Exception occurred"
            )  # write in the 'app.log' file
            self._telegram_service.send_error_message(data)
        return Response("Ok", status=200)
