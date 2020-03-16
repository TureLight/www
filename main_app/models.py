from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class PicturePools(models.Model):
    """
    图片分类
    """
    name = models.CharField('图片名称', max_length=252)
    tags = models.CharField('标签', default='动漫图片', max_length=2000)
    author = models.CharField('作者', default='admin', max_length=80)
    stars = models.IntegerField('评分', default=0)
    MD5 = models.CharField('md5值', max_length=128)
    mini_path = models.CharField('缩略图路径', max_length=500)
    view_path = models.CharField('浏览图路径', max_length=500)
    download_path = models.CharField('下载图路径', max_length=500)
    create_time = models.DateField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    operator = models.CharField('修改记录', max_length=20, default='admin')
    is_delete = models.BooleanField('是否删除', default=False)

    class Meta:
        db_table = 'picture_pools'
        verbose_name = '图片池'
        verbose_name_plural = '图片池'

    def __str__(self):
        return self.name

