from django.shortcuts import render
from .forms import ProductForm

def upload_product(request):
    result = None
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            l, w, h = product.box_dimensions()
            cost = product.cost_estimation()
            result = {
                'name': product.name,
                'image': product.image.url,   # ✅ ensures template can show uploaded image
                'box': (l, w, h),
                'cost': cost
            }
    else:
        form = ProductForm()
    return render(request, 'results.html', {'form': form, 'result': result})
