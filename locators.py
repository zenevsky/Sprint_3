# Линк "Зарегистрироваться" в форме логина
register_form_button = "//a[contains(text(),'Зарегистрироваться')]"

# Инпут "Имя" в форме регистрации
register_name_input = "//label[contains(text(),'Имя')]/parent::div/input"

# Инпут "Email" в форме регистрации
register_email_input = "//label[contains(text(),'Email')]/parent::div/input"

# Инпут "Пароль" в форме регистрации
register_password_input = "//label[contains(text(),'Пароль')]/parent::div/input"

# Кнопка "Зарегистрироваться" в форме регистрации
register_button = ".//button[text()='Зарегистрироваться']"

# Хинт "Некорректный пароль" поля "Пароль" на странице регистрации
register_error_hint = ".//p[contains(text(),'Некорректный пароль')]"

# Инпут "Email" в форме логина
login_email_input = "//label[contains(text(),'Email')]/parent::div/input"

# Инпут "Пароль" в форме логина
login_password_input = "//label[contains(text(),'Пароль')]/parent::div/input"

# Кнопка "Войти" в форме логина
login_button = ".//button[contains(text(),'Войти')]"

# Кнопка "Войти" на главной странице
login_from_main_page_button = "//button[text()='Войти в аккаунт']"

# Кнопка "Личный кабинет" на главной странице
profile_button = "//p[contains(text(),'Личный Кабинет')]"

# Инпут "Логин" в профиле
profile_email_input = "//label[contains(text(),'Логин')]/parent::div/input"

# Кнопка "Выйти" в профиле
profile_logout_button = "//button[contains(text(),'Выход')]"

# Инпут "Логин" в профиле
login_from_register_button = "//a[contains(text(),'Войти')]"

# Линк "Восстановить пароль" на странице логина
recover_password_button = "//a[contains(text(),'Восстановить пароль')]"

# Кнопка "Конструктор" на главной странице
constructor_button = "//p[contains(text(),'Конструктор')]"

# Заголовок "Соберите бургер" на главной странице
make_your_burger_header = "//h1[contains(text(),'Соберите бургер')]"

# Лого на главной
logo_div = "//div[@class='AppHeader_header__logo__2D0X2']"

# Таб "Булки" в конструкторе на главной странице
buns_section = "//span[text()='Булки']"

# Активный таб "Булки" в конструкторе на главной странице
buns_section_is_selected = "//span[text()='Булки']/parent::*[contains(@class, 'current')]"

# Таб "Соусы" в конструкторе на главной странице
sauces_section = "//span[text()='Соусы']"

# Таб "Соусы" в конструкторе на главной странице
sauces_section_is_selected = "//span[text()='Соусы']/parent::*[contains(@class, 'current')]"

# Таб "Начинки" в конструкторе на главной странице
stuffing_section = "//span[text()='Начинки']"

# Таб "Начинки" в конструкторе на главной странице
stuffing_section_is_selected = "//span[text()='Начинки']/parent::*[contains(@class, 'current')]"
