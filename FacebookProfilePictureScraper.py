import chromedriver_autoinstaller
from selenium import webdriver
from urllib import request
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()  # Initialise options class to set options for the driver
options.headless = False  # Change the value to hide or show the browser
options.add_argument("--disable-notifications")  # Disable notifications
path = chromedriver_autoinstaller.install()  # Installs chromedriver.exe latest version for chrome and returns path
driver = webdriver.Chrome(executable_path=path, options=options)  # Initialise the driver

# Alphabet list for generating all possible combination of username
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

output = ''


# The function below logs in to facebook so that one can access even private accounts to get there profile picture
def login(email, password):
    driver.get("https://en-gb.facebook.com/login/")  # Login page website
    email_box = driver.find_element_by_id("email")  # Email box element
    email_box.send_keys(email)  # Enter email into email box element
    password_box = driver.find_element_by_id("pass")  # Password box element
    password_box.send_keys(password)  # Enter password into password box element
    login_btn = driver.find_element_by_id("loginbutton")  # Login button element
    login_btn.click()  # Click on the login button


# Function to scrape profile picture
def profile_picture_capture_function(username):
    driver.get("https://facebook.com/" + username)  # The link that gives the profile page of the entered element
    try:
        display_picture = driver.find_element_by_xpath("""//*[@id="u_0_w"]/img""")  # Display picture element
        image_url = display_picture.get_attribute("src")  # Get the image url
        profile_name = driver.find_element_by_xpath("""//*[@id="fb-timeline-cover-name"]/a""")  # Get profile name
        name = profile_name.text.replace(" ", "") + ".png"  # Edit the profile name
        request.urlretrieve(image_url, name)  # Download and save the profile picture by the profile name
    except NoSuchElementException:  # Except and pass the no such element exception
        pass


# Username generator function
# Check out the UsernameGenerator.py file for explanation about the function
def username_generator_function(function_index, output_string):
    for alphabet in alphabet_list:
        output_string += alphabet
        if function_index != 0:
            function_index -= 1
            function_index, output_string = username_generator_function(function_index, output_string)
        else:
            # Call the profile picture capture and save function
            profile_picture_capture_function(output_string)
        output_string = output_string[:-1]
    function_index += 1
    return function_index, output_string


if __name__ == '__main__':
    # The email and password must be of a account without 2 factor authentication (2fa) enabled
    input_email = input("Enter your email: ")  # Get the username
    input_password = input("Enter your password: ")  # Get the password
    login(input_email, input_password)  # Call the login function
    # Comment out the main function till this point if you just want to scrape public accounts
    # Set the max string length of the username generated
    string_length = int(input("Enter the max username length you want to try: "))
    for num in range(string_length):
        username_generator_function(num, output)  # Call the username generator function
