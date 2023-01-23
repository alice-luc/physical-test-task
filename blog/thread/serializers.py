from rest_framework import serializers
from thread.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """ Классический сериализатор модели "Пост" без примесей """

    class Meta:
        model = Post
        fields = '__all__'


class PostLWithCommentSerializer(serializers.ModelSerializer):
    """ Сериализатор модели "Пост" с дополнительным полем "latest_comment" для отображения последнего комментария """

    latest_comment = serializers.DictField()

    class Meta:
        model = Post
        fields = ('pk', 'title', 'number_of_views', 'publish_date', 'text', 'latest_comment')
