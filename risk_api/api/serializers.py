from rest_framework import serializers
from .models import RiskType, Field, DataType, MetaField


class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ('name')


class MetaFieldSerializer(serializers.ModelSerializer):
    field_id = serializers.PrimaryKeyRelatedField(
        queryset=Field.objects.all(), source='field.id')

    class Meta:
        model = Field
        fields = ('key', 'value', 'field_id')


class FieldSerializer(serializers.ModelSerializer):
    meta = serializers.SerializerMethodField()
    data_type = serializers.ReadOnlyField(source='data_type.name')

    def get_meta(self, obj):
        metas = []
        for meta in obj.metafield_set.values():
            metas.append({meta['key']: meta['value']})
        return metas

    class Meta:
        model = Field
        fields = ('name', 'meta', 'data_type')


class RiskTypeSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = ('name', 'fields')
