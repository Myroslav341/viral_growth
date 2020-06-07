from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from ...models import User
from ...library.constants import *
from ...serializers import UserShortSerializer


class UserListView(LoginRequiredMixin, BaseView):
    template_name = USER_LIST_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        user_list_all = User.objects.exclude(id=request.user.id)

        page_number = kwargs.get(PAGE) or 1

        paginator = Paginator(user_list_all, ViralGrowthAppConfig.pagination_size)

        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            return redirect(reverse(USER_LIST_PAGE, args=(1,)))
        except EmptyPage:
            return redirect(reverse(USER_LIST_PAGE, args=(paginator.num_pages,)))

        pages = []

        pagination_data = {}
        if page.has_previous():
            pagination_data['previous'] = str(page.previous_page_number())
            pages.append(str(page.previous_page_number()))

        pages.append(page_number)

        if page.has_next():
            pagination_data['next'] = str(page.next_page_number())
            pages.append(str(page.next_page_number()))

        pagination_data['pages'] = pages
        pagination_data['current'] = page_number

        return self.render_template(
            request,
            users=UserShortSerializer(page.object_list, many=True).data,
            pagination=pagination_data,
        )
