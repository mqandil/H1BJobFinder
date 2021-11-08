import requests
from getdata import get_data
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

def parse_all_data():
    html = get_data()

    html_bs4 = BeautifulSoup(html, features="lxml")

    url_list = []
    company_names = []

    for url in html_bs4.find_all(target='_blank', rel=None, href=True):
        url_list.append(url['href'])
        company_names.append(url.text)
        
    i = 0
    for url in url_list:
        url_list[i] = 'https://www.myvisajobs.com' + url
        i += 1
        
    company_jobs_list = []

    print('Parsing Data...')
    
    for url in tqdm(url_list):
        request = requests.get(url).text
        company_html = BeautifulSoup(request, features='lxml')

        for company in company_html.find_all('table', width='100%'):
            if company.select('tr')[21].find_all('a') != []:
                company_jobs_list.append(company.select('tr')[21].find_all('a'))
            elif company.select('tr')[20].find_all('a') != []:
                company_jobs_list.append(company.select('tr')[20].find_all('a'))
            else:
                pass

    company_jobs_list = [x for x in company_jobs_list if x != []]

    print('Appending Data...')

    jobs_df = pd.DataFrame(
       columns=['Company', 'Position', 'Job Count'] 
    )

    i = 0
    for job_list in company_jobs_list:

        for job in job_list:
            test = job.text.split('(')
            position = test[0]
            job_count = test[-1][:-1]

            var_job_list = []
            var_job_list.append(company_names[i])
            var_job_list.append(position)
            var_job_list.append(job_count)

            jobs_df.loc[len(jobs_df)] = var_job_list

        i += 1

    jobs_df['Job Count'] = jobs_df['Job Count'].astype(int)

    return jobs_df

if __name__ == '__main__':
    parse_all_data()