# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from flask import views, render_template
from iefschina.blueprints import blueprint_www


from iefschina.models import ChannelModel, ArticleModel


class ArticleView(views.MethodView):
    '''
        文章页
    '''

    def get(self, aid):
        article = ArticleModel.query.get(aid)
        return render_template('www/article.html', article=article)


blueprint_www.add_url_rule('/article/<int:aid>/',
                            view_func=ArticleView.as_view(b'article'),
                            endpoint='article', methods=['GET'])