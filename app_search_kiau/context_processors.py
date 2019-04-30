from django.conf import settings

def get_active_value(request):
    # for active1
    home=''
    login=''
    signup=''
    about=''
    posts=''
    poll=''
    rezerve=''
    profile=''
    if request.resolver_match.url_name == "Search Kiau":
        home='active1'
    if request.resolver_match.url_name == "login":
        login='active1'
    if request.resolver_match.url_name == "signup":
        signup='active1'
    if request.resolver_match.url_name == "about":
        about='active1'
    if request.resolver_match.url_name == "posts":
        posts='active1'
    if request.resolver_match.url_name == "poll":
        poll='active1'
    if request.resolver_match.url_name == "rezerve":
        rezerve='active1'
    if request.resolver_match.url_name == "profile":
        profile='active1'
    # for active2
    home2=''
    login2=''
    signup2=''
    about2=''
    posts2=''
    poll2=''
    rezerve2=''
    profile2=''
    if request.resolver_match.url_name == "Search Kiau":
        home2='active2'
    if request.resolver_match.url_name == "login":
        login2='active2'
    if request.resolver_match.url_name == "signup":
        signup2='active2'
    if request.resolver_match.url_name == "about":
        about2='active2'
    if request.resolver_match.url_name == "posts":
        posts2='active2'
    if request.resolver_match.url_name == "poll":
        poll2='active2'
    if request.resolver_match.url_name == "rezerve":
        rezerve2='active2'
    if request.resolver_match.url_name == "profile":
        profile2='active2'
    return{
    # for active1
    "home":home,
    "login":login,
    "signup":signup,
    "about":about,
    "posts":posts,
    "poll":poll,
    "rezerve":rezerve,
    "profile":profile,
    # for active2
    "home2":home2,
    "login2":login2,
    "signup2":signup2,
    "about2":about2,
    "posts2":posts2,
    "poll2":poll2,
    "rezerve2":rezerve2,
    "profile2":profile2
    }
