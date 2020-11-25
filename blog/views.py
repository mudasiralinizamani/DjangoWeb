from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

AboutMe = "Hey my name is Mudasir Ali. And I am a full stack web developer. If you want to know more about me"

Brief = ""

Tittles = ['',
            '7 best FREE ALTERNATIVES of Adobe Premiere Pro',
            '6 Most Popular JavaScript Libraries in 2020',
            '7 Skills You Need as a JavaScript Developer in 2020 ',
            'Top 4 Dying PROGRAMMING LANGUAGES in 2020',
            'Top 5 Website Builder Apps (IOS & Android) | 2020 September',
            '10 Most Popular Programming Languages & Their Uses (2020 October)',
            ]

Another_Title = ['',
            '7 best FREE ALTERNATIVES of Adobe Premiere Pro',
            '6 Most Popular JavaScript Libraries in 2020',
            '7 Skills You Need as a JavaScript Developer in 2020 ',
            'Top 4 Dying PROGRAMMING LANGUAGES in 2020',
            'Top 5 Website Builder Apps (IOS & Android) | 2020 September',
            '10 Most Popular Programming Languages & Their Uses (2020 October)',
            ]

Dates = {'Post_1': '13 Aug, 2020', 'Post_2': '21 Aug, 2020', 'Post_3': '23 Aug, 2020', 'Post_4': '5 Sep, 2020', 'Post_5': '30 Sep, 2020', 'Post_6': '10 Oct, 2020'}

Descriptions = {'Post_1': "Hey, Are you looking FREE ALTERNATIVES of Adobe Premiere Pro. In this blog I will tell you 7 best FREE ALTERNATIVES of Adobe Premiere Pro.",
                'Post_2': "Hey, In this blog, I 'am going to tell you 6 Most Popular JavaScript Libraries in 2020. So lets get started.",
                'Post_3': "Hey, In this blog, I 'am going to tell you, 7 Skills You Need as a JavaScript Developer in 2020 . So lets get started.",
                'Post_4': "Hey, In this blog, I 'am going to tell you, Top Four Dying PROGRAMMING LANGUAGES in 2020. So lets get started.",
                'Post_5': 'so we know that the traditional way of building a website has always been on a laptop or a desktop computer but, nowadays we all have powerful computers sitting comfortably in our pockets and surprisingly enough there are in fact free apps that you can use to build a website in the palm of your hand. So in this blog I will tell you top 5 (ANDROID & IOS) apps to create websites.',
                'Post_6': "In this blog, I'm going to share with you the 10 most popular programming languages and what they're used for now, I've taken these rankings from GitHub based on the most popular poll request languages in quarter two of 2020. So ideally this will give us the best idea of the current, most popular programming languages.",
                }

Thumbnails = {'Post_1': 'Pics/Pages/Blogs/Premier-Pro.jpg',
                'Post_2': 'Pics/Pages/Blogs/js-1.jpg',
                'Post_3': 'Pics/Pages/Blogs/js-1.jpg',
                'Post_4': 'Pics/Pages/Blogs/languages.png',
                'Post_5': 'Pics/Pages/Blogs/top-5-app-to-build-websites.png',
                'Post_6': 'Pics/Pages/Blogs/post_6.jpg',
                }

Links = {'Post_1': '7_best_free_alternatives_of_adobe_premiere_pro',
        'Post_2': '6_most_popular_javascript_libraries_in_2020',
        'Post_3': '7_skills_you_need_as_a_javascript_developer_in_2020',
        'Post_4': 'top_4_dying_programming_languages_in_2020',
        'Post_5': 'top_5_website_builder_apps_2020_september',
        'Post_6': '10_most_popular_programming_Languages_and_their_uses_2020_october',
        }


# List of Directories - Mudasir Ali

Dates_list = list(Dates.values())
Thumbnails_list = list(Thumbnails.values())
Links_list = list(Links.values())

# Lists for Recent Posts - Mudasir Ali


Recent_Posts_Titles =  Another_Title
Recent_Posts_Thumbnails = Thumbnails_list
Recent_Posts_Links = Links_list
Recent_Posts_Dates = Dates_list


# Reversing the Lists for Recent Posts - Mudasir Ali

Recent_Posts_Titles.reverse()
Recent_Posts_Dates.reverse()
Recent_Posts_Thumbnails.reverse()
Recent_Posts_Links.reverse()



def Blogs(req):
    return render(req, 'Pages/Blogs.html', {'recent_post_1_title': Recent_Posts_Titles[0],
                                            'recent_post_1_thumb': Recent_Posts_Thumbnails[0],
                                            'recent_post_1_date': Recent_Posts_Dates[0],
                                            'recent_post_1_link': Recent_Posts_Links[0],

                                            'recent_post_2_title': Recent_Posts_Titles[1],
                                            'recent_post_2_thumb': Recent_Posts_Thumbnails[1],
                                            'recent_post_2_date': Recent_Posts_Dates[1],
                                            'recent_post_2_link': Recent_Posts_Links[1],

                                            'recent_post_3_title': Recent_Posts_Titles[2],
                                            'recent_post_3_thumb': Recent_Posts_Thumbnails[2],
                                            'recent_post_3_date': Recent_Posts_Dates[2],
                                            'recent_post_3_link': Recent_Posts_Links[2],
                                            
                                            'recent_post_4_title': Recent_Posts_Titles[3],
                                            'recent_post_4_thumb': Recent_Posts_Thumbnails[3],
                                            'recent_post_4_date': Recent_Posts_Dates[3],
                                            'recent_post_4_link': Recent_Posts_Links[3],
        
        
                                            'aboutme': AboutMe,
                                            'post_1_tittle': Tittles[1], 'post_2_tittle': Tittles[2], 'post_3_tittle': Tittles[3], 'post_4_tittle': Tittles[4], 'post_5_tittle': Tittles[5], 'post_6_tittle': Tittles[6],
                                            'post_1_desc': Descriptions.get('Post_1'), 'post_2_desc': Descriptions.get('Post_2'), 'post_3_desc': Descriptions.get('Post_3'), 'post_4_desc': Descriptions.get('Post_4'), 'post_5_desc': Descriptions.get('Post_5'), 'post_6_desc': Descriptions.get('Post_6'),
                                            'post_1_date': Dates.get('Post_1'), 'post_2_date': Dates.get('Post_2'), 'post_3_date': Dates.get('Post_3'), 'post_4_date': Dates.get('Post_4'), 'post_5_date': Dates.get('Post_5'), 'post_6_date': Dates.get('Post_6'),
                                            'post_1_thumb': Thumbnails.get('Post_1'), 'post_2_thumb': Thumbnails.get('Post_2'), 'post_3_thumb': Thumbnails.get('Post_3'), 'post_4_thumb': Thumbnails.get('Post_4'), 'post_5_thumb': Thumbnails.get('Post_5'), 'post_6_thumb': Thumbnails.get('Post_6'),
                                            'post_1_link': Links.get('Post_1'), 'post_2_link': Links.get('Post_2'), 'post_3_link': Links.get('Post_3'), 'post_4_link': Links.get('Post_4'), 'post_5_link': Links.get('Post_5'), 'post_6_link': Links.get('Post_6'), 
                                            })



def Post_1(req):
    Context = {'recent_post_1_title': Recent_Posts_Titles[0],
                'recent_post_1_thumb': Recent_Posts_Thumbnails[0],
                'recent_post_1_date': Recent_Posts_Dates[0],
                'recent_post_1_link': Recent_Posts_Links[0],

                'recent_post_2_title': Recent_Posts_Titles[1],
                'recent_post_2_thumb': Recent_Posts_Thumbnails[1],
                'recent_post_2_date': Recent_Posts_Dates[1],
                'recent_post_2_link': Recent_Posts_Links[1],

                'recent_post_3_title': Recent_Posts_Titles[2],
                'recent_post_3_thumb': Recent_Posts_Thumbnails[2],
                'recent_post_3_date': Recent_Posts_Dates[2],
                'recent_post_3_link': Recent_Posts_Links[2],
                
                'recent_post_4_title': Recent_Posts_Titles[3],
                'recent_post_4_thumb': Recent_Posts_Thumbnails[3],
                'recent_post_4_date': Recent_Posts_Dates[3],
                'recent_post_4_link': Recent_Posts_Links[3],
                
                'aboutme': AboutMe,
                'title': Tittles[1],
                'desc': Descriptions.get('Post_1'),
                'thumb': Thumbnails.get('Post_1'),
                'date': Dates.get('Post_1'),

                'prev_post_title': Tittles[1],
                'prev_post_thumb': Thumbnails.get('Post_1'),
                'prev_post_link': Links.get('Post_1'),

                'next_post_title': Tittles[2],
                'next_post_thumb': Thumbnails.get('Post_2'),
                'next_post_link': Links.get('Post_2')}

    return render(req, 'Blog/7_best_free_alternatives_of_adobe_premiere_pro.html', Context)


def Post_2(req):
    Context = {'recent_post_1_title': Recent_Posts_Titles[0],
                'recent_post_1_thumb': Recent_Posts_Thumbnails[0],
                'recent_post_1_date': Recent_Posts_Dates[0],
                'recent_post_1_link': Recent_Posts_Links[0],

                'recent_post_2_title': Recent_Posts_Titles[1],
                'recent_post_2_thumb': Recent_Posts_Thumbnails[1],
                'recent_post_2_date': Recent_Posts_Dates[1],
                'recent_post_2_link': Recent_Posts_Links[1],

                'recent_post_3_title': Recent_Posts_Titles[2],
                'recent_post_3_thumb': Recent_Posts_Thumbnails[2],
                'recent_post_3_date': Recent_Posts_Dates[2],
                'recent_post_3_link': Recent_Posts_Links[2],
                
                'recent_post_4_title': Recent_Posts_Titles[3],
                'recent_post_4_thumb': Recent_Posts_Thumbnails[3],
                'recent_post_4_date': Recent_Posts_Dates[3],
                'recent_post_4_link': Recent_Posts_Links[3],
                
                'aboutme': AboutMe,
                'title': Tittles[2],
                'desc': Descriptions.get('Post_2'),
                'thumb': Thumbnails.get('Post_2'),
                'date': Dates.get('Post_2'),

                'prev_post_title': Tittles[1],
                'prev_post_thumb': Thumbnails.get('Post_1'),
                'prev_post_link': Links.get('Post_1'),

                'next_post_title': Tittles[3],
                'next_post_thumb': Thumbnails.get('Post_3'),
                'next_post_link': Links.get('Post_3')}

    return render(req, 'Blog/6_most_popular_javascript_libraries_in_2020.html', Context)

def Post_3(req):
    Context = {'recent_post_1_title': Recent_Posts_Titles[0],
                'recent_post_1_thumb': Recent_Posts_Thumbnails[0],
                'recent_post_1_date': Recent_Posts_Dates[0],
                'recent_post_1_link': Recent_Posts_Links[0],

                'recent_post_2_title': Recent_Posts_Titles[1],
                'recent_post_2_thumb': Recent_Posts_Thumbnails[1],
                'recent_post_2_date': Recent_Posts_Dates[1],
                'recent_post_2_link': Recent_Posts_Links[1],

                'recent_post_3_title': Recent_Posts_Titles[2],
                'recent_post_3_thumb': Recent_Posts_Thumbnails[2],
                'recent_post_3_date': Recent_Posts_Dates[2],
                'recent_post_3_link': Recent_Posts_Links[2],
                
                'recent_post_4_title': Recent_Posts_Titles[3],
                'recent_post_4_thumb': Recent_Posts_Thumbnails[3],
                'recent_post_4_date': Recent_Posts_Dates[3],
                'recent_post_4_link': Recent_Posts_Links[3],
                
                'aboutme': AboutMe,
                'title': Tittles[3],
                'desc': Descriptions.get('Post_3'),
                'thumb': Thumbnails.get('Post_3'),
                'date': Dates.get('Post_3'),

                'prev_post_title': Tittles[2],
                'prev_post_thumb': Thumbnails.get('Post_2'),
                'prev_post_link': Links.get('Post_2'),

                'next_post_title': Tittles[4],
                'next_post_thumb': Thumbnails.get('Post_4'),
                'next_post_link': Links.get('Post_4')}

    return render(req, 'Blog/7_skills_you_need_as_a_javascript_developer_in_2020.html', Context)


def Post_4(req):
    Context = {'recent_post_1_title': Recent_Posts_Titles[0],
                'recent_post_1_thumb': Recent_Posts_Thumbnails[0],
                'recent_post_1_date': Recent_Posts_Dates[0],
                'recent_post_1_link': Recent_Posts_Links[0],

                'recent_post_2_title': Recent_Posts_Titles[1],
                'recent_post_2_thumb': Recent_Posts_Thumbnails[1],
                'recent_post_2_date': Recent_Posts_Dates[1],
                'recent_post_2_link': Recent_Posts_Links[1],

                'recent_post_3_title': Recent_Posts_Titles[2],
                'recent_post_3_thumb': Recent_Posts_Thumbnails[2],
                'recent_post_3_date': Recent_Posts_Dates[2],
                'recent_post_3_link': Recent_Posts_Links[2],
                
                'recent_post_4_title': Recent_Posts_Titles[3],
                'recent_post_4_thumb': Recent_Posts_Thumbnails[3],
                'recent_post_4_date': Recent_Posts_Dates[3],
                'recent_post_4_link': Recent_Posts_Links[3],
                
                'aboutme': AboutMe,
                'title': Tittles[4],
                'desc': Descriptions.get('Post_4'),
                'thumb': Thumbnails.get('Post_4'),
                'date': Dates.get('Post_4'),

                'prev_post_title': Tittles[3],
                'prev_post_thumb': Thumbnails.get('Post_3'),
                'prev_post_link': Links.get('Post_3'),

                'next_post_title': Tittles[5],
                'next_post_thumb': Thumbnails.get('Post_5'),
                'next_post_link': Links.get('Post_5')}
    return render(req, 'Blog/top_4_dying_programming_languages_in_2020.html', Context)

def Post_5(req):
    Context = {'recent_post_1_title': Recent_Posts_Titles[0],
                'recent_post_1_thumb': Recent_Posts_Thumbnails[0],
                'recent_post_1_date': Recent_Posts_Dates[0],
                'recent_post_1_link': Recent_Posts_Links[0],

                'recent_post_2_title': Recent_Posts_Titles[1],
                'recent_post_2_thumb': Recent_Posts_Thumbnails[1],
                'recent_post_2_date': Recent_Posts_Dates[1],
                'recent_post_2_link': Recent_Posts_Links[1],

                'recent_post_3_title': Recent_Posts_Titles[2],
                'recent_post_3_thumb': Recent_Posts_Thumbnails[2],
                'recent_post_3_date': Recent_Posts_Dates[2],
                'recent_post_3_link': Recent_Posts_Links[2],
                
                'recent_post_4_title': Recent_Posts_Titles[3],
                'recent_post_4_thumb': Recent_Posts_Thumbnails[3],
                'recent_post_4_date': Recent_Posts_Dates[3],
                'recent_post_4_link': Recent_Posts_Links[3],
                
                'aboutme': AboutMe,
                'title': Tittles[5],
                'desc': Descriptions.get('Post_5'),
                'thumb': Thumbnails.get('Post_5'),
                'date': Dates.get('Post_5'),

                'prev_post_title': Tittles[4],
                'prev_post_thumb': Thumbnails.get('Post_4'),
                'prev_post_link': Links.get('Post_4'),

                'next_post_title': Tittles[6],
                'next_post_thumb': Thumbnails.get('Post_6'),
                'next_post_link': Links.get('Post_6')}
    return render(req, 'Blog/top_5_website_builder_apps_2020_september.html', Context)

def Post_6(req):
    Context = {'recent_post_1_title': Recent_Posts_Titles[0],
                'recent_post_1_thumb': Recent_Posts_Thumbnails[0],
                'recent_post_1_date': Recent_Posts_Dates[0],
                'recent_post_1_link': Recent_Posts_Links[0],

                'recent_post_2_title': Recent_Posts_Titles[1],
                'recent_post_2_thumb': Recent_Posts_Thumbnails[1],
                'recent_post_2_date': Recent_Posts_Dates[1],
                'recent_post_2_link': Recent_Posts_Links[1],

                'recent_post_3_title': Recent_Posts_Titles[2],
                'recent_post_3_thumb': Recent_Posts_Thumbnails[2],
                'recent_post_3_date': Recent_Posts_Dates[2],
                'recent_post_3_link': Recent_Posts_Links[2],
                
                'recent_post_4_title': Recent_Posts_Titles[3],
                'recent_post_4_thumb': Recent_Posts_Thumbnails[3],
                'recent_post_4_date': Recent_Posts_Dates[3],
                'recent_post_4_link': Recent_Posts_Links[3],
                
                'aboutme': AboutMe,
                'title': Tittles[6],
                'desc': Descriptions.get('Post_6'),
                'thumb': Thumbnails.get('Post_6'),
                'date': Dates.get('Post_6'),

                'prev_post_title': Tittles[5],
                'prev_post_thumb': Thumbnails.get('Post_5'),
                'prev_post_link': Links.get('Post_5'),

                'next_post_title': Tittles[6],
                'next_post_thumb': Thumbnails.get('Post_6'),
                'next_post_link': Links.get('Post_6')}
    return render(req, 'Blog/10_most_popular_programming_Languages_and_their_uses_2020_october.html', Context)