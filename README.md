# Applitools-Ultrafast-Cross-Browser-Hackathon

### Pre-requisites:

1. Install required libraries using `requirements.txt` file. Pip command to install libraries `pip install -r requirements.txt`
2. Ensure Chrome browser is installed on your machine.
3. Download Chrome Webdriver on your machine and add chromedriver path in system environment variable `PATH`.
4. Add `APPLITOOLS_API_KEY` variable in system environment variables . This step is required to access Applitools API Keys in python scripts.  
   `APPLITOOLS_API_KEY = Copied API KEY from Applitools Dashboard`

### Steps to execute the test scripts
1. Clone the [Github repo](https://github.com/suresh1995/Applitools-Ultrafast-Cross-Browser-Hackathon) by using the command
   `git clone https://github.com/suresh1995/Applitools-Ultrafast-Cross-Browser-Hackathon.git`, or download zip file and unzip it
2. `cd Applitools-Ultrafast-Cross-Browser-Hackathon`
3.  To run ModernTestsV1 test scripts  
    `python ModernTestsV1.py`
4.  To run ModernTestsV2 test scripts  
    `python ModernTestsV2.py`
5. To run python unit tests in TraditionalTestsV1 folder   
   `python -m unittest TraditionalTestsV1Script.py`
5. To run python unit tests in TraditionalTestsV2 folder   
   `python -m unittest TraditionalTestsV2Script.py` 