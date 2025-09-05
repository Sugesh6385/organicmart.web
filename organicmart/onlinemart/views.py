from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')  # Render the product.html template

def about(request):
    return render(request, 'about.html')  # Render the about.html template

def contact(request):
    return render(request, 'contact.html')  # Render the contact.html template

def buy_now(request):
    return render(request, 'buy_now.html')

def confirm_purchase(request):
    if request.method == 'POST':
        # Handle form submission logic here
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        quantity = int(request.POST.get('quantity'))
        payment_type = request.POST.get('payment_type')
        product_name = "Fresh Organic Product"  # Example product name
        original_price_per_unit = 150  # Example original price per unit
        discounted_price_per_unit = 100  # Example discounted price per unit
        total_price = discounted_price_per_unit * quantity
        savings = (original_price_per_unit - discounted_price_per_unit) * quantity
        # Save or process the data
        return render(request, 'thank_you.html', {
            'name': name,
            'address': address,
            'phone': phone,
            'quantity': quantity,
            'payment_type': payment_type,
            'product_name': product_name,
            'total_price': total_price,
            'savings': savings
        })
    # Render the confirmation form for GET requests
    return render(request, 'confirm_purchase.html')
