from getdata import get_data
from bs4 import BeautifulSoup
import requests
import pandas as pd
from IPython.display import display
from tqdm import tqdm

def parse_city_data():
    html = get_data()

    html_bs4 = BeautifulSoup(html, features="lxml")

    url_list = []
    company_names = []

    for url in html_bs4.find_all(target='_blank', rel=None, href=True):
        url_list.append(url['href'])
        company_names.append(url.text)
        
    company_id_dict = {}

    for url in url_list:
        company_name = url.split('/')[2]
        company_id = url.split('/')[3][:-4]
        company_id_dict[company_name] = company_id

    from geturl import city_final_name

    i = 0
    for company in company_id_dict:
        url_list[i] = 'https://www.myvisajobs.com/H1B-Visa/Search.aspx?CI=' + company_id_dict[company] + '&WC=' + city_final_name
        i += 1
        
    city_jobs_df = pd.DataFrame(
        columns=['Company', 'Position', 'Job Count']
    )

    print('Parsing Data...')

    i = -1
    for url in tqdm(url_list):
        request = requests.get(url).text
        company_html = BeautifulSoup(request, features='lxml')

        i += 1
         
        for company in company_html.find_all('table', class_='tbl'):

            var_company_name = company_names[i]
            var_city_job_list = []
            var_city_job_count = []

            try:
                
                a_tags = company.find_all('div', id='divTitle')[1].find_all('a')
                
                for a in a_tags:
                    var_city_job_list.append(a['title'])
                     
                for a_tag in company.find_all('div', id='divTitle')[1].find_all('a'):
                    var_city_job_count.append(a_tag.next_sibling)

            except: #need to make more specific
                pass

            sorted_var_city_job_count = [x for x in var_city_job_count if x != None]
            final_var_city_job_count = [int(x.strip('(').strip(')')) for x in sorted_var_city_job_count]

            if var_city_job_list != []:
                j = 0
                var_final_append_list = []

                for index in range(len(var_city_job_list)):
                    var_final_append_list = [var_company_name, var_city_job_list[j], final_var_city_job_count[j]]
                    city_jobs_df.loc[len(city_jobs_df)] = var_final_append_list

                    j +=1

    return city_jobs_df

if __name__ == '__main__':
    parse_city_data()