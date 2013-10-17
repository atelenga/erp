# encoding: utf-8
# Импортируем модули для добавления наших моделей в административный
# интерфейс сайта
from django.contrib import admin
# Импортируем сами модели из файла models.py
from frontend.models import CodeBOM, Remains, Supplier, SupplierProduct, Order, ProcurementPlan, Complectation, ProductionPlan, Plan

# Регистрируем модели в административном интерфейсе
admin.site.register(CodeBOM)
admin.site.register(Remains)
admin.site.register(Supplier)
admin.site.register(SupplierProduct)
admin.site.register(Order)
admin.site.register(ProcurementPlan)
admin.site.register(Complectation)
admin.site.register(ProductionPlan)
admin.site.register(Plan)
