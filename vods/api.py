from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  CreateVodSerializer, VodSerializer
import vods.selectors as vods
import vods.service as service


class VodList(APIView):
    def get(self, request):
        blob = VodSerializer(vods.get_all(), many=True)
        return Response(blob.data)

    def post(self, request):
        serializer = CreateVodSerializer(data=request.data.dict())
        if serializer.is_valid(raise_exception=True):

            print(request.data.dict())
            created_vod = service.create_vod(**serializer.validated_data)
            created_game_details = service.create_game_details(
                vod=created_vod,
                map=serializer.validated_data["map"],
                winning_team=serializer.validated_data["winning_team"],
                length=serializer.validated_data["length"],
            )
            return Response({"message": "ok"}, status=201)
