# -*- coding: utf-8 -*-
import os, uuid
from django.http import HttpResponse
from const import FoundationConst


def read_file(filename, buf_size=262144):
    f = open(filename, 'rb')
    while True:
        c = f.read(buf_size)
        if c:
            yield c
        else:
            break
    f.close()


def file_for_download(full_filename, show_name):
    response = HttpResponse(read_file(full_filename), content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(show_name)
    response['Content-Length'] = os.path.getsize(full_filename)
    return response


# 为上传图片指定路径
def handle_image_upload(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper


class ClientException(Exception):
    def __init__(self, msg, detail_msg=None):
        self.msg = msg
        self.detail_msg = detail_msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg if self.detail_msg is None else self.detail_msg


class ServerException(Exception):
    def __init__(self, msg, detail_msg=None):
        self.msg = msg
        self.detail_msg = detail_msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg if self.detail_msg is None else self.detail_msg


def get_ip_from_request(request):
    if request.META.has_key(FoundationConst.DJANGO_HTTP_X_FORWARDED_FOR):
        return request.META[FoundationConst.DJANGO_HTTP_X_FORWARDED_FOR]
    else:
        return request.META[FoundationConst.DJANGO_REMOTE_ADDR]


def put_cookie_to_request(request, cookie_dict):
    if not hasattr(request, FoundationConst.RN_REQUEST_CUSTOM):
        request.CUSTOM = dict()
        request.CUSTOM[FoundationConst.RN_COOKIE_LIST] = [cookie_dict, ]
    else:
        request.CUSTOM[FoundationConst.RN_COOKIE_LIST].append(cookie_dict)


def get_cookie_list_from_request(request):
    cookie_list = None
    if hasattr(request, FoundationConst.RN_REQUEST_CUSTOM):
        cookie_list = request.CUSTOM.get(FoundationConst.RN_COOKIE_LIST, None)
    return cookie_list


def put_dict_data_to_request(request, key, value):
    if not hasattr(request, FoundationConst.RN_REQUEST_CUSTOM):
        request.CUSTOM = dict()
    request.CUSTOM[key] = value


def generate_uuid():
    return uuid.uuid4().hex
