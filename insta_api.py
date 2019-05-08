import requests

access_token = #Enter your access token

post_number  = #Enter post number whose details you want to see
# NOTE: 0 = latest_post ; total_no_of_posts-1 = first post

post_type = #Enter the typre of the post
#valuess possibe are 1)images 2)videos

url_for_user_details = f'https://api.instagram.com/v1/users/self/?access_token={access_token}'
url_for_post_details = f'https://api.instagram.com/v1/users/self/media/recent/?access_token={access_token}'


def get_user_details(url_for_user_details):
    r = requests.get(url_for_user_details).json()  #r = json data obtained from the api 
    username =  r['data']['username']
    fullname =  r['data']['full_name']
    img_link =  r['data']['profile_picture']
    bio      =  r['data']['bio']
    following = r['data']['counts']['follows']
    followers = r['data']['counts']['followed_by']
    user_info = {'username':username, 'fullname':fullname,
                 'img_link':img_link, 'bio':bio,
                 'followers':followers,'following':following}
    return(user_info)

def get_post_details(url_for_post_details, post_number, post_type):
    r = requests.get(url_for_post_details).json()        #r = json data obtained from the api
    no_of_comments = r['data'][post_number]['comments']['count']
    no_of_likes = r['data'][post_number]['likes']['count']
    post_link = r['data'][post_number][post_type]['standard_resolution']['url']
    caption = r['data'][post_number]['caption']['text']
    post_details = {'post_link':post_link, 'comments_count':no_of_comments, 'likes_count':no_of_likes,
                          'caption':caption}
    return(post_details)
