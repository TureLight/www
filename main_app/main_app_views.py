from django.shortcuts import render
from main_app.models import PicturePools
# Create your views here.


def view_page(request):

    # 今日图片区域
    pic_path = ['/home/github/media/timg.jpg',
                '/home/github/media/timg(1).jpg',
                '/home/github/media/timg(2).jpg',
                '/home/github/media/timg(3).jpg',
                '/home/github/media/timg(4).jpg',
                '/home/github/media/timg(5).jpg',
                '/home/github/media/timg(6).jpg',
                '/home/github/media/timg(7).jpg'
                ]
    temp_list = []
    # for i in pic_path:

    return render(request, 'main_app/view_page.html', context={'update_path': pic_path})
