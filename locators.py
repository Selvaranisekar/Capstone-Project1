class TestLocators:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    Email = 'username'
    Password = 'password'
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    Profile_image = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img'
    Logout_button = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
    pim_module = "//span[normalize-space()='PIM']"
    Add_employee = "//button[normalize-space()='Add']"
    first_name = "//input[@placeholder='First Name']"
    mid_name = "//input[@placeholder='Middle Name']"
    last_name = "//input[@placeholder='Last Name']"
    emp_id = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    save = "//button[normalize-space()='Save']"
    emp_list = "//a[normalize-space()='Employee List']"
    edit = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[9]/div[1]/button[2]"
    license_no = "//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[2]/div[1]/div[1]/div[2]/input[1]"
    delete = "(//button[@type='button'])[5]"
    popup = "//button[normalize-space()='Yes, Delete']"
