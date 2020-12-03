from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time
from selenium import webdriver


#your login credentials
insta_username='your_username'
insta_password='your_password'

#path to your workspace
set_workspace(path=None)

def job():
      
 
  session = InstaPy(username=insta_username, password=insta_password)

  with smart_run(session):
    """                                                I Basic sort of people accounts: 
    """
    """ 
    1. Sort by following count:
    potency_ratio with POSITIVE values can be used to route interactions to only potential (real) 
    users WHOSE followers count is higher than following count (e.g., potency_ratio = 1.39)
    find desired potency_ratio with this formula: potency_ratio == followers count / following count (use desired counts)
    """
    session.set_relationship_bounds(enabled=True,
                                  potency_ratio=1.4,
                                  delimit_by_numbers=True,
                                  max_followers=1200,
                                  max_following=1000,
                                  min_followers=30,
                                  min_following=35,
                                  min_posts=20,
                                max_posts=600)


    """ 
    2. Profile photo sort:

    """ 
    
    session.set_skip_users(skip_private=True,
                       skip_no_profile_pic=True,
                       skip_business=True,
		                   skip_non_business=False,
                       business_percentage=100,
                       no_profile_pic_percentage=100
                      )
    """
    3. Skipping by bio keywords in profile

    """
    session.set_skip_users(skip_bio_keyword = ['shop', 'cars', 'manager'])
 
    """ 
    4. Language sort

    """
    session.set_mandatory_language(enabled=True, character_set=['CYRILLIC'])

    """
                                                          II Bot restrictions
               Instagram is always bans accounts who do not follow the rules for signing up, likes, coments daily and hourly
                                              This restrictions could help not to be baned


    1) enabled: put True to activate or False to deactivate supervising any time
    2) sleep_after: is used to put InstaPy to sleep after reaching peak rather than jumping the action (or exiting- for server calls)
        Any action can be included ["likes", "comments", "follows", "unfollows", "server_calls"].
        As if you want to put sleep only after reaching hourly like peak, put "likes_h" OR put "likes_d" 
        for sleeping only after reaching daily like peak."""

      
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=40,
                              peak_likes_daily=200,
                               peak_comments_hourly=20,
                               peak_comments_daily=50,
                                peak_follows_hourly=50,
                                peak_follows_daily=150,
                                 peak_unfollows_hourly=5,
                                 peak_unfollows_daily=25,
                                  peak_server_calls_hourly=300,
                                  peak_server_calls_daily=3700)

    """
                                                              III Bot tasks: 
    
    1) Follows :

      Follow by location (https://www.instagram.com/explore/locations/)"""
      
    # session.follow_by_locations(['1234567/somecity/'], amount=5, skip_top_posts=True)
    """" Follow by a list

    Here you could use another programm called grab_folowers.py from my repository and still someones followers or following
    After you get a list of users from json file, place them all in User_slice.py and choose how many people you want to get
    Place them to the accs ->
    """

    # accs = ["someone_1", "someone_2", "someone_3"] 
    # session.follow_by_list(accs, times=1, sleep_delay=600, interact=False)

    """
    2) Commenting:"""
    # session.comment_by_locations(['213174824/saint-petersburg-russia/','17695300/nevsky-prospect-st-petersburg/'], amount=5, skip_top_posts= True)

    """ 
        1)To use emoji in comments, you should put - u. ([u'HashTag']) like this
        2)All emoji here -> : (https://www.webfx.com/tools/emoji-cheat-sheet/)"""

    # session.set_comments([open("comments.txt", "r")])

    """
    3) Likes :
    
    Easy likes by tag:
      /Generate smart hashtags based on https://displaypurposes.com/map ranking. Banned and spammy tags are filtered out.
      # radius: Radius around the location in Miles
      # limit: Defines amount limit of generated hashtags by hashtag"""

    # session.set_smart_location_hashtags(['213174824/saint-petersburg-russia/, 617091319, 17695300/nevsky-prospect-st-petersburg/'], radius=10, limit=10)
    # session.like_by_tags(amount=1, use_smart_location_hashtags=True)

    """Like by lokation same as comment follow by location:   """

    session.like_by_locations(['1234567/somecity/'], amount=1, skip_top_posts= True)
    
    """
    4) Unfollow: 
    
    # Prevents unfollow followers who have liked one of your latest 5 posts"""
    session.set_dont_unfollow_active_users(enabled=True, posts=5)
    session.unfollow_users(amount=2, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
    


    """
    Scheduel is a usefull feater to run bot without your assistance several times a day
    """

# schedule.every().day.at("09:30").do(job)
schedule.every().day.at("16:09").do(job)
# schedule.every().day.at('22:30').do(job_that_executes_once)


while True:
  schedule.run_pending()
  time.sleep(10)