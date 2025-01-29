W-2 Data Extraction from Images
This project extracts key information from W-2 forms in image format using Optical Character Recognition (OCR). The information is then saved to a CSV file for further analysis or processing.

Requirements
Python 3.x
Tesseract OCR
OpenCV
pandas
Installation
1. Install Python dependencies:
Make sure you have Python 3.x installed. You can install the required Python libraries by running:

bash
Copy
Edit
pip install pytesseract opencv-python pandas
2. Install Tesseract OCR:
Download and install Tesseract OCR from the official GitHub repository: https://github.com/tesseract-ocr/tesseract
Make sure to add Tesseract to your system's PATH or specify its location in the script (see below).
3. Configure Tesseract:
In the Python script, set the path to your Tesseract executable:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows example
For macOS and Linux, Tesseract is often installed in the system PATH, so you may not need to change this line.

Usage
Prepare the Image Folder:

Place all the W-2 image files (in formats like .png, .jpg, .jpeg, .tiff) into a folder.
Update the image_folder variable in the script to point to the folder containing the images.
python
Copy
Edit
image_folder = r"D:/IncomeTaxReturns/images"  # Update path to your folder
Run the Script:

Run the script using Python:
bash
Copy
Edit
python w2_data_extraction.py
The script will:

Process all the images in the specified folder.
Extract data such as Employer's Name, Employee's SSN, Wages, and other relevant fields.
Save the extracted data into a CSV file (updated_w2_data.csv by default).
Output:

The extracted data will be saved in a CSV file. The file name is specified in the script under output_csv.
Example of the output CSV format:

File Name	EIN	Employer's Name	Employee Name	Wages	Federal Income Tax Withheld	...
W2_Jan2025.jpg	12-3456789	XYZ Corp	John Doe	50000	5000	...
W2_Feb2025.jpg	98-7654321	ABC Corp	Jane Smith	45000	4500	...
Customization:

You can modify the regex patterns in the script to extract different fields from the W-2 forms, depending on your needs. Refer to the patterns dictionary in the code to make changes.
Notes
The accuracy of OCR depends on the quality of the images. Images with poor resolution or unusual fonts may lead to lower accuracy.
If the script is not extracting certain fields properly, consider improving the image quality or tweaking the preprocessing steps (like thresholding or resizing).
