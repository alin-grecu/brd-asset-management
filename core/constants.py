from datetime import date
import os


class Email:
    CHARSET = "UTF-8"
    AWS_REGION = os.getenv('REGION')
    SENDER = os.getenv('SENDER')
    RECIPIENT = os.getenv('RECIPIENT')
    SUBJECT = 'Raport BRD Asset Management' + ' ' + str(date.today())


class Graph:
    PLOT_MAX_PIXELS = 150  # Max plot height you want. This will be the height of max(data).


class Simfonia:
    NAME = 'simfonia'
    UNITS = float(os.getenv('UNITS_SIMFONIA'))
    INVESTED = int(os.getenv('INVESTED_SIMFONIA'))
    URL = 'https://brdam.ro/assets/json/istorics.json'
    START_COLOR = '#555454'
    END_COLOR = '#17a2b8'


class Diverso:
    NAME = 'diverso'
    UNITS = float(os.getenv('UNITS_DIVERSO'))
    INVESTED = int(os.getenv('INVESTED_DIVERSO'))
    URL = 'https://brdam.ro/assets/json/istoricd.json'
    START_COLOR = '#977849'
    END_COLOR = '#eca30f'

class ActiuniA:
    NAME = 'actiunia'
    UNITS = float(os.getenv('UNITS_ACTIUNIA'))
    INVESTED = int(os.getenv('INVESTED_ACTIUNIA'))
    URL = 'https://brdam.ro/assets/json/istorics.json'
    START_COLOR = '#067d67'
    END_COLOR = '#0fd9b4'

class Obligatiuni:
    NAME = 'obligatiuni'
    UNITS = float(os.getenv('UNITS_OBLIGATIUNI'))
    INVESTED = int(os.getenv('INVESTED_OBLIGATIUNI'))
    URL = 'https://brdam.ro/assets/json/istorics.json'
    START_COLOR = '#82160e'
    END_COLOR = '#d91b0d'

class Total:
    NAME = 'total'
    START_COLOR = '#538868'
    END_COLOR = '#67b020'
