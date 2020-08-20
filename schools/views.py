from django.shortcuts import render
from .models import School,Student
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy


class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model=School
    template_name = 'schools/detail.html'
    context_object_name='school_detail'

class StudentDetailView(DeleteView):
    model = Student
    template_name='schools/std_detail.html'
    context_object_name='std_detail'

def user_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('schools:school_list'))
            else:
                return HttpResponse('YOUR ACCount is not active')
        else:
            return HttpResponse("invalid credntials")
    else:
        return render(request,'schools/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('schools:school_list'))


class SchoolCreateView(CreateView):
    model  = School
    fields = ('name','manager','location')

class SchoolUpdateView(UpdateView):
    model= School
    fields = ('name','manager')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('schools:school_list')


class StudentCreateView(CreateView):
    model= Student
    fields=('name','age','school')

class StudentUpdateView(UpdateView):
    model = Student
    fields=('name','age','school')
    

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('schools:school_list')
    #TODO success url should reverse to school detail with pk 





















'''
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            self.kwargs['school_pk']
            pk = self.kwargs.get(self.pk_url_kwarg)           
            obj = School.objects.get(pk=pk)
            n = Student.objects.raw('SELECT COUNT(*) FROM STUDENT WHERE school={}',obj)
            #students_number = obj.students
            context['students_number'] = str(n)
            return context
'''
'''
#this have no effect
    def std_num(self):
        obj_lst = School.objects.all()
        students_number = len(obj_lst)
        context = {'students_number':'students_number'}
'''
