from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Members

#defines index.html
def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    # 辞書のキーはindex.htmlで使う変数
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context, request))

# defines add.html
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):

  # リクエスト元のデータを取得
  x = request.POST['first']
  y = request.POST['last']

  # dbに登録
  member = Members(firstname=x, lastname=y)
  member.save()

  # 別のhtmlを作らず、既存のindex.htmlへ移行
  return HttpResponseRedirect(reverse('index'))