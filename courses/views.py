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

Nodejs_Videos_Link = {'Video_1': 'https://www.youtube.com/embed/PiU1mqhRd6k',
                    'Video_2': 'https://www.youtube.com/embed/7FdSe67Ucuw',
                    'Video_3': 'https://www.youtube.com/embed/WTu9BYBAsFs',
                    'Video_4': 'https://www.youtube.com/embed/3UlHlgl7Z_I',
                    'Video_5': 'https://www.youtube.com/embed/SvrO49XFtCg'
                        }

Nodejs_Videos_Titles = {'Video_1': 'Getting Started || Urdu/Hindi || Mudasir Ali || Nodejs tut#1',
                'Video_2': 'Objects, Functions in Nodejs || Urdu/Hindi || Mudasir Ali || Nodejs tut#2',
                'Video_3': 'Modules in Nodejs || Urdu/Hindi || Mudasir Ali || Nodejs tut#3',
                'Video_4': 'Express in Nodejs || Urdu/Hindi || Mudasir Ali || Nodejs tut#4',
                'Video_5': 'Nodemon in Nodejs || Urdu/Hindi || Mudasir Ali || Nodejs tut#5',
                'Video_6': 'This sis node rifhted',
                'Empty': ''}

Nodejs_Videos_Descryptions = {'Video_1': 'Hey Guys. This is the first video of Nodejs course. In this i will give you a little introduction of Nodejs. And you will learn how to install Nodejs.',
                        'Video_2': 'Hey Guys. This is the Second video of Nodejs course. In this video you will learn Objects and Functions in JavaScript. Because Objects and Functions are important in Nodejs thats why i maked this video.',
                        'Video_3': 'Hey Guys. This is the Third video of Nodejs course. In this video I will tell you what are Modules, And how to use them in nodejs.',
                        'Video_4': 'Hey Guys. This is the Fourth video of Nodejs course. In this video I will tell you what express, and why to use it.',
                        'Video_5': 'Hey Guys. This is the Fifth video of Nodejs course. In this video I will tell you what is nodemon, and why to use it.'
                        }

Nodejs_Links = []

for i in range(1, len(Nodejs_Videos_Titles.keys())):
    Nodejs_Links.append(str(f'Nodejs_{i}'))


Code_Download_Nodejs = {'Video_1': '/Downloads/Codes/Courses/Nodejs/1.js'}


Nodejs_Course_Content = []

for i in range(1, len(Nodejs_Videos_Titles.keys())):
    Nodejs_Course_Content.append(str(Nodejs_Videos_Titles.get(f'Video_{i}')))


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
    Context = {'title': Nodejs_Videos_Titles.get('Video_1'),
                'desc': Nodejs_Videos_Descryptions.get('Video_1'),
                'video_link': Nodejs_Videos_Link.get('Video_1'),
                'code_download': Code_Download_Nodejs.get('Video_1'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[0],
                'next_link': Nodejs_Links[1],
                }
    return render(req, 'courses/Nodejs/1.html', Context)

def Nodejs_2(req):
    Context = {'title': Nodejs_Videos_Titles.get('Video_2'),
                'desc': Nodejs_Videos_Descryptions.get('Video_2'),
                'video_link': Nodejs_Videos_Link.get('Video_2'),
                'code_download': Code_Download_Nodejs.get('Video_2'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[0],
                'next_link': Nodejs_Links[1],
                }
    return render(req, 'courses/Nodejs/2.html', Context)

def Nodejs_3(req):
    Context = {'title': Nodejs_Videos_Titles.get('Video_3'),
                'desc': Nodejs_Videos_Descryptions.get('Video_3'),
                'video_link': Nodejs_Videos_Link.get('Video_3'),
                'code_download': Code_Download_Nodejs.get('Video_3'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[0],
                'next_link': Nodejs_Links[1],
                }
    return render(req, 'courses/Nodejs/3.html', Context)

def Nodejs_4(req):
    Context = {'title': Nodejs_Videos_Titles.get('Video_4'),
                'desc': Nodejs_Videos_Descryptions.get('Video_4'),
                'video_link': Nodejs_Videos_Link.get('Video_4'),
                'code_download': Code_Download_Nodejs.get('Video_4'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[0],
                'next_link': Nodejs_Links[1],
                }
    return render(req, 'courses/Nodejs/4.html', Context)

def Nodejs_5(req):
    Context = {'title': Nodejs_Videos_Titles.get('Video_5'),
                'desc': Nodejs_Videos_Descryptions.get('Video_5'),
                'video_link': Nodejs_Videos_Link.get('Video_5'),
                'code_download': Code_Download_Nodejs.get('Video_5'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[0],
                'next_link': Nodejs_Links[1],
                }
    return render(req, 'courses/Nodejs/5.html', Context)


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
