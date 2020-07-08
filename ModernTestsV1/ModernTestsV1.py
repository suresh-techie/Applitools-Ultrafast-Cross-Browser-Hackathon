from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import os
import time


from applitools.selenium import (
    VisualGridRunner,
    Eyes,
    Target,
    BatchInfo,
    BrowserType,
    DeviceName,
)


def set_up(eyes):

    # You can get your api key from the Applitools dashboard

    APPLITOOLS_API_KEY = os.environ["APPLITOOLS_API_KEY"]
    eyes.configure.set_api_key(APPLITOOLS_API_KEY)

    # create a new batch info instance and set it to the configuration
    eyes.configure.set_batch(BatchInfo("UFG Hackathon"))

    # Add browsers with different viewports
    # Add mobile emulation devices in Portrait mode
    (
        eyes.configure.add_browser(1200, 700, BrowserType.CHROME)
        .add_browser(1200, 700, BrowserType.FIREFOX)
        .add_browser(1200, 700, BrowserType.EDGE_CHROMIUM)
        .add_browser(768, 700, BrowserType.CHROME)
        .add_browser(768, 700, BrowserType.FIREFOX)
        .add_browser(768, 700, BrowserType.EDGE_CHROMIUM)
        .add_device_emulation(DeviceName.iPhone_X)
    )


def ultra_fast_test(web_driver, eyes):
    try:
        # Navigate to the url we want to test
        web_driver.get("https://demo.applitools.com/gridHackathonV1.html")
        web_driver.implicitly_wait(5)


        # Call Open on eyes to initialize a test session (Task1)
        eyes.open(
            web_driver, "Hackathon App", "Task 1", {"width": 800, "height": 600}
        )

        # checks the SearchBox element is displayed in the page

        web_driver.find_element_by_id("INPUTtext____42").click()
        time.sleep(5)
        # take screenshot for the Cross-Device Elements Test
        eyes.check("Cross-Device Elements Test", Target.window().fully().with_name("Home page"))

        # Call Open on eyes to initialize a test session (Task2)
        eyes.open(
            web_driver, "Hackathon App", "Task 2", {"width": 800, "height": 600}
        )

        web_driver.find_element_by_id("ti-filter").click()
        web_driver.find_element_by_id("filter_col")

        # Filtering black color shoes by clicking on black color Checkbox and click Filter button for results
        elements = web_driver.find_elements_by_class_name("container_check")
        for element in elements:
            print(element.text)
            if "Black" in element.text:
                element.click()
                break
        web_driver.find_element_by_id("filterBtn").click()
        web_driver.find_element_by_id("product_grid")
        time.sleep(5)

        # take screenshot for the filtered results
        eyes.check("Filter Results", Target.window().region("#product_grid"))

        # Call Open on eyes to initialize a test session (Task3)

        eyes.open(
            web_driver, "Hackathon App", "Task 3", {"width": 800, "height": 600}
        )

        # Go to the first black shoe product details
        elements = web_driver.find_elements_by_class_name("grid_item")
        elements[0].find_element_by_tag_name('a').click()

        web_driver.find_element_by_id("DIV__pageheader__66").is_displayed()
        time.sleep(5)

        # take screenshot for the Product Details
        eyes.check("Product Details test", Target.window().fully().with_name("Home page"))

        # Call Close on eyes to let the server know it should display the results
        eyes.close()
    except Exception as e:
        eyes.abort_async()
        print(e)


def tear_down(web_driver, runner):
    # Close the browser
    web_driver.quit()

    # we pass false to this method to suppress the exception that is thrown if we
    # find visual differences
    all_test_results = runner.get_all_test_results(False)
    print(all_test_results)


# Create a new chrome web driver
web_driver = Chrome(ChromeDriverManager().install())

# Create a runner with concurrency of 1
runner = VisualGridRunner(10)

# Create Eyes object with the runner, meaning it'll be a Visual Grid eyes.
eyes = Eyes(runner)

set_up(eyes)

try:
    # Execute UFG test
    ultra_fast_test(web_driver, eyes)
finally:
    tear_down(web_driver, runner)
