import time, praw

r = praw.Reddit(user_agent='a bot to alert nick of the keywoard \'minivan\' on /r/mechmarket. '
'Made by /u/beardedcroughton', client_id='Wvyikrl5De3mcQ', client_secret='w4kga_DuOoUu0tFd-TNIeSgYKac',
username='alertbeano77_bot', password='arppar92')

already_done = []
post_lim = 25

def alert_nock(post):
    msg = 'minivan related thread: %s' % post.short_link
    print('alerting nock with message: %s' % msg)
    r.send_message('thebeano77', 'minivan related thread', msg)

while True:
    # try:
        subreddit = r.subreddit('mechmarket')
        for post in subreddit.new(limit=25):
            if post.id not in already_done and ('minivan' in post.title or 'minivan' in post.selftext):
                alert_nock(post)
                already_done.append(post.id)
    # except Exception as err:
    #     print('exception when connecting to reddit: {0}'.format(err))

        post_lim = 10
        time.sleep(60000)