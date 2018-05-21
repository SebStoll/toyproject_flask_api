import sys
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, Blueprint
import settings
from api.restplus import api
from api.linear_reg.endpoints.training import ns as linear_reg_training_namespace
from api.linear_reg.endpoints.prediction import ns as linear_reg_prediction_namespace

print(sys.path)

app = Flask(__name__)


# Configure app
def configure_app(flask_app):
    #flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    #flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    #flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)
    
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(linear_reg_training_namespace)
    api.add_namespace(linear_reg_prediction_namespace)
    flask_app.register_blueprint(blueprint)
    
    #api.init_app(flask_app)
    
def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    
    # create a file handler
    handler = RotatingFileHandler('TEST_LOG.log', maxBytes=1e6, backupCount=5)
    handler.setLevel(logging.DEBUG)  
    
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter) 
    
    # add the handlers to the logger
    logger.addHandler(handler)    
    
    logger.info('Initialize app')
    initialize_app(app)
    logger.debug('Initialization done')
    app.run(debug=settings.FLASK_DEBUG)   
    
if __name__=='__main__':
    main()


