from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='previews/', verbose_name='изображение')
    date = models.DateField(auto_now_add=True, verbose_name='дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} - {self.body[:100]} ({self.date})'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        permissions = [
            ('change_blog_status', 'Can change blog theme status')
        ]
