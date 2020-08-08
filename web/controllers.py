from .models import *
from datetime import datetime


# ----------  save info into database   -----------

def saveNewUser(request):
    people = User.objects.all()

    bool
    isUser = False

    for val in people:
        if val.username == request.POST.get("username"):
            isUser = True
            print("Пользователь уже зарегистрирован")
            break
    if isUser == False:
        newUser = User.objects.create(email=request.POST.get("email"),
                                      username=request.POST.get("username"),
                                      password=request.POST.get("password"),
                                      firstname=request.POST.get("firstname"),
                                      lastname=request.POST.get("lastname"),
                                      role="worker")
        print("Регистрация прошла успешно!")


def createNewTask(request):
    task = Task()
    task.name = request.POST.get("name")
    task.desc = request.POST.get("desc")
    task.dateStartAdmin = datetime.now()
    task.dateFinishAdmin = request.POST.get("dateFinishAdmin")
    task.dateStartWorker = None
    task.dateFinishWorker = None
    task.status = "Не здано"
    task.save()
    print("Новое задание добавлено успешно")



# ----------  get info from database   -----------

# def getAllTasks():
#     task = Task.objects.all()
#     return task


