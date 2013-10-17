#/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
# В python path добавляется директория проекта
dn = os.path.dirname
PROJECT_ROOT = os.path.abspath( dn(dn(__file__)) )
sys.path.append (PROJECT_ROOT )
DJANGO_PROJECT_ROOT = os.path.join(PROJECT_ROOT, 'erp')
sys.path.append( DJANGO_PROJECT_ROOT )

# Установка файла настроек
os.environ['DJANGO_SETTINGS_MODULE'] = 'erp.settings'

# Запуск wsgi-обработчика
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()