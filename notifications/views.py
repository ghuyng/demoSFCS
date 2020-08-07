from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .models import Notification
# Create your views here.

def get_notifications(request):
    recent_notis = request.user.notification_set.all()
    if len(recent_notis) > 5:
        recent_notis = recent_notis[:5]

    result = recent_notis.filter(status=Notification.UNREAD).count()

    return JsonResponse({
        'result' : result,
        'notifications_list': render_to_string('notifications.html', {'noti_list': recent_notis}),
    })


def mark_notifications(request):
    request.user.notification_set.filter(status=Notification.UNREAD).update(status=Notification.READ)
    return JsonResponse({
        'success' : True,
    })