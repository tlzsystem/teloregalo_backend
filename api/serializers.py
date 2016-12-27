from rest_framework import serializers
from category.models import Category
from publication.models import Publication
from status.models import Status

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name')

class PublicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id','category_id','user_creator','status','publish_date','title','description')

class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id','status_name')