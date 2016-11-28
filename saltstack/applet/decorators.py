# -*- coding: utf-8 -*-
import json, time
from django import http
from const import DisplayConst, FoundationConst
from saltstack.applet import utils, response
from django.conf  import settings

def generate_other_dict_data():
    odd = dict()
    odd[FoundationConst.RN_STATIC_URL] = '{0}'.format("http://hypro-10030008.file.myqcloud.com/")
    if settings.DEBUG:
        odd[FoundationConst.RN_WEIXIN_DEBUG] = '?{0}'.format(int(time.time()))
    return odd

def _render_page(request, template_name, other_dict_data, page_view, *args, **kwargs):
    try:
        rd = page_view(request, *args, **kwargs)
        cookie_list = utils.get_cookie_list_from_request(request)
        if isinstance(rd, dict):
            if other_dict_data is not None:
                rd.update(other_dict_data)
            return response.page_success(template_name, rd, cookie_list)
        elif rd is None:
            return response.page_success(template_name, other_dict_data, cookie_list)
        elif isinstance(rd, http.HttpResponse):
            return rd
        else:
            raise utils.ServerException(DisplayConst.EXCEPTION_SERVER_NOT_STD_BEHAVIOUR)
    except Exception as e:
        client_error_dict = {DisplayConst.ERROR_MESSAGE: str(e)}
        if isinstance(e, utils.ClientException):
            return response.page_400(DisplayConst.PAGE_400, client_error_dict)
        elif isinstance(e, utils.ServerException):
            return response.page_500(DisplayConst.PAGE_500, client_error_dict)
        else:
            return response.page_501(DisplayConst.PAGE_501, client_error_dict)





def _render_action(request, action_view, *args, **kwargs):
    try:
        rd = action_view(request, *args, **kwargs)
        cookie_list = utils.get_cookie_list_from_request(request)
        if isinstance(rd, dict):
            return response.action_success(rd, cookie_list)
        elif rd is None:
            return response.action_success(dict(), cookie_list)
        elif isinstance(rd, http.HttpResponse):
            return rd
        else:
            raise utils.ServerException(DisplayConst.EXCEPTION_SERVER_NOT_STD_BEHAVIOUR)
    except Exception as e:
        client_error_dict = {DisplayConst.ERROR_MESSAGE: str(e)}
        if isinstance(e, utils.ClientException):
            return response.action_400(client_error_dict)
        elif isinstance(e, utils.ServerException):
            return response.action_500(client_error_dict)
        else:
            return response.action_501(client_error_dict)



def page_render(template_name):
    def wrapper(page_view):
        def wrapped(request, *args, **kwargs):
            return _render_page(request, template_name, generate_other_dict_data(), page_view, *args, **kwargs)
        return wrapped
    return wrapper


def action_render(action_view):
    def wrapper(request, *args, **kwargs):
        return _render_action(request, action_view, *args, **kwargs)
    return wrapper

