from django.shortcuts import render
import redis
import time
import os
# Create your views here.

def return_count(cache):
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

host = os.environ.get('REDIS_HOST', 'localhost')
def get_hit_count(request):
    cache = redis.Redis(host=host, port = 6379)
    count = return_count(cache)
    context = {'count': count}
    return render(request, 'counter/home.html', context)