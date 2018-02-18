from app import app_instance, db_instance
from app.models import Companyinfo

@app_instance.shell_context_processor
def make_shell_context():
    return {'db': db_instance, 'companyinfo': Companyinfo}
