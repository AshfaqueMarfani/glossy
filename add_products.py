import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glossy.settings')
django.setup()

from products.models import Category, Product, ProductVariant
from django.core.files.images import ImageFile

def add_categories():
    """Add categories for Glossy cosmetics products"""
    categories = [
        {
            'name': 'face',
            'friendly_name': 'Face Makeup'
        },
        {
            'name': 'lips',
            'friendly_name': 'Lip Products'
        },
        {
            'name': 'eyes',
            'friendly_name': 'Eye Makeup'
        },
        {
            'name': 'cheeks',
            'friendly_name': 'Cheek Products'
        },
        {
            'name': 'skincare',
            'friendly_name': 'Skincare'
        },
        {
            'name': 'brushes',
            'friendly_name': 'Brushes & Tools'
        },
    ]
    
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={'friendly_name': category_data['friendly_name']}
        )
        if created:
            print(f"Created category: {category.friendly_name}")
        else:
            print(f"Category already exists: {category.friendly_name}")
    
    return {cat['name']: Category.objects.get(name=cat['name']) for cat in categories}

def add_products(categories):
    """Add sample products for Glossy cosmetics"""
    products = [
        {
            'category': categories['face'],
            'name': 'Luminous Foundation',
            'description': 'A lightweight, buildable foundation that provides medium to full coverage with a luminous finish. Perfect for all skin types, this foundation hydrates while providing a flawless complexion that lasts all day.',
            'ingredients': 'Water, Cyclopentasiloxane, Dimethicone, Glycerin, Phenyl Trimethicone, PEG-10 Dimethicone, Alcohol Denat., Bis-PEG/PPG-14/14 Dimethicone, Phenoxyethanol, Sodium Chloride, Nylon-12, Caprylyl Glycol, Tocopheryl Acetate, Fragrance',
            'price': 30.00,
            'has_variants': True,
            'is_featured': True,
            'variants': [
                {'name': 'Fair (01)', 'sku_suffix': '01'},
                {'name': 'Light (02)', 'sku_suffix': '02'},
                {'name': 'Medium (03)', 'sku_suffix': '03'},
                {'name': 'Tan (04)', 'sku_suffix': '04'},
                {'name': 'Deep (05)', 'sku_suffix': '05'},
            ]
        },
        {
            'category': categories['face'],
            'name': 'Perfecting Concealer',
            'description': 'This creamy, full-coverage concealer instantly hides dark circles, blemishes, and imperfections with a natural matte finish that won\'t crease or cake. The long-wearing formula stays put for up to 24 hours.',
            'ingredients': 'Isododecane, Dimethicone, Trimethylsiloxysilicate, Polyethylene, Disteardimonium Hectorite, Tocopheryl Acetate, Phenoxyethanol, Titanium Dioxide, Iron Oxides',
            'price': 30.00,
            'has_variants': True,
            'is_featured': False,
            'variants': [
                {'name': 'Fair (01)', 'sku_suffix': '01'},
                {'name': 'Light (02)', 'sku_suffix': '02'},
                {'name': 'Medium (03)', 'sku_suffix': '03'},
                {'name': 'Tan (04)', 'sku_suffix': '04'},
                {'name': 'Deep (05)', 'sku_suffix': '05'},
            ]
        },
        {
            'category': categories['lips'],
            'name': 'Velvet Matte Lipstick',
            'description': 'A richly pigmented lipstick with a luxurious matte finish that feels weightless on the lips. This non-drying formula provides full coverage color that lasts for hours without feathering or bleeding.',
            'ingredients': 'Dimethicone, Isononyl Isononanoate, Polyethylene, Aluminum Starch Octenylsuccinate, Silica, Isohexadecane, Synthetic Fluorphlogopite, Calcium Aluminum Borosilicate, Caprylyl Glycol, Ethylhexylglycerin, Fragrance',
            'price': 30.00,
            'has_variants': True,
            'is_featured': True,
            'variants': [
                {'name': 'Bare Rose', 'sku_suffix': 'BR'},
                {'name': 'Mauve Magic', 'sku_suffix': 'MM'},
                {'name': 'Ruby Red', 'sku_suffix': 'RR'},
                {'name': 'Berry Bliss', 'sku_suffix': 'BB'},
                {'name': 'Coral Crush', 'sku_suffix': 'CC'},
            ]
        },
        {
            'category': categories['lips'],
            'name': 'Hydrating Lip Gloss',
            'description': 'This ultra-shiny, non-sticky lip gloss delivers brilliant shine and rich color while conditioning and hydrating lips. Infused with vitamin E and jojoba oil for comfortable wear and a plumping effect.',
            'ingredients': 'Polybutene, Hydrogenated Polyisobutene, Hydroxystearic Acid, Jojoba Oil, Tocopheryl Acetate, Ethylhexyl Palmitate, Silica, Fragrance, Benzyl Benzoate',
            'price': 30.00,
            'has_variants': True,
            'is_featured': False,
            'variants': [
                {'name': 'Crystal Clear', 'sku_suffix': 'CC'},
                {'name': 'Pink Shimmer', 'sku_suffix': 'PS'},
                {'name': 'Peachy Glow', 'sku_suffix': 'PG'},
                {'name': 'Berry Sparkle', 'sku_suffix': 'BS'},
            ]
        },
        {
            'category': categories['eyes'],
            'name': 'Ultimate Eyeshadow Palette',
            'description': 'A versatile eyeshadow palette featuring 12 highly pigmented shades in matte, shimmer, and metallic finishes. Create endless eye looks from subtle daytime to dramatic evening styles with these blendable, long-wearing formulas.',
            'ingredients': 'Talc, Mica, Magnesium Stearate, Silica, Ethylhexyl Palmitate, Dimethicone, Mineral Oil, Polybutene, Phenoxyethanol, Tocopheryl Acetate. May Contain: Titanium Dioxide, Iron Oxides, Carmine, Ultramarines',
            'price': 30.00,
            'has_variants': True,
            'is_featured': True,
            'variants': [
                {'name': 'Nude Neutrals', 'sku_suffix': 'NN'},
                {'name': 'Smoky Drama', 'sku_suffix': 'SD'},
                {'name': 'Rose Gold Edition', 'sku_suffix': 'RG'},
            ]
        },
        {
            'category': categories['eyes'],
            'name': 'Precision Liquid Eyeliner',
            'description': 'A waterproof liquid eyeliner with an ultra-fine brush tip for precise application. The quick-drying, smudge-proof formula creates defined lines that stay put for up to 24 hours without fading or flaking.',
            'ingredients': 'Water, Styrene/Acrylates/Ammonium Methacrylate Copolymer, Butylene Glycol, Alcohol, Peg-60 Hydrogenated Castor Oil, Phenoxyethanol, Sodium Laureth-12 Sulfate, Caprylyl Glycol, Ethylhexylglycerin, Carbon Black',
            'price': 30.00,
            'has_variants': True,
            'is_featured': False,
            'variants': [
                {'name': 'Jet Black', 'sku_suffix': 'JB'},
                {'name': 'Brown', 'sku_suffix': 'BR'},
            ]
        },
        {
            'category': categories['cheeks'],
            'name': 'Satin Blush',
            'description': 'A silky powder blush that glides on smoothly for a natural-looking flush of color. The buildable, blendable formula provides a luminous finish that enhances the cheeks with a radiant glow.',
            'ingredients': 'Talc, Mica, Magnesium Stearate, Dimethicone, Nylon-12, Zinc Stearate, Hydrogenated Polyisobutene, Ethylhexyl Palmitate, Fragrance, Tocopheryl Acetate. May Contain: Titanium Dioxide, Iron Oxides, Red 7 Lake, Yellow 5 Lake',
            'price': 30.00,
            'has_variants': True,
            'is_featured': True,
            'variants': [
                {'name': 'Peach Glow', 'sku_suffix': 'PG'},
                {'name': 'Rose Flush', 'sku_suffix': 'RF'},
                {'name': 'Berry Bliss', 'sku_suffix': 'BB'},
                {'name': 'Coral Pop', 'sku_suffix': 'CP'},
            ]
        },
        {
            'category': categories['cheeks'],
            'name': 'Highlighting Powder',
            'description': 'A finely-milled highlighting powder that gives skin a soft, luminous glow. The lightweight formula blends seamlessly for a subtle radiance that can be built up for a more intense highlight.',
            'ingredients': 'Mica, Talc, Dimethicone, Isopropyl Palmitate, Synthetic Fluorphlogopite, Zinc Stearate, Boron Nitride, Silica, Nylon-12, Phenoxyethanol, Caprylyl Glycol, Tin Oxide',
            'price': 30.00,
            'has_variants': True,
            'is_featured': False,
            'variants': [
                {'name': 'Champagne Pop', 'sku_suffix': 'CP'},
                {'name': 'Golden Glow', 'sku_suffix': 'GG'},
                {'name': 'Rose Gold', 'sku_suffix': 'RG'},
            ]
        },
        {
            'category': categories['skincare'],
            'name': 'Hydrating Facial Serum',
            'description': 'A lightweight, fast-absorbing serum that delivers intense hydration and nourishment to the skin. Formulated with hyaluronic acid and vitamin E to plump, smooth, and rejuvenate for a radiant complexion.',
            'ingredients': 'Water, Glycerin, Butylene Glycol, Sodium Hyaluronate, Tocopheryl Acetate, Panthenol, Allantoin, Phenoxyethanol, Ethylhexylglycerin, Hydroxyethylcellulose, Disodium EDTA',
            'price': 30.00,
            'has_variants': False,
            'is_featured': True,
        },
        {
            'category': categories['skincare'],
            'name': 'Clarifying Clay Mask',
            'description': 'A purifying clay mask that deeply cleanses and detoxifies the skin. Formulated with kaolin clay and charcoal to draw out impurities, absorb excess oil, and minimize the appearance of pores for a clearer complexion.',
            'ingredients': 'Water, Kaolin, Bentonite, Glycerin, Charcoal Powder, Montmorillonite, Butylene Glycol, Pentylene Glycol, Betaine, Caprylyl Glycol, Ethylhexylglycerin, Phenoxyethanol',
            'price': 30.00,
            'has_variants': False,
            'is_featured': False,
        },
        {
            'category': categories['brushes'],
            'name': 'Professional Makeup Brush Set',
            'description': 'A comprehensive set of 10 professional-quality makeup brushes for face and eyes. Crafted with soft, synthetic bristles and sleek handles for precise application and seamless blending of all makeup products.',
            'ingredients': 'Synthetic bristles, aluminum ferrules, wooden handles',
            'price': 30.00,
            'has_variants': False,
            'is_featured': True,
        },
        {
            'category': categories['brushes'],
            'name': 'Beauty Blender Sponge',
            'description': 'A soft, latex-free makeup sponge designed for the application and blending of liquid and cream products. The unique egg shape and rounded surfaces allow for streak-free application on all areas of the face.',
            'ingredients': 'Non-latex foam',
            'price': 30.00,
            'has_variants': False,
            'is_featured': False,
        },
    ]
    
    for product_data in products:
        # Get or create the product
        has_variants = product_data.get('has_variants', False)
        is_featured = product_data.get('is_featured', False)
        
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'category': product_data['category'],
                'description': product_data['description'],
                'ingredients': product_data['ingredients'],
                'price': product_data['price'],
                'has_variants': has_variants,
                'is_featured': is_featured,
                'sku': f"SKU-{product_data['name'][:3].upper()}",
            }
        )
        
        if created:
            print(f"Created product: {product.name}")
            
            # Add variants if the product has them
            if has_variants and 'variants' in product_data:
                for variant_data in product_data['variants']:
                    variant, variant_created = ProductVariant.objects.get_or_create(
                        product=product,
                        name=variant_data['name'],
                        defaults={
                            'sku_suffix': variant_data['sku_suffix'],
                            'price_adjustment': 0.00,
                            'stock_qty': 50,
                        }
                    )
                    if variant_created:
                        print(f"  - Added variant: {variant.name}")
        else:
            print(f"Product already exists: {product.name}")


if __name__ == "__main__":
    print("Adding Glossy cosmetics products to the database...")
    categories = add_categories()
    add_products(categories)
    print("Completed adding products!")