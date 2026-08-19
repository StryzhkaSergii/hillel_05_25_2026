from dynaconf import Dynaconf
from os.path import join
from constants import BASE_PROJECT_PATH


settings = Dynaconf(
    settings_files=[join(BASE_PROJECT_PATH, "base_settings.ini")],  # path/glob
    environments=True,  # activate layered environments
    envvar_prefix="DYNACONF",  # `export MYAPP_FOO=bar`
    load_dotenv=True,  # read a .env file
)