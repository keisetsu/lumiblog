from rest_framework import serializers
from api.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True,
    #                               max_length=100)
    # text = serializers.CharField(style={'base_template': 'textarea.html'})

    # def create(self, validated_data):
    #     return Entry.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.text = validated_data.get('text', instance.text)

    #     instance.save()
    #     return instance
    class Meta:
        model = Entry
        fields = ('id', 'title', 'text')
