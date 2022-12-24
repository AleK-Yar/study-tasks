from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections
from dotenv import load_dotenv
import os
import argparse
from pathlib import Path


def load_env(path):
    if not path:
        path = Path('.') / '.env'
    load_dotenv(dotenv_path=path)
    return os.getenv('WINE_FILE_PATH')


def get_company_age() -> int:
    foundation_year = 1920
    return datetime.date.today().year - foundation_year


def get_age_ending(year: int) -> str:
    year = str(year)
    if year[-1] == '1' and year[-2:] != '11':
        return 'год'
    elif year[-1] in ('2', '3', '4') and year[-2:] not in ('12', '13', '14'):
        return 'года'
    return 'лет'


def convert_excel_to_dictionary(exel_file: str) -> dict:
    excel_data_df = pandas.read_excel(exel_file, na_values=None, keep_default_na=False)
    wines = excel_data_df.to_dict(orient='records')
    wines_categorized = collections.defaultdict(list)
    [wines_categorized[wine['Категория']].append(wine) for wine in wines]
    return wines_categorized


def main(patch_to_file=None, env_patch=None):
    try:
        if not patch_to_file:
            patch_to_file = load_env(env_patch)
        wines_categorized = convert_excel_to_dictionary(patch_to_file)
        company_age = get_company_age()
        years_age = get_age_ending(company_age)

        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('template.html')
        rendered_page = template.render(
            company_age=company_age,
            years_age=years_age,
            wines_categorized=wines_categorized
        )

        with open('index.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)
        server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
        server.serve_forever()
    except (FileNotFoundError, ValueError):
        print('Ошибка доступа к файлу, проверьте правильность указания пути!')
    except KeyError as err:
        print('Проверьте правильность excel файла:', err)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Adding a product to the site from an excel file')
    parser.add_argument('-p', '--path_to_file', help='Path to excel file')
    parser.add_argument('-ep', '--env_path', help='Path to .env file')
    args = parser.parse_args()
    main(args.path_to_file, args.env_path)

