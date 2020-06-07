from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, Page
from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from ...models import User
from ...library.constants import *
from ...serializers import UserShortSerializer


class UserListView(LoginRequiredMixin, BaseView):
    """
    user list representation using pagination
    """
    template_name = USER_LIST_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        user_list_all = User.objects.exclude(id=request.user.id)
        page_number = kwargs.get(PAGE) or 1

        paginator = Paginator(user_list_all, ViralGrowthAppConfig.pagination_size)

        return self.__configure_pagination(request, paginator, page_number)

    def __configure_pagination(self, request, paginator: Paginator, page_number: int):
        """
        configure pagination data and users data
        """
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            return redirect(reverse(USER_LIST_PAGE, args=(1,)))
        except EmptyPage:
            return redirect(reverse(USER_LIST_PAGE, args=(paginator.num_pages,)))

        pagination_data = self.__get_pagination_data(page, page_number)

        return self.render_template(
            request,
            users=UserShortSerializer(page.object_list, many=True).data,
            pagination=pagination_data,
        )

    def __get_pagination_data(self, page: Page, page_number: int):
        """
        create and return pagination data for pagination bar in front
        """
        pages = []
        pagination_data = {}

        if page.has_previous():
            pagination_data[PREVIOUS] = str(page.previous_page_number())
            pages.append(str(page.previous_page_number()))

        pages.append(page_number)

        if page.has_next():
            pagination_data[NEXT] = str(page.next_page_number())
            pages.append(str(page.next_page_number()))

        pagination_data[PAGES] = pages
        pagination_data[CURRENT] = page_number

        return pagination_data
