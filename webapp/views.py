from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from webapp.models import Post
from webapp.models import Schedule
from webapp.mixins import MonthCalendarMixin, WeekCalendarMixin,WeekWithScheduleMixin
from .forms import PostCreateForm
from .forms import BS4ScheduleForm
import datetime
# Create your views here.

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('webapp:post_list')

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = reverse_lazy('webapp:post_detail')

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('webapp:post_list')

class Calendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    '''月間、週間カレンダー、スケージュール登録画面'''
    template_name = 'templates/calendar.html'
    model = Schedule
    data_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
    
    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return redirect('webapp:calendar', year=date.year, month=date.month, day=date.day)

class MonthCalendar(MonthCalendarMixin):
    template_name = 'templates/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class WeekCalendar(WeekCalendarMixin):
    template_name ='templates/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calender_context = self.get_week_calendar()
        context.update(calender_context)
        return context

class WeekWithScheduleCalendar(WeekWithScheduleMixin, generic.TemplateView):
    template_name ='templates/week_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_context_data(**kwargs)
        context.update(calendar_context)
        context['week_row'] = zip(
            calendar_context['week_names'],
            calendar_context['week_days'],
            calendar_context['week_day_schedules'].values
        )
        return context