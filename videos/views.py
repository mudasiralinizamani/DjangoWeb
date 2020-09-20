from django.shortcuts import render

# Create your views here.

Brief = 'Full Stack Developer'

Name = 'Mudasir Ali'

Titles = ['', 'Input Animation With HTML & CSS', 'Instagram Login Automation With Python & Selenium ', 'This Bot will get FOLLOWERS for you. ']

Descyptions = {'Video_1': 'In this video, I will tell you. How to create an Animated Input in Html CSS.',
                'Video_2': 'In this video, I am creating a Instagram Login Automation Program. Code is provided.',
                'Video_3': 'In this video, I will tell you. How to create an Instagram bot that will get followers for you.'
                }

Thumbnails = {'MudasirAli': 'Pics/my-pic.jpg', 'Video_1': 'Pics/Pages/Videos/input_animation_with_html_and_css.jpg', 'Video_2': 'Pics/Pages/Videos/instagram_login_automation.png', 'Video_3': 'Pics/Pages/Videos/this_bot_will_get_followers_for_you.png', }

Dates = {'Video_1': 'Aug 14, 2020', 'Video_2': 'Sep 1, 2020', 'Video_3': 'Sep 6, 2020'}

Links = {'Video_1': 'Video_1', 'Video_2': 'Video_2', 'Video_3': 'Video_3'}

Video_Links = {'Video_1': 'https://www.youtube.com/embed/nER0LN0gIKY'}
Code_Download = {'Video_1': ['Downloads/Codes/Videos/Video_1/Index.html', ''], }

def Videos(req):
    Context = {'name': Name, 'video_1_title': Titles[1], 'video_2_title': Titles[2], 'video_3_title': Titles[3],
               'brief': Brief, 'video_1_desc': Descyptions.get('Video_1'), 'video_2_desc': Descyptions.get('Video_2'), 'video_3_desc': Descyptions.get('Video_3'),
               'mudasir': Thumbnails.get('MudasirAli'),   'video_1_thumb': Thumbnails.get('Video_1'), 'video_2_thumb': Thumbnails.get('Video_2'), 'video_3_thumb': Thumbnails.get('Video_3'),
               'video_1_date': Dates.get('Video_1'), 'video_2_date': Dates.get('Video_2'), 'video_3_date': Dates.get('Video_3'),
               'video_1_link': Links.get('Video_1'),  'video_2_link': Links.get('Video_2'),  'video_3_link': Links.get('Video_3'),
               }
    return render(req, 'Pages/Videos.html', Context)


def Video_1(req):
    Context = {'title': f'{Titles[1]} || Urdu/Hindi || Mudasir Ali',
                'desc': Descyptions.get('Video_1'),
                'video_link': Video_Links.get('Video_1'),
                'code_download': Code_Download.get('Video_1')[0],
                }
    return render(req, 'videos/Video_1.html', Context)

def Video_2(req):
    pass

def Video_3(req):
    pass