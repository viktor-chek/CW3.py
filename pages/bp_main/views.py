from flask import Blueprint, render_template
import utils


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

data_json = "data/data.json"


@main_blueprint.route("/")  # Представление главной страницы
def main_page():
    all_posts = utils.get_posts_all(data_json)
    return render_template("index.html", data=all_posts)

