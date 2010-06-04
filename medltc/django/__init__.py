import django.conf
import medltc.mysql_config
django.conf.settings.configure(DATABASE_ENGINE='mysql',
        DATABASE_NAME = medltc.mysql_config.DATABASE_NAME,
        DATABASE_USER = medltc.mysql_config.DATABASE_USER,
        DATABASE_PASSWORD = medltc.mysql_config.DATABASE_PASSWORD,
        DATABASE_HOST = medltc.mysql_config.DATABASE_HOST,
        DATABASE_PORT = medltc.mysql_config.DATABASE_PORT)
