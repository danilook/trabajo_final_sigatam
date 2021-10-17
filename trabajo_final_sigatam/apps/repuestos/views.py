from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import CompraForm , AltaRepuestoForm

def altaCompra (request):
     if request.method == 'POST':
         compra_form = CompraForm(request.POST)
         if compra_form.is_valid():
             compra_form.save()
             return redirect ('index')
     else:
        compra_form= CompraForm()

     return render (request, 'repuestos/alta_compra.html',{'compra_form': compra_form})

# class altaCompraView(TemplateView):
#     template_name ='repuestos/alta_compra.html'
#
#     @method_decorator(csrf_exempt)
#
#     def dispach(self,request,*args,**kwargs):
#         return super().dispach(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         data= {}
#         try:
#             action = request.POST ['action']
#             if action == 'searchdata':
#                 pass
#             else:
#                 data ['error'] = 'ha ocurrido un error'
#         except Exception as e:
#             data ['error'] = str(e)
#         return JsonResponse(data, safe= false)
#
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'select anidados'
#         context['form'] = 'CompraForm'
#         return context

def altaRepuesto (request):
    if request.method == 'POST':
        alta_form = AltaRepuestoForm(request.POST)
        if alta_form.is_valid():
            alta_form.save()
            return redirect ('Repuestos:registrar_compra')
    else:
        alta_form= AltaRepuestoForm()
    return render (request,'repuestos/modalrepuestos.html',{'alta_form':alta_form})
