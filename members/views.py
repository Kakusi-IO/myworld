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

# delete/{{ x.id }}のidは第二引数として渡る
def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

# 変更画面へ転送
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# dbを編集して、indexへ転送
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))