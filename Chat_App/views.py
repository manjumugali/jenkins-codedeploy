import json
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404

from .models import registerUser


def index(request):             # render the index.html file
    return render(request, 'Chat_App/index.html', {})


def room(request, room_name):   # render the room.html file
    return render(request, 'Chat_App/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def base(request):              # render the base.html file
    return render(request, 'Chat_App/base.html')


def signupView(request):        # render the register.html file
    return render(request, 'Chat_App/register.html', {})


def addUser(request):           # adding the users to database using save() method
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['psw']
        all_users = registerUser(firstname=fname, lastname=lname, emailid=email, password=password)
        all_users.save()                    # insert user data into DB
        return render(request, 'Chat_App/login.html', {})


def loginView(request):         # render the login.html file
    return render(request, 'Chat_App/login.html', {})


def chatView(request):
    all_users = registerUser.objects.all()  # get all the users from database
    email = request.POST['uname']
    password = request.POST['psw']

    for user in all_users:                  # loop over users
        if user.emailid == email and user.password == password: # if emailid and password matches then log in successfully
            name = user.firstname
            return render(request, 'Chat_App/index.html', {'name': name})

    return render(request, 'Chat_App/login.html', {'error': "**invalid username and password"})
