from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, ProductVariant


def cart_contents(request):
    """
    Context processor for cart contents - makes it available across all templates
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        # Check if the item has a variant
        if '_' in item_id:
            product_id, variant_id = item_id.split('_')
            product = get_object_or_404(Product, pk=product_id)
            variant = get_object_or_404(ProductVariant, pk=variant_id)
            
            # Calculate price with the variant adjustment
            item_price = variant.final_price
            subtotal = item_price * quantity
            
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'variant': variant,
                'subtotal': subtotal,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            subtotal = product.price * quantity
            
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'subtotal': subtotal,
            })
        
        total += subtotal
        product_count += quantity

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context