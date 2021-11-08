from databasesearcher import OverallDataSearcher as oDS
from databasesearcher import CityDataSearcher as cDS

from IPython.display import display
import pandas as pd
import time

pd.set_option('display.max_rows', None)

def main():
    
    ods_vs_cds = input("""Please choose one of the following options by inputting the corresponding number:
        1. View Job Counts for Company Overall
        2. View Job Counts for Company in City \n \n"""
    )
    
    if ods_vs_cds == '1':
        main_instance_oDS = oDS()

        selection = input("""
            Please choose one of the following options by inputting a number:
            1. Company Name Match
            2. Job Title Keyword Match
            3. Job Title Exact Match \n \n
            """
        )

        run_again = 'Yes'
        
        if selection == '1':
            while run_again == 'Yes':
                company_name = input('Please choose a company: ')
                company_table_final = main_instance_oDS.find_company(company_name).sort_values(by='Job Count', ascending=False)
                display(company_table_final)

                time.sleep(5)
                run_again = input('Would you like to choose another company? (Yes or No): ')
            print('Task ended.')

        elif selection == "2":
            while run_again == 'Yes':
                keyword = input('Please choose a keyword: ')
                keyword_table_final = main_instance_oDS.find_job_keyword(keyword).sort_values(by='Job Count', ascending=False)
                display(keyword_table_final)

                time.sleep(5)
                run_again = input('Would you like to choose another keyword? (Yes or No): ')
            print('Task ended.')

        elif selection == "3":
            while run_again == 'Yes':
                job_title = input('Please choose a job title: ')
                job_match_table_final = main_instance_oDS.find_exact_job_title(job_title).sort_values(by='Job Count', ascending=False)
                display(job_match_table_final)

                time.sleep(5)
                run_again = input('Would you like to choose another job title? (Yes or No): ')
            print('Task ended.')

        else:
            raise NameError('The input did not match any of the given options.')

    elif ods_vs_cds == '2':
        print('First, please choose a location: ')
        main_instance_cDS = cDS()

        selection = input("""
            Please choose one of the following options by inputting a number:
            1. Company Name Match
            2. Job Title Keyword Match
            3. Job Title Exact Match \n \n
            """
        )

        run_again = 'Yes'

        if selection == "1":
            while run_again == 'Yes':
                company_name = input('Please choose a company:')
                company_table_final = main_instance_cDS.find_city_company(company_name).sort_values(by='Job Count', ascending=False)
                display(company_table_final)

                time.sleep(5)
                run_again = input('Would you like to choose another company? (Yes or No): ')
            print('Task ended.')

        elif selection == "2":
            while run_again == 'Yes':
                keyword = input('Please choose a keyword:')
                keyword_table_final = main_instance_cDS.find_city_job_keyword(keyword).sort_values(by='Job Count', ascending=False)
                display(keyword_table_final)

                time.sleep(5)
                run_again = input('Would you like to choose another keyword? (Yes or No): ')
            print('Task ended.')

        elif selection == "3":
            while run_again == 'Yes':
                job_title = input('Please choose a job title: ')
                job_match_table_final = main_instance_cDS.find_city_exact_job_title(job_title).sort_values(by='Job Count', ascending=False)
                display(job_match_table_final)

                time.sleep(5)
                run_again = input('Would you like to choose another job title? (Yes or No): ')
            print('Task ended.')

        else:
            raise NameError('The input did not match any of the given options.')

    else:
        raise NameError('The input did not match any of the given options.')

if __name__ == '__main__':
    main()