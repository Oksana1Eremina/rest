import yaml
from zeep import Client, Settings


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    wsdl = data('wsdl')

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)

if __name__ == '__main__':
    print(client.service.checkText('молако'))