import os
import cv2
import pytesseract
import re
import pandas as pd

# Set Tesseract OCR path (Update for Windows if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Folder containing W-2 images
image_folder = r"D:/IncomeTaxReturns/images"  # Update path
output_csv = r"D:/IncomeTaxReturns/updated_w2_data.csv"

# Define regex patterns for extracting W-2 fields
patterns = {
    "File_BaseName": r"(.*)",
    "EIN": r"Employer\s*ID\s*Number[:\s]*([\d\-]+)",
    "Employer's Name": r"Employer\s*Name[:\s]*([A-Za-z\s&,.]+)",
    "Employer's Street Address": r"Employer\s*Address[:\s]*(.*)",
    "Employer's City-State-Zip": r"Employer\s*City,\s*State\s*ZIP[:\s]*(.*)",
    "Employee Social Security Number": r"Employee\s*SSN[:\s]*([\d\-]+)",
    "Employee Name": r"Employee\s*Name[:\s]*([A-Za-z\s]+)",
    "Employee Street Address": r"Employee\s*Address[:\s]*(.*)",
    "Employee's City-State-Zip": r"Employee\s*City,\s*State\s*ZIP[:\s]*(.*)",
    "Control Number": r"Control\s*Number[:\s]*([\w\-]+)",
    "Wages, Tips & other Compensation": r"Wages,\s*Tips,\s*Other\s*Compensation[:\s]*([\d,\.]+)",
    "Federal Income Tax Withheld": r"Federal\s*Income\s*Tax\s*Withheld[:\s]*([\d,\.]+)",
    "Social Security Wages": r"Social\s*Security\s*Wages[:\s]*([\d,\.]+)",
    "Social Security Tax Withheld": r"Social\s*Security\s*Tax\s*Withheld[:\s]*([\d,\.]+)",
    "Medicare Wages & Tips": r"Medicare\s*Wages[:\s]*([\d,\.]+)",
    "Medicare Tax withheld": r"Medicare\s*Tax\s*Withheld[:\s]*([\d,\.]+)",
    "State_1": r"State[:\s]*([A-Z]{2})",
    "Employee State ID_1": r"Employee\s*State\s*ID[:\s]*([\w\-]+)",
    "State wages, tips,etc_1": r"State\s*Wages[:\s]*([\d,\.]+)",
    "State Income Tax_1": r"State\s*Income\s*Tax[:\s]*([\d,\.]+)",
    "Employer Name": r"Employer\s*Name[:\s]*([A-Za-z\s&,.]+)",
    "Employer Address": r"Employer\s*Address[:\s]*(.*)",
    "Employee Address": r"Employee\s*Address[:\s]*(.*)",
    "Employee SSN": r"Employee\s*SSN[:\s]*([\d\-]+)",
    "Wages": r"Wages[:\s]*([\d,\.]+)",
    "Medicare Wages": r"Medicare\s*Wages[:\s]*([\d,\.]+)",
    "State Wages": r"State\s*Wages[:\s]*([\d,\.]+)"
}

# Preprocessing function for better OCR accuracy
def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)[1]  # Apply thresholding
    return image

# Extract text using Tesseract OCR and match fields using regex
def extract_data_from_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    extracted_text = pytesseract.image_to_string(preprocessed_image)  # Extract text
    
    extracted_data = {"File Name": os.path.basename(image_path)}  # Store the file name
    
    for field, pattern in patterns.items():
        match = re.search(pattern, extracted_text, re.IGNORECASE)
        extracted_data[field] = match.group(1).strip() if match else "Not Found"
    
    return extracted_data

# Process all images in the folder
all_extracted_data = []
for image_file in os.listdir(image_folder):
    if image_file.lower().endswith((".png", ".jpg", ".jpeg", ".tiff")):  # Process image files
        image_path = os.path.join(image_folder, image_file)
        extracted_data = extract_data_from_image(image_path)
        all_extracted_data.append(extracted_data)

# Convert extracted data to DataFrame and save as CSV
if all_extracted_data:
    df = pd.DataFrame(all_extracted_data)
    df.to_csv(output_csv, index=False)
    print(f"Data extraction complete! Saved to {output_csv}")
else:
    print("No valid images found or extracted.")
