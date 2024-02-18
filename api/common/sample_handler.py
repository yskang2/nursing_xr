import traceback

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class SampleHandler(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SampleHandler, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print("SampleHandler GET")
        try:
           id = request.GET.get("id")
           pw = request.GET.get("pw")

           if id == "nursing_xr" and pw == "1234":
               context = {
                   "proc": "success"
               }
               return JsonResponse(context)
           else:
               context = {
                   "proc": "fail"
               }
               return JsonResponse(context, status=404)

        except Exception as e:
            context = {
                "proc": "fail",
                "message": f"An error occurred: {str(e)}"
            }
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("============== SampleHandler Fail %s", message)


    def post(self, request, *args, **kwargs):
        print("SampleHandler POST")
        try:
           print("post")
           context = {
            "proc": "post"
           }
        except Exception as e:
            context = {
                "proc": "fail",
                "message": f"An error occurred: {str(e)}"
            }
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("============== SampleHandler Fail %s", message)
        return JsonResponse(context)

    def put(self, request, *args, **kwargs):
        print("SampleHandler PUT")
        try:
           context = {
            "proc": "put"
           }
        except Exception as e:
            context = {
                "proc": "fail",
                "message": f"An error occurred: {str(e)}"
            }
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("============== SampleHandler Fail %s", message)
        return JsonResponse(context)

    def delete(self, request, *args, **kwargs):
        print("SampleHandler DELETE")
        try:
           context = {
            "proc": "delete"
           }
        except Exception as e:
            context = {
                "proc": "fail",
                "message": f"An error occurred: {str(e)}"
            }
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            print("============== SampleHandler Fail %s", message)
        return JsonResponse(context)