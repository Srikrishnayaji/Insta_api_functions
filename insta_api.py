import requests

url_1 = 'https://api.instagram.com/v1/users/self/?access_token=Enter_your_access_token'
url_2 = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=Enter_your_access_token'


def get_user_details(url_1):
    r_1 = requests.get(url_1).json()
    username =  r_1['data']['username']
    fullname =  r_1['data']['full_name']
    img_link =  r_1['data']['profile_picture']
    bio      =  r_1['data']['bio']
    following = r_1['data']['counts']['follows']
    followers = r_1['data']['counts']['followed_by']
    user_info = {'username':username, 'fullname':fullname,
                 'img_link':img_link, 'bio':bio,
                 'followers':followers,'following':following}
    return(user_info)

def get_post_details(url_2, post_number):
    r_2 = requests.get(url_2).json()
    no_of_comments = r_2['data'][post_number]['comments']['count']
    no_of_likes = r_2['data'][post_number]['likes']['count']
    post_link = r_2['data'][post_number]['images']['low_resolution']['url']
    caption = r_2['data'][post_number]['caption']['text']
    post_detail = {'post_link':post_link, 'comments_count':no_of_comments, 'likes_count':no_of_likes,
                          'caption':caption}
    return(post_detail)
