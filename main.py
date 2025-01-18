from login import FacebookLogin
from forgot_password import FacebookForgotPassword

if __name__ == "__main__":
    # Run the Facebook login functionality
    fb_login = FacebookLogin("chromedriver.exe", "seleniumtest.cinec@gmail.com", "SeleniumTest@123")
    fb_login.login()
    fb_login.logout()
    fb_login.close_browser()
    

    # Run the Facebook forgot password functionality
    fb_forgot_password = FacebookForgotPassword("chromedriver.exe", "seleniumtest.cinec@gmail.com", "SeleniumTest@66162219")
    fb_forgot_password.forgot_password()
    fb_forgot_password.logout()
    fb_forgot_password.close_browser()
