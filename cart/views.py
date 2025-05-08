from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product, ProductVariant

def view_cart(request):
    """A view to render the cart contents page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the shopping cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity', 1))
        redirect_url = request.POST.get('redirect_url')
        variant_id = request.POST.get('variant_id')
        cart = request.session.get('cart', {})
        
        if variant_id:
            variant = get_object_or_404(ProductVariant, pk=variant_id)
            item_id_str = f"{item_id}_{variant_id}"
            
            if item_id_str in cart:
                cart[item_id_str] += quantity
                messages.success(request, f'Updated {variant.name} {product.name} quantity to {cart[item_id_str]}')
            else:
                cart[item_id_str] = quantity
                messages.success(request, f'Added {variant.name} {product.name} to your cart')
        else:
            if str(item_id) in cart:
                cart[str(item_id)] += quantity
                messages.success(request, f'Updated {product.name} quantity to {cart[str(item_id)]}')
            else:
                cart[str(item_id)] = quantity
                messages.success(request, f'Added {product.name} to your cart')
        
        request.session['cart'] = cart
        return redirect(redirect_url)
    except Exception as e:
        messages.error(request, f"Error adding item to cart: {e}")
        return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    try:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        
        # Check if item_id exists in cart
        if item_id in cart:
            if quantity > 0:
                cart[item_id] = quantity
                # Display success message indicating the item was updated
                if '_' in item_id:
                    # It's a product variant
                    product_id, variant_id = item_id.split('_')
                    product = get_object_or_404(Product, pk=product_id)
                    variant = get_object_or_404(ProductVariant, pk=variant_id)
                    messages.success(request, f'Updated {variant.name} {product.name} quantity to {quantity}')
                else:
                    # It's a regular product
                    product = get_object_or_404(Product, pk=item_id)
                    messages.success(request, f'Updated {product.name} quantity to {quantity}')
            else:
                cart.pop(item_id)
                # Display success message indicating the item was removed
                if '_' in item_id:
                    # It's a product variant
                    product_id, variant_id = item_id.split('_')
                    product = get_object_or_404(Product, pk=product_id)
                    variant = get_object_or_404(ProductVariant, pk=variant_id)
                    messages.success(request, f'Removed {variant.name} {product.name} from your cart')
                else:
                    # It's a regular product
                    product = get_object_or_404(Product, pk=item_id)
                    messages.success(request, f'Removed {product.name} from your cart')
        
        request.session['cart'] = cart
        return redirect(reverse('cart:view_cart'))
    except Exception as e:
        messages.error(request, f"Error updating cart: {e}")
        return redirect(reverse('cart:view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        cart = request.session.get('cart', {})
        
        if item_id in cart:
            cart.pop(item_id)
            request.session['cart'] = cart
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    except Exception as e:
        return HttpResponse(content=str(e), status=500)


def clear_cart(request):
    """Clear all items from the shopping cart"""
    try:
        # Reset the cart to an empty dictionary
        request.session['cart'] = {}
        messages.success(request, 'Your cart has been cleared')
        return redirect(reverse('cart:view_cart'))
    except Exception as e:
        messages.error(request, f"Error clearing cart: {e}")
        return redirect(reverse('cart:view_cart'))
