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

Current = 1

# Nodejs Variables - Mudasir Ali
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


Code_Download_Nodejs = {'Video_1': '/Downloads/Codes/Courses/Nodejs/1.js',
                        'Video_2': '/Downloads/Codes/Courses/Nodejs/2.js',
                        'Video_3': '/Downloads/Codes/Courses/Nodejs/3.js',
                        'Video_4': '/Downloads/Codes/Courses/Nodejs/4.js',
                        'Video_5': '/Downloads/Codes/Courses/Nodejs/5.js',
                        }


Nodejs_Course_Content = []

for i in range(1, len(Nodejs_Videos_Titles.keys())):
    Nodejs_Course_Content.append(str(Nodejs_Videos_Titles.get(f'Video_{i}')))


# Go Variables - Mudasir Ali
Go_Videos_Link = {'Video_1': 'https://www.youtube.com/embed/pm-DIuch-Lg',
                    'Video_2': 'https://www.youtube.com/embed/iooR46XU-4c',
                    'Video_3': 'https://www.youtube.com/embed/Whn73byNVfA',
                    'Video_4': 'https://www.youtube.com/embed/Rfchi-aFsWc',
                    'Video_5': 'https://www.youtube.com/embed/483BSQyYdF8',
                    'Video_6': 'https://www.youtube.com/embed/muGnKPG5gAw',
                    'Video_7': 'https://www.youtube.com/embed/iA4h3YsLmKI',
                    'Video_8': 'https://www.youtube.com/embed/gLmMviOTU0Q',
                        }

Go_Videos_Titles = {'Video_1': 'Installing Golang | Urdu/Hindi | Mudasir Ali | Golang tut#1',
                'Video_2': 'Syntax of Golang | Urdu/Hindi | Mudasir Ali | Golang tut#2 ',
                'Video_3': 'Variables | Urdu/Hindi | Mudasir Ali | Golang tut#3 ',
                'Video_4': 'Functions | Urdu/Hindi | Mudasir Ali | Golang tut#4',
                'Video_5': 'If else | Hindi/Urdu | Mudasir Ali | Golang tut#5',
                'Video_6': 'switch, loop, break and continue | Urdu/Hindi | Mudasir Ali | Golang tut#6',
                'Video_7': 'Variable Scope, Struct | Hindi/Urdu | Mudasir Ali | Golang tut#7',
                'Video_8': 'Pointers in Go | Hindi/Urdu | Mudasir Ali | Golang tut#8',
                'Empty': ''}

Go_Videos_Descryptions = {'Video_1': ' Hi Guys. This is the series of Golang. In this series i will teach you Go language. This is the First Video of this series in this video you will learn how to install golang on machine.',
                        'Video_2': ' Hello Guys. This is the Second video of our Golang series. In this video i will tell you about the syntax of golang and some other things.',
                        'Video_3': 'Hello Guys. This is the Third video of our Golang series. In this video i will tell you about Variables of golang.',
                        'Video_4': 'This is the Fourth video of our Golang series. In this video you will learn about the functions of golang.',
                        'Video_5': 'Hey Guys. This is the Fifth video of our Golang series. In this video i will tell you about the if else in golang.',
                        'Video_6': 'This is the Sixth video of our Golang series. In this video i will tell you about what is switch and what is loop, how it works and i will tell you also what is break and continue keyword.',
                        'Video_7': 'This is the Seventh video of our Golang series. In this video i will tell you the scope of variables in golang and what is struct and how it works.',
                        'Video_8': "This is the Edith video of our golang series. In this video you 've/will learn about Pointers in golang.",
                        }

Go_Links = []

for i in range(1, len(Go_Videos_Titles.keys())):
    Go_Links.append(str(f'Go_{i}'))


Go_Code_Download = {'Video_1': '/Downloads/Codes/Courses/Go/1.go',
                        'Video_2': '/Downloads/Codes/Courses/Go/2.go',
                        'Video_3': '/Downloads/Codes/Courses/Go/3.go',
                        'Video_4': '/Downloads/Codes/Courses/Go/4.go',
                        'Video_5': '/Downloads/Codes/Courses/Go/5.go',
                        'Video_6': '/Downloads/Codes/Courses/Go/6.go',
                        'Video_7': '/Downloads/Codes/Courses/Go/7.go',
                        'Video_8': '/Downloads/Codes/Courses/Go/8.go'
                        }


Go_Course_Content = []

for i in range(1, len(Go_Videos_Titles.keys())):
    Go_Course_Content.append(str(Go_Videos_Titles.get(f'Video_{i}')))


# Deno Variables - Mudasir ALi
Deno_Videos_Link = {'Video_1': 'https://www.youtube.com/embed/OTA_Z-WV-8E',
                    'Video_2': 'https://www.youtube.com/embed/BClhx8qlPFw',
                    'Video_3': 'https://www.youtube.com/embed/VQ6qbEieV4s',
                        }

Deno_Videos_Titles = {'Video_1': 'Deno: Getting Started | Installing deno | Urdu/Hindi | Mudasir Ali | Deno tut#1',
                'Video_2': 'Landing Code | Urdu/Hindi | Mudasir Ali | Deno tut#2',
                'Video_3': ' How to import library and modules in deno | Urdu/Hindi | Mudasir Ali | Deno tut#3',
                'Empty': ''}

Deno_Videos_Descryptions = {'Video_1': 'This is the first video of deno series. In this series i will teach you deno framework from scratch. And in this video i will give you a little intro of deno and i will tell you how to install deno.',
                        'Video_2': 'This is the Second video of deno series. In this series i will tell you what the deno previous code do.',
                        'Video_3': 'Hello Guys. This is the Second video of deno series. In this series i will tell you what the deno previous code do. ',
                        }

Deno_Links = []

for i in range(1, len(Deno_Videos_Titles.keys())):
    Deno_Links.append(str(f'Deno_{i}'))


Deno_Code_Download = {'Video_1': '/Downloads/Codes/Courses/Deno/1.ts',
                        'Video_2': '/Downloads/Codes/Courses/Deno/2.ts',
                        'Video_3': '/Downloads/Codes/Courses/Deno/3.ts',
                        }


Deno_Course_Content = []

for i in range(1, len(Deno_Videos_Titles.keys())):
    Deno_Course_Content.append(str(Deno_Videos_Titles.get(f'Video_{i}')))

# Ethical Hacking Variables - Mudasir Ali

EthicalHacking_Videos_Link = {'Video_1': 'https://www.youtube.com/embed/ueaCLbrD7Go',
                    'Video_2': 'https://www.youtube.com/embed/EWFzrjTr_V0',
                        }

EthicalHacking_Videos_Titles = {'Video_1': 'Introduction to Hacking | Urdu/Hindi | Mudasir Ali | EthicalHacking tut#1 ',
                'Video_2': 'Terminal | Urdu/Hindi | Mudasir Ali | EthicalHacking tut#2 ',
                'Empty': ''}

EthicalHacking_Videos_Descryptions = {'Video_1': 'This is the first video of Ethical Hacking course. In this video i will give you an Introduction of What is Hacking, how many types of hacking And How many types of hackers.',
                        'Video_2': 'This is the second video of Ethical Hacking course. In this video i will tell you what is terminal. And some basic commands.',
                        }

EthicalHacking_Links = []

for i in range(1, len(EthicalHacking_Videos_Titles.keys())):
    EthicalHacking_Links.append(str(f'EthicalHacking_{i}'))


EthicalHacking_Course_Content = []

for i in range(1, len(EthicalHacking_Videos_Titles.keys())):
    EthicalHacking_Course_Content.append(str(EthicalHacking_Videos_Titles.get(f'Video_{i}')))


# Selenium Variables - Mudasir Ali

Selenium_Videos_Link = {'Video_1': 'https://www.youtube.com/embed/H06VWHWsOjc',
                    'Video_2': 'https://www.youtube.com/embed/OnSjWwvkRPk',
                        }

Selenium_Videos_Titles = {'Video_1': ' What is Selenium?, Installing Selenium | Urdu\Hindi | Mudasir Ali | Selenium tut#1 ',
                'Video_2': ' Accessing Elements | Urdu\Hindi | Mudasir Ali | Selenium tut#2',
                'Empty': ''}

Selenium_Videos_Descryptions = {'Video_1': 'This is the first video of our selenium series and in this video i will tell you what is selenium and how we can install it.',
                        'Video_2': 'So this is the second video of our selenium course. In this video i will tell you how to Access the elements in selenium.',
                        }

Selenium_Links = []

for i in range(1, len(Selenium_Videos_Titles.keys())):
    Selenium_Links.append(str(f'Selenium_{i}'))


Selenium_Code_Download = {'Video_1': '/Downloads/Codes/Courses/Selenium/1.py',
                        'Video_2': '/Downloads/Codes/Courses/Selenium/2.py',
                        }


Selenium_Course_Content = []

for i in range(1, len(Selenium_Videos_Titles.keys())):
    Selenium_Course_Content.append(str(Selenium_Videos_Titles.get(f'Video_{i}')))



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
                'current': Current,
                }
    return render(req, 'Courses/Nodejs/1.html', Context)

def Nodejs_2(req):
    Current = 2
    Context = {'title': Nodejs_Videos_Titles.get('Video_2'),
                'desc': Nodejs_Videos_Descryptions.get('Video_2'),
                'video_link': Nodejs_Videos_Link.get('Video_2'),
                'code_download': Code_Download_Nodejs.get('Video_2'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[0],
                'next_link': Nodejs_Links[2],
                'current': Current,
                }
    return render(req, 'Courses/Nodejs/2.html', Context)

def Nodejs_3(req):
    Current = 3
    Context = {'title': Nodejs_Videos_Titles.get('Video_3'),
                'desc': Nodejs_Videos_Descryptions.get('Video_3'),
                'video_link': Nodejs_Videos_Link.get('Video_3'),
                'code_download': Code_Download_Nodejs.get('Video_3'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[1],
                'next_link': Nodejs_Links[3],
                'current': Current,
                }
    return render(req, 'Courses/Nodejs/3.html', Context)

def Nodejs_4(req):
    Current = 4
    Context = {'title': Nodejs_Videos_Titles.get('Video_4'),
                'desc': Nodejs_Videos_Descryptions.get('Video_4'),
                'video_link': Nodejs_Videos_Link.get('Video_4'),
                'code_download': Code_Download_Nodejs.get('Video_4'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[2],
                'next_link': Nodejs_Links[4],
                'current': Current,
                }
    return render(req, 'Courses/Nodejs/4.html', Context)

def Nodejs_5(req):
    Current = 5
    Context = {'title': Nodejs_Videos_Titles.get('Video_5'),
                'desc': Nodejs_Videos_Descryptions.get('Video_5'),
                'video_link': Nodejs_Videos_Link.get('Video_5'),
                'code_download': Code_Download_Nodejs.get('Video_5'),
                'course_content': Nodejs_Course_Content,
                'prev_link': Nodejs_Links[3],
                'next_link': Nodejs_Links[4],
                'current': Current,}
    return render(req, 'Courses/Nodejs/5.html', Context)


# Go Courses Functions - Mudasir Ali
def Go_1(req):
    Context = {'title': Go_Videos_Titles.get('Video_1'),
            'desc': Go_Videos_Descryptions.get('Video_1'),
            'video_link': Go_Videos_Link.get('Video_1'),
            'code_download': Go_Code_Download.get('Video_1'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[0],
            'next_link': Go_Links[1],
            'current': Current,}
    return render(req, 'Courses/Go/1.html', Context)

def Go_2(req):
    Context = {'title': Go_Videos_Titles.get('Video_2'),
            'desc': Go_Videos_Descryptions.get('Video_2'),
            'video_link': Go_Videos_Link.get('Video_2'),
            'code_download': Go_Code_Download.get('Video_2'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[0],
            'next_link': Go_Links[2],
            'current': Current,}
    return render(req, 'Courses/Go/2.html', Context)

def Go_3(req):
    Context = {'title': Go_Videos_Titles.get('Video_3'),
            'desc': Go_Videos_Descryptions.get('Video_3'),
            'video_link': Go_Videos_Link.get('Video_3'),
            'code_download': Go_Code_Download.get('Video_3'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[1],
            'next_link': Go_Links[3],
            'current': Current,}
    return render(req, 'Courses/Go/3.html', Context)

def Go_4(req):
    Context = {'title': Go_Videos_Titles.get('Video_4'),
            'desc': Go_Videos_Descryptions.get('Video_4'),
            'video_link': Go_Videos_Link.get('Video_4'),
            'code_download': Go_Code_Download.get('Video_4'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[2],
            'next_link': Go_Links[4],
            'current': Current,}
    return render(req, 'Courses/Go/4.html', Context)

def Go_5(req):
    Context = {'title': Go_Videos_Titles.get('Video_5'),
            'desc': Go_Videos_Descryptions.get('Video_5'),
            'video_link': Go_Videos_Link.get('Video_5'),
            'code_download': Go_Code_Download.get('Video_5'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[3],
            'next_link': Go_Links[5],
            'current': Current,}
    return render(req, 'Courses/Go/5.html', Context)

def Go_6(req):
    Context = {'title': Go_Videos_Titles.get('Video_6'),
            'desc': Go_Videos_Descryptions.get('Video_6'),
            'video_link': Go_Videos_Link.get('Video_6'),
            'code_download': Go_Code_Download.get('Video_6'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[4],
            'next_link': Go_Links[6],
            'current': Current,}
    return render(req, 'Courses/Go/6.html', Context)

def Go_7(req):
    Context = {'title': Go_Videos_Titles.get('Video_7'),
            'desc': Go_Videos_Descryptions.get('Video_7'),
            'video_link': Go_Videos_Link.get('Video_7'),
            'code_download': Go_Code_Download.get('Video_7'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[5],
            'next_link': Go_Links[7],
            'current': Current,}
    return render(req, 'Courses/Go/7.html', Context)

def Go_8(req):
    Context = {'title': Go_Videos_Titles.get('Video_8'),
            'desc': Go_Videos_Descryptions.get('Video_8'),
            'video_link': Go_Videos_Link.get('Video_8'),
            'code_download': Go_Code_Download.get('Video_8'),
            'course_content': Go_Course_Content,
            'prev_link': Go_Links[6],
            'next_link': Go_Links[7],
            'current': Current,}
    return render(req, 'Courses/Go/2.html', Context)



# Deno Courses Functions - Mudasir Ali
def Deno_1(req):
    Context = {'title': Deno_Videos_Titles.get('Video_1'),
            'desc': Deno_Videos_Descryptions.get('Video_1'),
            'video_link': Deno_Videos_Link.get('Video_1'),
            'code_download': Deno_Code_Download.get('Video_1'),
            'course_content': Deno_Course_Content,
            'prev_link': Deno_Links[0],
            'next_link': Deno_Links[1],
            'current': Current,}
    return render(req, 'Courses/Deno/1.html', Context)

def Deno_2(req):
    Context = {'title': Deno_Videos_Titles.get('Video_2'),
            'desc': Deno_Videos_Descryptions.get('Video_2'),
            'video_link': Deno_Videos_Link.get('Video_2'),
            'code_download': Deno_Code_Download.get('Video_2'),
            'course_content': Deno_Course_Content,
            'prev_link': Deno_Links[0],
            'next_link': Deno_Links[2],
            'current': Current,}
    return render(req, 'Courses/Deno/2.html', Context)

def Deno_3(req):
    Context = {'title': Deno_Videos_Titles.get('Video_3'),
            'desc': Deno_Videos_Descryptions.get('Video_3'),
            'video_link': Deno_Videos_Link.get('Video_3'),
            'code_download': Deno_Code_Download.get('Video_3'),
            'course_content': Deno_Course_Content,
            'prev_link': Deno_Links[1],
            'next_link': Deno_Links[2],
            'current': Current,}
    return render(req, 'Courses/Deno/2.html', Context)



# EthicalHacking Courses Functions - Mudasir Ali
def EthicalHacking_1(req):
    Context = {'title': EthicalHacking_Videos_Titles.get('Video_1'),
            'desc': EthicalHacking_Videos_Descryptions.get('Video_1'),
            'video_link': EthicalHacking_Videos_Link.get('Video_1'),
            'course_content': EthicalHacking_Course_Content,
            'prev_link': EthicalHacking_Links[0],
            'next_link': EthicalHacking_Links[1],
            'current': Current,}
    return render(req, 'Courses/EthicalHacking/1.html', Context)

def EthicalHacking_2(req):
    Context = {'title': EthicalHacking_Videos_Titles.get('Video_2'),
            'desc': EthicalHacking_Videos_Descryptions.get('Video_2'),
            'video_link': EthicalHacking_Videos_Link.get('Video_2'),
            'course_content': EthicalHacking_Course_Content,
            'prev_link': EthicalHacking_Links[0],
            'next_link': EthicalHacking_Links[1],
            'current': Current,}
    return render(req, 'Courses/EthicalHacking/2.html', Context)





# Selenium Courses Functions - Mudasir Ali
def Selenium_1(req):
    Context = {'title': Selenium_Videos_Titles.get('Video_1'),
            'desc': Selenium_Videos_Descryptions.get('Video_1'),
            'video_link': Selenium_Videos_Link.get('Video_1'),
            'code_download': Selenium_Code_Download.get('Video_1'),
            'course_content': Selenium_Course_Content,
            'prev_link': Selenium_Links[0],
            'next_link': Selenium_Links[1],
            'current': Current,}
    return render(req, 'Courses/Selenium/1.html', Context)

def Selenium_2(req):
    Context = {'title': Selenium_Videos_Titles.get('Video_2'),
            'desc': Selenium_Videos_Descryptions.get('Video_2'),
            'video_link': Selenium_Videos_Link.get('Video_2'),
            'code_download': Selenium_Code_Download.get('Video_2'),
            'course_content': Selenium_Course_Content,
            'prev_link': Selenium_Links[0],
            'next_link': Selenium_Links[1],
            'current': Current,}
    return render(req, 'Courses/Selenium/2.html', Context)
