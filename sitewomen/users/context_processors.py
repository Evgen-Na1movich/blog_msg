from women.utils import menu


def get_women_context(request):
    return {'mainmenu': menu}


def default_data(request):
    return {
        'default_avatar': 'profile/default_avatar.jpg',
        'default_auth': 'username/password'
    }
