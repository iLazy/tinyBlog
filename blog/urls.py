from django.conf.urls.defaults import *
from models import Entry, Link, Category
from tagging.models import Tag

entry_info_dict ={
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

link_info_dict ={
    'queryset': Link.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
                       (r'^$', 'archive_index', entry_info_dict, 'blog_entry_archive_index'),
                       (r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'blog_entry_archive_year'),
                       (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_info_dict, 'blog_entry_archive_month'),
                       (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict, 'blog_entry_archive_day'),
                       (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'blog_entry_detail'),

                       (r'^links/$', 'archive_index', link_info_dict, 'blog_link_archive_index'),
                       (r'^links/(?P<year>\d{4})/$', 'archive_year', link_info_dict, 'blog_link_archive_year'),
                       (r'^links/(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', link_info_dict, 'blog_link_archive_month'),
                       (r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', link_info_dict, 'blog_link_archive_day'),
                       (r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2#})/(?P<slug>[-\w]+)/$', 'object_detail', link_info_dict, 'blog_link_detail'),
)

#urlpatterns +=patterns{'blog.views',
#                        (r'^categories/$', 'category_list'),
#                        (r'^categories/(?P<slug>[-\w]+)/$', 'category_detail'),
#}




urlpatterns += patterns('',
                        (r'^tags/$',
                         'django.views.generic.list_detail.object_list',
                         {'queryset': Tag.objects.all()}),
                        
                        (r'^tags/entries/(?P<tag>[-\w]+)/$',
                         'tagging.views.tagged_object_list',
                         {'queryset_or_model': Entry,
                          'template_name': 'blog/entries_by_tag.html'}),

                        (r'^tags/entries/(?P<tag>[-\w]+)/$',
                         'tagging.views.tagged_object_list',
                         {'queryset_or_model': Link,
                          'template_name': 'blog/links_by_tag.html'}),

                       )
