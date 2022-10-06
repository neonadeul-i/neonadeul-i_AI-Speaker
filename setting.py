import configparser

def config_generator():
   config = configparser.ConfigParser()

   config.read('config.ini')

   config.set('system','isNotSet','true')
   with open('config.ini', 'wb') as configfile:
       config.write(configfile)

config_generator()
