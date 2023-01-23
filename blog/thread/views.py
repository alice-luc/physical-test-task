from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from thread.serializers import PostSerializer, PostLWithCommentSerializer
from thread.models import Post, Comment


def _get_comments_details(post: Post.objects) -> list[Comment]:
	""" Получить данные о всех комментариях одного поста """
	queryset = post.comment_set.all()
	return queryset.values()


def _concatenate_post_and_comment_data(queryset: Post.objects) -> list[dict]:
	""" Собрать данные о последнем комментари каждого поста из сета """

	result = []
	for obj in queryset:
		latest_comment = obj.comment_set.latest()
		result.append({
			'pk': obj.pk,
			'title': obj.title,
			'number_of_views': obj.number_of_views,
			'text': obj.text,
			'publish_date': obj.publish_date,
			'latest_comment': latest_comment.get_short_comment_info()
		})
	return result


class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def retrieve(self, request, *args, **kwargs):
		""" GET для одного поста с его комментариями и с увеличением счетчика просмотров """
		post = self.get_object()
		serializer = PostSerializer(post)
		post.increase_num_of_views()

		return Response({**serializer.data, 'comments': _get_comments_details(post)})

	def list(self, request, *args, **kwargs):
		""" GET для списка постов с последними добавленными комментариями"""
		queryset = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(queryset)

		if page is not None:
			concatenated_response = _concatenate_post_and_comment_data(page)
			serializer = PostLWithCommentSerializer(concatenated_response, many=True)
			return self.get_paginated_response({**serializer.data})

		concatenated_response = _concatenate_post_and_comment_data(queryset)
		serializer = PostLWithCommentSerializer(concatenated_response, many=True)
		return Response(serializer.data)
