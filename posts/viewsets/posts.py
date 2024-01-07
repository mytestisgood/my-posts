import json
import os
from datetime import datetime
from operator import itemgetter

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from myposts import settings


class PostsViewSet(viewsets.ViewSet):
    JSON_FILE_PATH = os.path.join(settings.BASE_DIR, 'assets/posts.json')
    ITEMS_PER_PAGE = 15

    def list(self, request):
        page = request.query_params.get('page', 1)
        page = int(page)

        with open(self.JSON_FILE_PATH, 'r') as json_file:
            all_posts = json.load(json_file)

        all_posts = sorted(all_posts, key=itemgetter('created_at'), reverse=True)
        # Calculate the start and end index for the current page
        start_index = (page - 1) * self.ITEMS_PER_PAGE
        end_index = page * self.ITEMS_PER_PAGE

        # Get the posts for the current page
        posts_for_page = all_posts[start_index:end_index]
        formatted_posts = [{'userName': post['user_name'], 'userEmail': post['email'], 'content': post['content'],
                            'date': datetime.fromisoformat(post['created_at']).strftime('%m/%d/%Y %H:%M'), 'tags': post['tags']} for post in
                           posts_for_page]

        return JsonResponse({'posts': formatted_posts}, safe=False)
