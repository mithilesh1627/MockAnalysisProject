# MockAnalysis

MockAnalysis is an automation tool designed to streamline web scraping and data analysis tasks using Selenium and Python. This project demonstrates efficient data extraction and processing from a specified web portal.

## Features

- **Automated Login**: Automatically logs into the specified portal using a phone number.
- **Data Navigation**: Navigates through various test sections to gather required data.
- **Dynamic Interaction**: Interacts with dynamically loaded elements on the webpage.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/MockAnalysis.git
   cd MockAnalysis
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Set up your phone number as an environment variable:
   - On Unix-based systems:
     ```bash
     export MOBILE_NUMBER='your_phone_number'
     ```
   - On Windows (Command Prompt):
     ```cmd
     set MOBILE_NUMBER=your_phone_number
     ```

## Usage

1. **Run the Script**:
   Execute the Python script:
   ```bash
   python main.py
   ```

2. **Functionality**:
   - The script will open a browser, navigate to the login page, and log in using the provided phone number.
   - It will then navigate through specified test sections and perform defined actions.

## Project Structure

- `main.py`: The main script containing the Selenium automation logic.
- `demo.py`: A supplementary module containing additional functions (like `Sectional_Summary`).
- `requirements.txt`: Lists all the Python dependencies.

## Requirements

- Python 3.x
- Selenium
- Edge WebDriver (ensure it's installed and added to PATH)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Contact
For any questions or issues, please reach out via GitHub or contact me directly through [LinkedIn](https://www.linkedin.com/in/mithilesh1627).
