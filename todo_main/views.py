from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    # print(tasks)
    #get - only 1 data will be fetched
    #filter - mulltiple data fetched
    #all - all the data will be fetched

    completed_tasks=Task.objects.filter(is_completed=True)

    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }

    # return HttpResponse("homepage")
    return render(request,'home.html',context)