from rest_framework.status import *
from rest_framework.views  import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.
class mcq_data(APIView):
    

    def get(self,request):
        mcq_data = mcqs.objects.order_by("?")[:31]
        mcq_data = mcqsSerializer(mcq_data,many=True)
        return Response(mcq_data.data,status=HTTP_200_OK)

    def post(self,request):
        user_data = user_outputSerializer(data=request.data)
        if user_data.is_valid():
            user_data.save()
            return Response({"status_code":200,"Data":user_data.data},status=HTTP_200_OK)
        return Response({"status_code":406,"Exception" : "Incorrent formate"})
    


class user_login(APIView):
    
    def get(self,request):
        try:
            if not request.data:
                return Response({"status_code":428,"Exception":"Please post name and password."},status=HTTP_428_PRECONDITION_REQUIRED)
            try:
                login_details = Users.objects.get(name=request.data['name'],passw=request.data['passw'])
            
            except:
                return Response({"status_code":404,"No user found":"No such user details found"},status=HTTP_404_NOT_FOUND)
            login_details = UsersSerializer(login_details)
            return Response({"status_code":200,"Data":login_details.data},status=HTTP_200_OK)
        except:
            return Response({"status_code":404,"Exception":"invalid parameter request"},status=HTTP_404_NOT_FOUND)
            
            
    
    def post(self,request):
        new_data = UsersSerializer(data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response({"status_code":200,"Data":new_data.data},status=HTTP_200_OK)
        return Response({"status_code":406,"Exception" : "Incorrent formate"})
    
    

    def patch(self,request):
        try:
            update_data = Users.objects.get(id=request.data['id'])
        except:
            return Response({"Exception": "id not provided"},status=HTTP_428_PRECONDITION_REQUIRED)
        update_data = UsersSerializer(update_data,data=request.data,partial=True)
        if update_data.is_valid():
            update_data.save()
            return Response(update_data.data,status=HTTP_200_OK)
        return Response({"Exception":"Invalid formate"},status=HTTP_304_NOT_MODIFIED)
    
    

    def delete(self,request):
        try:
            delete_data = Users.objects.get(id=request.data['id'])
        except:
            return Response({"Exception": "id not provided"},status=HTTP_428_PRECONDITION_REQUIRED)
        delete_data.delete()
        return Response({"Task":"Content deleted successful"},status=HTTP_200_OK)        
        