import os
from application import create_app

if __name__ == '__main__':
    if os.environ.get('YOUC_ENV_IS_PROD', 'FALSE').upper() == 'TRUE':
        app = create_app('prod')
    else:
        app = create_app('dev')

    app.run()