import cv2
import pytesseract
from PIL import Image
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at the path: {image_path}")
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image. Please check the file format and path.")
    
    return image

def main(image_path):
    try:
        # Load image
        image = load_image(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # OCR to extract text
        text = pytesseract.image_to_string(gray)
        print("Extracted Text: ", text)

        # Edge detection
        edges = cv2.Canny(gray, 100, 200)

        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours and save visual elements
        visual_elements = []
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            element = image[y:y+h, x:x+w]
            visual_elements.append(element)
            cv2.imwrite(f'element_{i}.png', element)
        
        # Create HTML structure
        html_content = "<html><body>"
        # Add extracted text
        html_content += f"<p>{text}</p>"

        # Add visual elements
        for i in range(len(visual_elements)):
            html_content += f'<img src="element_{i}.png" alt="Visual Element {i}"><br>'

        html_content += "</body></html>"

        # Save HTML to file
        with open('output.html', 'w') as f:
            f.write(html_content)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:

        
        print(val_error)
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the image
image_path = './OCR/OCR_Test1.jpg'
# Run the main function
main(image_path)
