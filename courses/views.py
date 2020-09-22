from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Variable - Mudasir ALi

Names = ['', 'Selenium', 'Ethical Hacking', 'Deno', 'Go', 'Nodejs']

Descryptions = {'Selenium': 'Hello Friends. This is the Course Selenium with Python. In this course you will learn Selenium Python. Source code will be provided.',
                'Ethical Hacking': 'This is the Course of EthicalHacking. In this course you will learn Ethical Hacking from beginner to advance. With Ethical Hacking Examples.',
                'Deno': 'In this course. I will teach you Deno Framework from beginner to advance and with practices. Source code will be provided.',
                'Go': 'Hi. This is the course of Golang. In this course, I will teach you Go language fully and with practices. Source code will be provided.',
                'Nodejs': ' Hey. This is the Course of Nodejs. In this course, you will learn Nodejs from beginner to advance and the source will be provided.'}

Thumbnails = {'Selenium': 'Pics/Pages/Courses/selenium.png',
              'Ethical Hacking': 'Pics/Pages/Courses/hacking.jpg',
              'Deno': 'Pics/Pages/Courses/deno.svg',
              'Go': 'Pics/Pages/Courses/go.png',
              'Nodejs': 'Pics/Pages/Courses/nodejs.jpg'}

# Nodejs Variables

Nodejs_Videos_Link = {}

Nodejs_Titles = {'Video_1': '', 'Video_2': '', 'Video_3': '', 'Video_4': '', 'Video_5': ''}

Nodejs_Descryptions = {'Video_1': '',
                        'Video_2': '',
                        'Video_3': '',
                        'Video_4': ''
                        }

Nodejs_Link = ['', '']

Code_Download_Nodejs = {}

# Go Variables

# Deno Variables

# Ethical Hacking Variables

# Selenium Variables



# Courses Main Function - Mudasir Ali
def Courses(req):
    Context = {'name_1': Names[1], 'name_2': Names[2], 'name_3': Names[3], 'name_4': Names[4], 'name_5': Names[5],
                'desc_1': Descryptions.get('Selenium'), 'desc_2': Descryptions.get('Ethical Hacking'), 'desc_3': Descryptions.get('Deno'), 'desc_4': Descryptions.get('Go'), 'desc_5': Descryptions.get('Nodejs'),
                'thumb_1': Thumbnails.get('Selenium'), 'thumb_2': Thumbnails.get('Ethical Hacking'), 'thumb_3': Thumbnails.get('Deno'), 'thumb_4': Thumbnails.get('Go'), 'thumb_5': Thumbnails.get('Nodejs')}

    return render(req, 'Pages/Courses.html', Context)

# Nodejs Courses Functions - Mudasir Ali
def Nodejs_1(req):
    Context = {}
    return render(req, 'courses/Nodejs/1.html', Context)


# Go Courses Functions - Mudasir Ali
def Go_1(req):
    return HttpResponse("This is the courses page")


# Deno Courses Functions - Mudasir Ali
def Deno_1(req):
    return HttpResponse("This is the courses page")


# EthicalHacking Courses Functions - Mudasir Ali
def EthicalHacking_1(req):
    return HttpResponse("This is the courses page")


# Selenium Courses Functions - Mudasir Ali
def Selenium_1(req):
    return HttpResponse("This is the courses page")
