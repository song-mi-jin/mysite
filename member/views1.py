#from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from member.models import Mem
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage

class MemListView(ListView):
    model = Mem
    ## 모델명(소문자)_list.html
    template_name = 'member/list.html'
    ## object_list 로 객체 반환
    

class MemAddView(CreateView):
    model = Mem
    fields = ['Mem_id','Mem_name', 'Mem_pwd', 'Mem_img']
    success_url = reverse_lazy('member:list')
    template_name = 'member/add.html'

##def add(request):
##    if request.method == "POST":
##        
##        if request.FILES:
##            mem_img = request.FILES['upload_files'].name
##            fs = FileSystemStorage(location='member/', base_url='member/')
##            # FileSystemStorage.save(file_name, file_content)
##            filename = fs.save(mem_img, request.FILES['upload_files'])
##            uploaded_file_url = fs.url(filename)
##            print(uploaded_file_url)
##        else:
##            mem_img = ''
##        qry = Mem(Mem_id=request.POST['mem_id'], Mem_name=request.POST['mem_name'],\
##                  Mem_pwd=request.POST['mem_pwd'], Mem_img=mem_img)
##        qry.save()
##        return HttpResponseRedirect(reverse('member:list'))
##
##    else:
##        return render(request, 'member/add.html')


class MemDetailView(DetailView):
    model = Mem
    ## 모델명(소문자)_detail.html
    template_name = 'member/detail.html'
    ## object 로 객체 반환

class MemEditView(UpdateView):
    model = Mem
    fields = ['Mem_name', 'Mem_pwd', 'Mem_img']
    template_name = 'member/edit.html'
    ##success_url = reverse_lazy('member:list')


class MemRemoveView(DeleteView):
    model = Mem
    success_url = reverse_lazy('member:list')
    
def login(request):

    if request.method == "POST":

        m = Mem.objects.get(Mem_id=request.POST['mem_id'])
        if m.Mem_pwd == request.POST['mem_pwd']:
            ## 일치 하는 값이 있으면 로그인 처리
            request.session['member_id'] = m.Mem_id
            request.session.set_expiry(300)
            print(request.session.get_expiry_date())
            return HttpResponseRedirect(reverse('member:login_ok'))
        else:
            return HttpResponse("Your username and password didn't match.")

        #return HttpResponseRedirect(reverse('member:login_ok'))

    else:
        return render(request, 'member/login.html')


def login_ok(request):

    member = Mem.objects.get(Mem_id=request.session['member_id'])
    return render(request, 'member/login_ok.html', {'member': member})


def logout(request):

    if request.session['member_id']:
        #request.session.flush()
        del request.session['member_id']
        return HttpResponseRedirect(reverse('member:login'))
    else:
        pass



