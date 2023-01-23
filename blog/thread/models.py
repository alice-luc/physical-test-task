from django.db import models


class Post(models.Model):
	""" Публикация пользователя на сайте """
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Текст поста')
	number_of_views = models.SmallIntegerField(verbose_name='Количество просмотров', editable=False, default=0)
	publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, editable=False)

	objects = models.Manager()

	def __str__(self):
		return self.title

	def __int__(self):
		return self.number_of_views

	class Meta:
		db_table = 'post'
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

	def increase_num_of_views(self):
		self.number_of_views += 1
		self.save()


class Comment(models.Model):
	""" Комментарий к конкретной публикации на сайте """
	text = models.TextField(verbose_name='Текст комментария')
	publish_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, editable=False)
	post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)

	objects = models.Manager()

	def get_short_comment_info(self):  # для получения урезанного объекта с вьюхи
		return {f'{self.pk}': self.text}

	class Meta:
		db_table = 'comment'
		get_latest_by = 'publish_date'
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
