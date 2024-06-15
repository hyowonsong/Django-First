from django.views.generic.base import TemplateView
from django.apps import apps

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_dict = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                verbose_dict[app.label] = app.verbose_name
                # 예시로 'polls' 앱에 대해 URL 패턴을 추가할 수 있습니다.
                if app.label == 'polls':
                    verbose_dict[app.label] = {
                        'verbose_name': app.verbose_name,
                        'url_name': 'polls:index'  # 이 부분을 해당 앱의 실제 URL 패턴 또는 뷰 이름으로 수정
                    }
        context['verbose_dict'] = verbose_dict
        return context
