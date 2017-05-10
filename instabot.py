

import requests  #imported requests library

app_access_token="4574696093.b304389.186119a6bb1d46eea9b636becfc092b3 "   #acess token from insta
base_url = "https://api.instagram.com/v1/"                               #common url part


#_______________________________________________________________________________________________________________________


#to show my own info
def info():
    request_url=base_url + "users/self/?access_token=" + app_access_token
   # print "requesting url for data=" + request_url
    my_info=requests.get(request_url).json()
    print ("my_info is : \n\r")

    print("Bio:" , my_info["data"]["bio"])
    print ("Username:" , my_info["data"]["username"])
    print ("Fullname:" , my_info["data"]["full_name"])
    print ("Website:" , my_info["data"]["website"])
    print ("Following:" , my_info["data"]["counts"]["follows"])
    print ("Followers:" , my_info["data"]["counts"]["followed_by"])

#_______________________________________________________________________________________________________________________


#to show info of username input by user
def get_user_by_username(insta_username):
    r_url = (base_url + "users/search?q=%s&access_token=%s") %(insta_username,app_access_token)
    #print "requesting url for data=" + r_url
    search_results = requests.get(r_url).json()

    #print search_results

    if search_results['meta']['code']==200:  # checking status code
        if len(search_results['data']):
            print ("Full Name:" , search_results["data"][0]["full_name"])
            print ("Username:" , search_results["data"][0]["username"])
            print ("Id:" , search_results["data"][0]["id"])
            return search_results["data"][0]["id"]
        else:
            print ("User doesn't exist")
            return None
    else:
        print ("request can't be completed")

    return None
    #print search_results

#get_user_by_username("abhi3454")

#_______________________________________________________________________________________________________________________


#to get userid only
def get_user_id_by_username(insta_username):
    r_url = (base_url + "users/search?q=%s&access_token=%s") %(insta_username,app_access_token)
    #print "requesting url for data=" + r_url
    search_results = requests.get(r_url).json()

    #print search_results

    if search_results['meta']['code']==200:
        if len(search_results['data']):
           # print "Full Name:" , search_results["data"][0]["full_name"]
            #print "Username:" , search_results["data"][0]["username"]
            #print "Id:" , search_results["data"][0]["id"]
            return search_results["data"][0]["id"]
        else:
            print ("User doesn't exist")
            return None
    else:
        print ("request can't be completed")

    return None


#_______________________________________________________________________________________________________________________


#to get recent posts
def get_users_recent_posts(insta_username):
    insta_user_id=get_user_id_by_username(insta_username)
    requests_url = (base_url + "users/%s/media/recent/?access_token=%s") % (insta_user_id , app_access_token)
   # print "requesting url for data=" + r_url
    recent_posts = requests.get(requests_url).json()

  #  print recent_posts

    if recent_posts["meta"]["code"] ==200:      #checking status code
        if len(recent_posts["data"]):
         #   return recent_posts["data"][0]["id"]
            for recent in recent_posts["data"]:

                print (recent["images"]["standard_resolution"]["url"] , " has likes =" ,  recent["likes"]["count"])

            return recent_posts["data"][0]["id"]   #returning post_id of latest post
            #print "pp"
        else:
            print ("No recents posts by this user")
    else:
        print ("status code other than 200")


#get_users_recent_posts("abhi3454")

#_______________________________________________________________________________________________________________________


#to like a post
def like_post(insta_username):
    post_id=get_users_recent_posts(insta_username)
    print(post_id)
    payload = {'access token':app_access_token}
    request_url = ( base_url + "media/%s/likes" ) % (post_id)
   # print "requesting url for data=" + request_url
    response_to_like = requests.post( request_url , payload ).json()
    #print response_to_like #["meta"]["code"]

    if response_to_like["meta"]["code"] == 200:
        print ("You ve' successfully liked that post !")

    else:
        print ("Failed to like this Post !")



#_______________________________________________________________________________________________________________________



#to get comment id only
def get_comment_id_for_a_post(insta_username):
    media_id = get_users_recent_posts(insta_username)
    request_url = (base_url  + "media/%s/comments?access_token=%s") %(media_id , app_access_token)
    print (("requesting comments from instagram using %s") % (request_url))
    comments = requests.get(request_url).json()
#    print comments
    for comment in comments["data"]:
       # print ("%s commented: %s") % ( comment["from"]["username"] , comment["text"])
        #print "comment id: " , comment["id"]
        return comment["id"]
#_______________________________________________________________________________________________________________________


#to post a new comment
def post_a_new_comment(insta_username):
    my_comment = input("enter the comment")
    media_id = get_users_recent_posts(insta_username)
    request_url = (base_url + "media/%s/comments") % (media_id )
    request_data = {"access_token":app_access_token , "text":my_comment}
    comment_request = requests.post( request_url , request_data).json()
   # print comment_request
    if comment_request["meta"]["code"]==200:      #checking statuscode
        print ("Successfully commented")
    else:
        print ("Error occured")

#_______________________________________________________________________________________________________________________


#to search comment with particular words
def search_comments(insta_usename):
    word = input("Enter word you want to search:")
    media_id = get_users_recent_posts(insta_username)
    requests_url = (base_url + 'media/%s/comments?access_token=%s' % (media_id, app_access_token))
    result = requests.get(requests_url).json()
   # print "result", result
    result2 = result['data']
    #print "result2", result2
    comment_list = []



    for i in range(len(result2)):
        split = result2[i]['text'].split()
        if word in split:
            comment_list.append(result2[i]['id'])
    print (("comment id of comments with %s:") %(word) , comment_list)
    return comment_list

#_______________________________________________________________________________________________________________________



#to delete comment with particular words
def delete_comments(insta_usename):
    comment_list=search_comments(insta_username)
    media_id = get_users_recent_posts(insta_username)
    if len(comment_list):
        for i in comment_list:
            requests_url2 = (base_url + 'media/%s/comments/%s?access_token=%s' % (media_id, i, app_access_token))
            response = requests.delete(requests_url2).json()
        print  (" Comment successfully deleted !")

    else:
        print ("No comments found ")
        print ("Comment not deleted !")

#delete_comments
#_______________________________________________________________________________________________________________________

#to find average no. of words in comments
def average_number_of_words(user_id ):
    media_id = get_users_recent_posts(insta_username)
    r_url = base_url + 'media/%s/comments?access_token=%s' % (media_id, app_access_token)
    fetch = requests.get(r_url).json()
    count = 1
    average = 0
    if len(fetch['data']) > 0:

        for comments in fetch['data']:
            if len(comments['text']):
                print ("comment id : " + str(count) + " " + "text : " + str(comments['text']))
                splitted_comment = comments['text'].split()    #splitting comment
                count2 = 0
                for i in splitted_comment:
                    count2 += 1
                average = average + count2

            count += 1    #increment of 1
        total_words = average
        total_comments = count - 1
        Average = total_words / total_comments
        print ("Average number of words per comment is : " + str( Average))

    else:
        print ("No comments found !")




#average_number_of_words("abhi3454")
# Calling a function .

#_______________________________________________________________________________________________________________________



#taking username as input
insta_username=input("please enter the username")
print ("\n")
print("-*-*-*-*-*-*-*-*-*-*-\n")

#menu
print ("a.Get own details\n")
print ("b.Get the details of userid you entered above\n")
print ("c.Get recent posts of userid you entered above\n")
print ("d.To like post of userid you entered above\n")
print ("e.To comment on post of userid you entered above\n")
print ("f.To search for comments with a particular word\n")
print ("g.To delete comment with a particular word\n")
print ("h.To calculate average no. of words in comments\n")
print ("i.To exit\n")


choice=input("Enter the choice from above options")
print (choice)
if choice=="a":
    info()
elif choice=="b":
    get_user_by_username(insta_username)
elif choice=="c":
    get_users_recent_posts(insta_username)
elif choice=="d":
    like_post(insta_username)
elif choice=="e":
    post_a_new_comment(insta_username)
elif choice=="f":
    search_comments(insta_username)
elif choice=="g":
    delete_comments(insta_username)
elif choice=="h":
    average_number_of_words(insta_username)
elif choice=="i":
    exit()
else:
    print ("wrong choice")



