from flask import Flask
from models import db
from werkzeug.utils import import_string

bps = ['jade_ims.views.dashboard:dashboard',
       'jade_ims.views.install:install',
       'jade_ims.views.login:login',
       'jade_ims.views.sale:sale',
       'jade_ims.views.user:user',
       'jade_ims.views.purchase.inputbill:inputbill',
       'jade_ims.views.purchase.supplier:supplier',
       'jade_ims.views.stock.enterstockbill:enterstockbill',
       'jade_ims.views.stock.leavestockbill:leavestockbill',
       'jade_ims.views.stock.stock:stock'
       ]


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    db.init_app(app)

    for path in bps:
        bp = import_string(path)
        app.register_blueprint(bp)

    return app
