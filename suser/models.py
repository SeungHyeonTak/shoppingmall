from django.db import models


class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=54, verbose_name='비밀번호')
    register_data = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'shopping_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
