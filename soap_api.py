import yaml
import logging
from zeep import Client, Settings

try:
    with open('config.yaml', encoding='utf-8') as f:
        logging.info('trying to open file config.yaml')
        data = yaml.safe_load(f)
        wsdl = data('wsdl')
    logging.info('file config.yaml successfully opened')
except Exception(FileNotFoundError) as e:
    logging.exception('open file config.yaml failed')

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_text(text: str) -> list[str]:
    try:
        logging.info('try to send rest request')
        resp = client.service.checkText(text)
        return resp[0]['s']
    except Exception as ex:
        logging.exception('exception when try to send rest request')
