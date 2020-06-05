from django.shortcuts import render
from django.views.generic import TemplateView


class BaseView(TemplateView):
    def render_template(self, request, **kwargs):
        return render(request, self.template_name, kwargs)
