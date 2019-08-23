from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .decorators import validate_material_data, validate_project_data, validate_request_data
from .models import Materials, Project, Requests
from .serializers import MaterialsSerializer, TokenSerializer, UserSerializer, ProjectSerializer, RequestSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def home(request):
    return render(request, 'home.html')


class ListCreateProjectView(generics.ListCreateAPIView):
    """
    GET projects/
    POST projects/
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny,)

    @validate_project_data
    def post(self, request, *args, **kwargs):
        username = request.data.get("name", "")
        password = request.data.get("password", "")
        email = request.data.get("contractor_email", "")
        a_project = Project.objects.create(
            name=request.data["name"],
            contractor_email=request.data["contractor_email"],
            password=request.data["password"],
            user=request.user,
        )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=ProjectSerializer(a_project).data,
            status=status.HTTP_201_CREATED
        )


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET project/:id/
    PUT project/:id/
    DELETE project/:id/
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_project = self.queryset.get(pk=kwargs["pk"])
            return Response(ProjectSerializer(a_project).data)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_project_data
    def put(self, request, *args, **kwargs):
        try:
            a_project = self.queryset.get(pk=kwargs["pk"])
            serializer = ProjectSerializer()
            updated_project = serializer.update(a_project, request.data)
            return Response(ProjectSerializer(updated_project).data)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_project = self.queryset.get(pk=kwargs["pk"])
            a_project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateMaterialsView(generics.ListCreateAPIView):
    """
    GET materials/
    POST materials/
    """
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = (permissions.AllowAny,)

    @validate_material_data
    def post(self, request, *args, **kwargs):
        a_material = Materials.objects.create(
            name=request.data["name"],
            quantity=request.data["quantity"],
        )
        return Response(
            data=MaterialsSerializer(a_material).data,
            status=status.HTTP_201_CREATED
        )


class MaterialsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET materials/:id/
    PUT materials/:id/
    DELETE materials/:id/
    """
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_material = self.queryset.get(pk=kwargs["pk"])
            return Response(MaterialsSerializer(a_material).data)
        except Materials.DoesNotExist:
            return Response(
                data={
                    "message": "Material with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_material_data
    def put(self, request, *args, **kwargs):
        try:
            a_material = self.queryset.get(pk=kwargs["pk"])
            serializer = MaterialsSerializer()
            updated_material = serializer.update(a_material, request.data)
            return Response(MaterialsSerializer(updated_material).data)
        except Materials.DoesNotExist:
            return Response(
                data={
                    "message": "Material with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_material = self.queryset.get(pk=kwargs["pk"])
            a_material.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Materials.DoesNotExist:
            return Response(
                data={
                    "message": "Material with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateRequestView(generics.ListCreateAPIView):
    """
    GET projects/
    POST projects/
    """
    queryset = Requests.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.AllowAny,)

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_request = Requests.objects.create(
            name=request.data["name"],
            quantity=request.data["quantity"],
            photo=request.data["photo"],
            project=request.data["project"],
            location=request.data["location"],
        )
        return Response(
            data=RequestSerializer(a_request).data,
            status=status.HTTP_201_CREATED
        )


class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET requests/:id/
    PUT requests/:id/
    DELETE requests/:id/
    """
    queryset = Requests.objects.all()
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            return Response(RequestSerializer(a_request).data)
        except Requests.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            serializer = RequestSerializer()
            updated_request = serializer.update(a_request, request.data)
            return Response(RequestSerializer(updated_request).data)
        except Requests.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            a_request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Requests.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """

    # This permission class will over ride the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=UserSerializer(new_user).data, status=status.HTTP_201_CREATED
        )
