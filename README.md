# Insta_api_functions

Code written: Python; 
Library Used: requests; 
API used    : Instagram API; 

Details about the file insta_api.py.
      The file consists of 2 functions that can be created based on the previlages given by insta api in client mode:
# 1) function get_user_details(*args):
      This function gets the user details like:
      i) Username
     ii) Actual Name
    iii) Number of Followers the user has
     iv) Number of people the user is following
      v) User's bio
     vi) User's profile picture link
     All the above mentioned details is returned as dictionary.
     
# 2)function get_post_details(*args):
      This function gets the user's post details like :
      i) Post(image) link
     ii) Caption given by the user to the post
    iii) Number of comments for that post
     iv) Number of likes for that post
     All the above mentioned details is returned as dictionary.
     /*The above function has to be specified with the post_number argument, where 0 = latestpost and total_posts-1 = firstpost*/
     
     The above functions can be used to get an insta user's and his/her posts' details on the condition that "The app created by the user 
     gets approved by instagram and he gets the permission to change from client_mode to live_mode". Also by getting the live mode              permission one gets access to more features of the api.
     
   # Useful links:
     1) https://www.instagram.com/developer/ - to register and get access to insta api
     2) https://www.instagram.com/developer/authentication/ - helps you to get the access_token
     
     
      
     
