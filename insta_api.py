import requests


#access_token = 'Enter your access token' #register as an instagram developer and get the access token
#post_index   =  # Enter post_index value; type=int(); 0=latest post and total_posts-1 = first post;
#post_type    =  'Enter_post type' #possible values 'images' or 'videos'


#function to get the user's details from the instagram api
def get_user_details(access_token):
    url = f'https://api.instagram.com/v1/users/self/?access_token={access_token}'
    try:
        r = requests.get(url).json()
        username         = r['data']['username']
        profile_pic_link = r['data']['profile_picture']
        full_name        = r['data']['full_name']
        bio              = r['data']['bio']
        website          = r['data']['website']
        is_business      = r['data']['is_business']
        no_of_posts_made = r['data']['counts']['media']
        no_of_following  = r['data']['counts']['follows']
        no_of_followers  = r['data']['counts']['followed_by']
        collected_data   = {'username':username, 'profile_pic_link':profile_pic_link,
                            'full_name':full_name, 'bio':bio, 'website':website,
                            'is_business': is_business, 'no_of_posts_made': no_of_posts_made,
                            'no_of_following':no_of_following, 'no_of_followers':no_of_followers}
        return(collected_data)
    except:
        return("Cannot print emojis used in one of the data on the console. Try printing the details on a html file")


#function to get the user's post details from the instagram api
def get_post_details(access_token, post_index, post_type='images'):
    url = f'https://api.instagram.com/v1/users/self/?access_token={access_token}'
    try:
        r = requests.get(url).json()
        no_of_comments = r['data'][post_index]['comments']['count']
        caption        = r['data'][post_index]['caption']['text']
        post_link      = r['data'][post_index][post_type]['standard_resolution']['url']
        no_of_likes    = r['data'][post_index]['likes']['count']
        location       = r['data'][post_index]['location']['name']
        tagged_people  = r['data'][post_index]['users_in_photo'] #returns a list
        collected_data = {'no_of_comments':no_of_comments, 'caption':caption,
                        'post_link':post_link, 'no_of_likes':no_of_likes,
                        'location':location, 'tagged_people':tagged_people}
        return(collected_data)
    except:
        return("Cannot print emojis used in one of the data on the console. Try printing the details on a html file")
