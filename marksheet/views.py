from django.shortcuts import render
from .forms import courses

# Create your views here.
def index(request):
    form=courses()
    if request.method=="POST":
        form=courses(request.POST)
        if form.is_valid():
            c1=form.cleaned_data['course1']
            c2=form.cleaned_data['course2']
            c3=form.cleaned_data['course3']
            c4=form.cleaned_data['course4']
            c5=form.cleaned_data['course5']
            total=c1+c2+c3+c4+c5
            percentage=(total/500)*100
            if (percentage>=50):
                Division="Pass"
            else:
                Division="Fail"    
            return render(request,'marksheet/index.html',{'form':form,'total':total,'percentage':percentage,'Division':Division})
    else:
        form=courses()
    return render(request,'marksheet/index.html',{'form':form})       