from django.urls import path
from . import views
app_name ='webapp'

urlpatterns = [
    path('post_list', views.PostListView.as_view(), name='post_list'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', view=views.PostDetailView.as_view(), name='post_detail'),
    path('post_update/<int:pk>', view=views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', view=views.PostDeleteView.as_view(), name="post_delete"),
    path('calendar/',view=views.Calendar.as_view(), name='calendar'),
    path('calendar/<int:year>/<int:month>/<int:day>/', view=views.Calendar.as_view(), name='calendar'),
    path('', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>', view=views.MonthCalendar.as_view(), name='month'),
    path('week/', view=views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', view=views.WeekCalendar.as_view(),  name='week'),
    path('week_with_schedule/', view=views.WeekWithScheduleCalendar.as_view(), name="week_with_schedule"),
    path(
        'week_with_schedule/<int:year>/<int:month>/<int:day>/',
        view=views.WeekWithScheduleCalendar.as_view(),
        name='week_with_schedule'
    )
]