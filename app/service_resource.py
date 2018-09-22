from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader('static', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)


def render(tpl, **kwargs) -> object:
    """Function for rendering templates"""
    template = env.get_template(tpl)
    content = template.render(kwargs)
    return content


def home() -> object:
    """Function for rendering home page"""
    content = render('home.html', site='SeleniumTests')
    return content


def page404() -> object:
    """Function for rendering 404 page"""
    content = render('page404.html', site='SeleniumTests')
    return content
