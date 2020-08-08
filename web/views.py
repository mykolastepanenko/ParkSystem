from django.shortcuts import render
from django.http import *
import web.templates
from .models import User
from .forms import *
from web.controllers import *


# Create your views here.
def index(request):
    title = "PARK SYSTEM | Система управління громадським парком"
    context = {"title": title,
               "username": request.session.get("username"), }
    return render(request, "index.html", context=context)


def admin(request):
    if request.session.get("role") == "worker":
        return HttpResponseRedirect("/forbidden")
    title = "PARK SYSTEM | Адміністратор"
    tasks = Task.objects.all()

    context = {"title": title,
               "tasks": tasks,
               "username": request.session.get("username"), }

    if request.POST:
        id = request.POST.get("id")
        title = "PARK SYSTEM | Завдання " + str(id)
        task = findTask(id)
        context = {"title": title,
                   "task": task,
                   "username": request.session.get("username"),
                   "role" : request.session.get("role"),}
        return render(request, "currentTask.html", context=context)

    if "username" in request.session:
        return render(request, "admin.html", context=context)
    else:
        return HttpResponseRedirect("/login")


def worker(request):
    if request.session.get("role") == "admin":
        return HttpResponseRedirect("/forbidden")
    title = "PARK SYSTEM | Працівник"
    tasks = Task.objects.all()
    context = {"title": title,
               "tasks": tasks,
               "username": request.session.get("username"), }

    if "username" in request.session:
        if request.POST:
            id = request.POST.get("id")
            title = "PARK SYSTEM | Завдання " + str(id)
            task = findTask(id)
            context = {"title": title,
                       "task": task,
                       "username": request.session.get("username"),
                       "role": request.session.get("role")}

            return render(request, "currentTask.html", context=context)
    else:
        return HttpResponseRedirect("/login")
    return render(request, "worker.html", context=context)


def login(request):
    title = "PARK SYSTEM | Авторизація"
    form = RegistrationForm()

    if request.POST:
        user = User.objects.get(username=request.POST.get("username"))
        request.session["username"] = user.username
        request.session["role"] = user.role
        print("name from session", request.session.get("username"))
        print("role from session", request.session.get("role"))
        return HttpResponseRedirect("/")

    context = {"title": title,
               "form": form,
               "username": request.session.get("username"),
               }
    return render(request, "login.html", context=context)


def logout(request):
    del request.session["username"]
    del request.session["role"]
    return HttpResponseRedirect("/")


def access(request):
    title = "PARK SYSTEM | Доступ заборонено!"
    username = request.session.get("username")
    context = {"title": title,
               "username": username}
    return render(request, "access.html", context=context)


def registration(request):
    title = "PARK SYSTEM | Реєстрація"
    form = RegistrationForm()
    context = {"title": title,
               "form": form}

    if request.method == "POST":
        saveNewUser(request)
        return HttpResponseRedirect("/")
    return render(request, "registration.html", context=context)


def currentTask(request):
    id = request.POST.get("id")
    title = "PARK SYSTEM | Завдання " + str(id)
    task = findTask(5)
    context = {"title": title,
               "task": task,
               "username": request.session.get("username"),
               "role": request.session.get("role"), }

    return render(request, "currentTask.html", context=context)


# ------- CRUD -------- #

def createTask(request):
    form = CreateTask()
    context = {"form": form}
    if request.method == "POST":
        createNewTask(request)
        return HttpResponseRedirect("/admin")
    return render(request, "admin.html", context=context)


def findTask(id):
    task = Task.objects.get(id=id)
    return task


def deleteTask(request):
    id = request.POST.get("id")
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect("/worker")


def deleteAllTasks(request):
    tasks = Task.objects.all()
    tasks.delete()
    return HttpResponseRedirect("/admin")


# ----------------------------------------

def acceptTask(request):
    id = request.POST.get("id")
    task = Task.objects.get(id=id)
    task.status = "Розпочато"
    task.dateStartWorker = datetime.now()
    task.save()
    # return HttpRequest().path()
    return HttpResponseRedirect("/worker")


def finishTask(request):
    id = request.POST.get("id")
    task = Task.objects.get(id=id)
    task.dateFinishWorker = datetime.now()
    task.status = "Здано"
    task.save()
    return HttpResponseRedirect("/worker")
