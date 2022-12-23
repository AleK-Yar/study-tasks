from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections


def calculation_age_company() -> int:
    foundation_year = 1920
    return datetime.date.today().year - foundation_year


def substitution_cases_term_age_company(year: int) -> str:
    year = str(year)
    if year[-1] == '1' and year[-2:] != '11':
        return 'год'
    elif year[-1] in ('2', '3', '4') and year[-2:] not in ('12', '13', '14'):
        return 'года'
    return 'лет'


def get_data_excel(exel_file: str) -> dict:
    excel_data_df = pandas.read_excel(exel_file, na_values=None, keep_default_na=False)
    list_dict = excel_data_df.to_dict(orient='records')
    wines_dict = collections.defaultdict(list)
    [wines_dict[d['Категория']].append(d) for d in list_dict]
    return wines_dict


patch_to_file_wines = 'wine3.xlsx'

wines_dict = get_data_excel(patch_to_file_wines)
age_company = calculation_age_company()
years_age = substitution_cases_term_age_company(age_company)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')
rendered_page = template.render(age_company=age_company, years_age=years_age, wines_dict=wines_dict)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
