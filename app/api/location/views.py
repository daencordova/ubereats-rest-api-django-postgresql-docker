from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import LocationModel
from .serializers import LocationSerializer


class LocationListView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        locations = LocationModel.objects.all()
        serializer = LocationSerializer(locations, many=True)

        return Response(
            {"data": serializer.data, "message": "Ok"}, status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors, "message": "Data sent not valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        return Response(
            {"data": serializer.data, "message": "Location added"},
            status=status.HTTP_201_CREATED,
        )


class LocationDetailView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return LocationModel.objects.get(pk=pk)
        except LocationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        location = self.get_object(pk)

        if not location:
            return Response(
                {"message": "Location does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = LocationSerializer(location)
        return Response(
            {"data": serializer.data, "message": "Ok"}, status=status.HTTP_200_OK
        )

    def put(self, request, pk, format=None):
        location = self.get_object(pk)

        if not location:
            return Response(
                {"message": "Location does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = LocationSerializer(location, data=request.data)

        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors, "message": "Data sent not valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        return Response(
            {"data": serializer.data, "message": "Location modified"},
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)

        if not location:
            return Response(
                {"message": "Location does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        location.delete()
        return Response({"message": "Location deleted"}, status=status.HTTP_200_OK)
