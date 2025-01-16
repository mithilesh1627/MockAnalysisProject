# Mock Analysis Automation with Selenium

This project automates the analysis of mock tests from a online education platform using Selenium WebDriver. The automation includes logging into the platform, navigating through mock tests, capturing question and answer screenshots, and compiling the results into Excel files for further analysis.

## Features
- **Automated Login**: Logs into the platform using a mobile number.
- **Mock Test Analysis**: Navigates through mock tests, captures screenshots, and analyzes results.
- **Sectional Summary**: Saves details of each question, including status (Correct, Incorrect, Unattempted) and time spent, into Excel files.
- **Topic-wise Test Analysis**: Analyzes tests based on specific topics of Maths, Logical Reasoning, and Computer Concepts.

## Project Structure

```
.
├── MainProgram.py          # Main script to execute the automation
├── MockAnalysis.py         # Handles mock test result analysis
├── Login.py                # Manages login process
├── Screenshot.py           # Handles screenshot operations and image merging
├── TopicTest.py            # Automates the topic-wise test analysis
```

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Selenium**: Install Selenium using pip:
 ```bash
  pip install selenium
  ```
- **Edge WebDriver**: Ensure Microsoft Edge WebDriver matches your Edge browser version.
- **Pandas**: Install Pandas for Excel file handling:
- **numpy**: NumPy is a Python library used for working with arrays
  ```bash
  pip install pandas
  pip install numpy
  ```
- **OpenCV**: For image processing:
  ```bash
  pip install opencv-python
  ```

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mithilesh1627/MockAnalysisProject.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd MockAnalysisProject
   ```

3. **Install Dependencies**:
   Install the required Python packages as mentioned in the prerequisites section.

4. **Setup Environment Variables**:
   Set your mobile number as an environment variable:
   ```bash
   export MOBILE_NUMBER="your_mobile_number"
   ```

## Usage

1. **Run the Main Program**:
   ```bash
   python MainProgram.py
   ```

2. **Customization**:
   - Modify `Mock_num`, `login_page_link`, and `Mock_Section_link` in `MainProgram.py` to suit your needs.
   - Adjust sleep timings in the code if needed, based on network speed or platform response time.

3. **Output**:
   - Screenshots and Excel files will be saved in the specified folders for review.

## How It Works

1. **Login**: Logs into the platform using the provided mobile number.
2. **Navigation**: Navigates to the mock test section and opens each test sequentially.
3. **Analysis**: Captures screenshots of each question and compiles the results into Excel files.
4. **Result Compilation**: Saves the analyzed data into structured folders for easy access.
