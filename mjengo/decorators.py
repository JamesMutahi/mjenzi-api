from rest_framework.response import Response
from rest_framework.views import status


def validate_project_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object+
        name = args[0].request.data.get("name", "")
        contractor_email = args[0].request.data.get("contractor_email", "")
        password = args[0].request.data.get("name", "")
        if not name and not contractor_email and not password:
            return Response(
                data={
                    "message": "All fields are required to add a project"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated


def validate_material_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        name = args[0].request.data.get("name", "")
        quantity = args[0].request.data.get("quantity", "")
        if not name and not quantity:
            return Response(
                data={
                    "message": "Both name and quantity are required to add a material"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)

    return decorated


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        name = args[0].request.data.get("name", "")
        quantity = args[0].request.data.get("quantity", "")
        project = args[0].request.data.get("project", "")
        photo = args[0].request.data.get("photo", "")
        if not name and not quantity and not project and not photo:
            return Response(
                data={
                    "message": "All fields are required to add a request"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)

    return decorated
