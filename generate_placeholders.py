import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_image(filename, text, size=(500, 300), bg_color=(240, 240, 240), 
                             text_color=(100, 100, 100)):
    """Create a simple placeholder image with text."""
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a system font, falling back to default if not found
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (150, 30)
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    # Draw the text
    draw.text(position, text, fill=text_color, font=font)
    
    # Save the image
    img_path = os.path.join('static', 'images', filename)
    img.save(img_path)
    print(f"Created {img_path}")

def main():
    # Create directory if it doesn't exist
    os.makedirs(os.path.join('static', 'images'), exist_ok=True)
    
    # Create placeholder images
    create_placeholder_image('placeholder.png', 'Placeholder Image')
    create_placeholder_image('404.png', 'Page Not Found')
    create_placeholder_image('500.png', 'Server Error')
    create_placeholder_image('403.png', 'Access Denied')
    create_placeholder_image('coming-soon.png', 'Coming Soon')

if __name__ == "__main__":
    main()