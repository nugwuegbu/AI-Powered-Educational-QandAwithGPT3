from rest_framework import serializers

class SearchSerializer(serializers.Serializer):

    search_text = serializers.CharField(required=True)