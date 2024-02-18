import traceback
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, permissions


class SampleViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):

    def list(self, request, *args, **kwargs):
        try:
            data = {
                "proc": "list"
            }
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("==================== SampleViewSet create Fail %s", message)
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": f"{e}"}
            )
        return Response(status=status.HTTP_201_CREATED, data=data)

    def create(self, request, *args, **kwargs):
        try:
            data = {
                "proc": "create"
            }
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("==================== SampleViewSet create Fail %s", message)
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": f"{e}"}
            )
        return Response(status=status.HTTP_201_CREATED, data=data)

    def update(self, request, *args, **kwargs):
        try:
            print("update")
            print(kwargs.get("pk"))
            #  https://localhost:8000/id/
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("==================== SampleViewSet update Fail %s", message)
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": f"{e}"}
            )
        data = {
            "proc": "update",
            "id": kwargs.get("pk"),
        }
        return Response(status=status.HTTP_200_OK, data=data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            print("delete")
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("==================== SampleViewSet destroy Fail %s", message)
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": f"{e}"}
            )
        data = {
            "proc": "delete",
            "id": kwargs.get("pk"),
        }
        return Response(status=status.HTTP_200_OK, data=data)