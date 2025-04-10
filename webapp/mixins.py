import calendar
from collections import deque

class BaseCalendarMixin:
    '''カレンダー関連Mixinの基底クラス'''
    first_weekday = 0
    week_names =['月', '火', '水', '木', '金', '土', '日']

    def setup_calendar(self):
        '''
        内部カレンダーの設定処理
        calendar.Calendarクラスの機能を利用するためインスタンス化する
        火曜日から表示したい時 fist_weekday=1の時のセットアップ
        '''
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        '''first_weekday似合わせてweek_namesをシフトする'''
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names