import softest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Get the browser, viewport and device info from a variable like below or from a file or environment variable.
browser = "Chrome"
viewport = "900X700"
device = "Laptop"
weburl = "https://demo.applitools.com/gridHackathonV1.html"


# A Helper to print the test result in the following format:
# Task: <Task Number>, Test Name: <Test Name>, DOM Id:: <id>, Browser: <Browser>, Viewport: <Width x Height>, Device<Device type>, Status: <Pass | Fail>
#
# Example: Task: 1, Test Name: Search field is displayed, DOM Id: DIV__customsear__41, Browser: Chrome, Viewport: 1200 x 700, Device: Laptop, Status: Pass
#
# @param task                    int - 1, 2 or 3
# @param testName.               string - Something meaningful. E.g. 1.1 Search field is displayed
# @param domId                   string - DOM ID of the element
# @param comparisonResult        boolean - The result of comparing the "Expected" value and the "Actual" value.
# @return                        boolean - returns the same comparison result back so that it can be used for further Assertions in the test code.


def HackathonReport(task, testName, domId,comparisonResult):
    f = open("traditional-V1-TestResults.txt", "a")

    report_content = "Task: {task}, Test Name: {test_name}, DOM Id: {dom_id}, Viewport: {viewport}, Device: {device}" \
                     ", Status: {status}\n".format(task=task, test_name=testName, dom_id=domId, viewport=viewport,
                                                 device=device, status=comparisonResult)
    f.write(report_content)

    f.close()

    # returns the result so that it can be used for further Assertions in the test code.
    return comparisonResult


class Testing(softest.TestCase):

    def test_sample(self):
        # create a driver object for chrome
        # ChromeDriver.exe file is added to the python folder
        driver = webdriver.Chrome()
        driver.set_window_size(900, 700)
        driver.implicitly_wait(5)
        driver.get(weburl)

        # to check searchbox is displayed in the page
        searchField = "DIV__customsear__41"
        searchFieldElement = driver.find_element_by_id(searchField)
        self.soft_assert(self.assertTrue, HackathonReport(1, "Search field is displayed in the page", searchField, searchFieldElement.is_displayed()))

        # check banner in the page
        topBanner = "DIV__topbanner__187"
        topBannerElement = driver.find_element_by_id(topBanner)
        self.soft_assert(self.assertTrue, HackathonReport(1, "Top banner is displayed in the page", topBanner, topBannerElement.is_displayed()))

        actions = ActionChains(driver)
        productGrid = "product_grid"
        actions.move_to_element(driver.find_element_by_id("product_grid")).perform()
        productGridElement = driver.find_element_by_id(productGrid)
        self.soft_assert(self.assertTrue, HackathonReport(1, "Product Grid is displayed in the page", productGrid, productGridElement.is_displayed()))

        # Check Filter displayed in the page
        ti_filter = "ti-filter"
        ti_filterElement = driver.find_element_by_id(ti_filter)
        self.soft_assert(self.assertTrue, HackathonReport(2, "Filter is displayed in the page", ti_filter, ti_filterElement.is_displayed()))
        ti_filterElement.click()
        driver.find_element_by_id("filter_col")

        # Filter Black color by clicking on the Black checkbox element
        elements = driver.find_elements_by_class_name("container_check")
        for element in elements:
            print(element.text)
            if "Black" in element.text:
                element.is_displayed()
                self.soft_assert(self.assertTrue,
                                 HackathonReport(2, "Black color checkbox element is displayed in the page", element, element.is_displayed()))

                element.click()
                break

        time.sleep(5)

        # Check Filter button is displayed in the page
        filterButton = "filterBtn"
        filterButtonElement = driver.find_element_by_id(filterButton)
        self.soft_assert(self.assertTrue, HackathonReport(2, "Check Filter Button is displayed in the page", filterButton, filterButtonElement.is_displayed()))
        filterButtonElement.click()
        time.sleep(5)

        gridItem = "grid_item"
        elements = driver.find_elements_by_class_name(gridItem)
        print(elements)
        if len(elements) == 2:
            self.soft_assert(self.assertTrue,
                             HackathonReport(2, "Total number of products filtered for Black color is 2", gridItem,
                                            True))
        else:
            self.soft_assert(self.assertTrue,
                             HackathonReport(2, "Other color products also displayed in the page along with black color: ERROR in Filtering", gridItem,
                                             True))

        firstProductElement = elements[0].find_element_by_tag_name('a')
        self.soft_assert(self.assertTrue, HackathonReport(3, "Clicking on First product item in the grid item", gridItem, firstProductElement.is_displayed()))
        firstProductElement.click()

        productPageHeader = "DIV__pageheader__66"
        productPageHeaderElement = driver.find_element_by_id(productPageHeader)
        self.soft_assert(self.assertTrue, HackathonReport(3, "First product page header is displayed", productPageHeader, productPageHeaderElement.is_displayed()))
        if "Appli Air x Night" in productPageHeaderElement.text:
            self.soft_assert(self.assertTrue,
                             HackathonReport(3, "Verify product name", productPageHeader,
                                             True))
        self.assert_all()



if __name__ == '__main__':
    softest.main()