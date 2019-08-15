1. User registration.
1. User login. (facebook, google, new).
1. User detail (profile).

# User loged
1. **Create a match.**
1. **Share a match.** (friend list, dashboard, wa, face).
1. **Join a match.**
1. List all matches in dashboard.
1. Social.
  1. Add friend.
  1. Show friend list.
  1. search for friend.
1. List all user matches (my games).
1. quit match. (reduce reputation).


# API Features:
1. Listing all the match stored in the system.
1. Filtering of listed items based on query parameters like `name`, `sport`, `ordering`.
1. Detailed view of a particular match using its: `id`http://127.0.0.1:8000/api/match/994839351740
1. Uses nested serializers for detailed view of children elements.
1. Retrieve football matches ordered by start_time Ex: http://127.0.0.1:8000/api/match/?sport=football&ordering=startTime


User = (username, password, firstname, lastname) 
Player = (fullname, birthday,)
Match/Game = ()
Court/Stadium = ()


Player (10)-----< play >------(1,n) Match/Game
 - un usuario puede participar en varios juegos
 - en un juego participan 10 jugadores


