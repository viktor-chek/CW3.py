from flask import Flask
from pages.bp_main.views import main_blueprint
from pages.bp_post_page.views import post_blueprint  # Импорт всех блупринтов
from pages.bp_search.views import search_blueprint
from pages.bp_user_page.views import user_blueprint
from pages.bp_errors.errors import errors_blueprint
from pages.bp_api.views import api_blueprint


app = Flask(__name__)  # Создание экземпляра фласк

app.config["JSON_AS_ASCII"] = False


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)  # Регистрация блупринтов
app.register_blueprint(user_blueprint)
app.register_blueprint(errors_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run()  # Запуск приложения
