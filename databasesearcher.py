from parsealldata import parse_all_data
from parsecitydata import parse_city_data
import pandas as pd


class OverallDataSearcher():
    def __init__(self):
        jobs_available = parse_all_data()
        self.jobs_available = jobs_available

    def find_job_keyword(self, keyword):
        partial_job_match = pd.DataFrame(self.jobs_available.loc[self.jobs_available['Position'].str.contains(keyword)])
        return partial_job_match

    def find_company(self, company_name):
        company_match = pd.DataFrame(self.jobs_available.loc[self.jobs_available['Company'] == company_name])
        return company_match

    def find_exact_job_title(self, title):
        exact_job_match = pd.DataFrame(self.jobs_available.loc[self.jobs_available['Position'] == title])
        return exact_job_match


class CityDataSearcher():
    def __init__(self):
        city_jobs_available = parse_city_data()
        self.city_jobs_available = city_jobs_available
    
    def find_city_job_keyword(self, keyword):
        city_partial_job_match = pd.DataFrame(self.city_jobs_available.loc[self.city_jobs_available['Position'].str.contains(keyword)])
        return city_partial_job_match

    def find_city_company(self, company_name):
        city_company_match = pd.DataFrame(self.city_jobs_available.loc[self.city_jobs_available['Company'] == company_name])
        return city_company_match

    def find_city_exact_job_title(self, title):
        city_exact_job_match = pd.DataFrame(self.city_jobs_available.loc[self.city_jobs_available['Position'] == title])
        return city_exact_job_match


if __name__ == '__main__':
    test = OverallDataSearcher()
    test.find_job_keyword('Engineer')
    test.find_company('Atos Syntel')
    test.find_exact_job_title('Clinical Fellow')