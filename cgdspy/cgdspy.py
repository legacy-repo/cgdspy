# -*- coding: utf-8 -*-
"""
    cgdspy.cgdspy
    ~~~~~~~~~~~~~

    Python based API for accessing the Cancer Genomics Data Server (CGDS).

    :copyright: © 2019 by the Choppy Team.
    :license: AGPLv3+, see LICENSE for more details.
"""

import requests
import json
import pandas as pd
import io

def join_str(string):
    if isinstance(string, str):
        return string
    else:
        return ','.join(string)

class CGDSPY:
    def __init__(self, url, token = None, verbose = False, ploterrormsg = ''):
        """CGDSPY Initializer

        :url: data port url
        :token: An optional ’Authorization: Bearer’ token to connect to 
                 cBioPortal instances that require authentication (default NULL)
        :verbose: A boolean variable specifying verbose output (default FALSE)
        :ploterrormsg: An optional message to display in plots if an error occurs (default ”)
        """
        self.url = url
        self.token = token
        self.verbose = verbose
        self.ploterrormsg = ploterrormsg

    def get_cancer_studies(self):
        """Get all cancer studies from CGDS.
        """
        url = (self.url +  "webservice.do?cmd=getCancerStudies&")
        print(url)
        url_data = requests.get(url).content
        raw_data = pd.read_table(io.StringIO(url_data.decode('utf-8')))
        return(raw_data)

    def get_case_lists(self, cancer_study):
        """Get all case lists with `cancer_study` from CGDS.

        :cancer_study: from GetCancerStudies
        """
        url = (self.url +  "webservice.do?cmd=getCaseLists&cancer_study_id=" + cancer_study)
        url_data = requests.get(url).content
        raw_data = pd.read_table(io.StringIO(url_data.decode('utf-8')))
        return(raw_data)

    def get_genetic_profiles(self, cancer_study):
        """Get all genetic profiles with `cancer_study` from CGDS.

        :cancer_study: from GetCancerStudies
        """
        url = (self.url +  "webservice.do?cmd=getGeneticProfiles&cancer_study_id=" + cancer_study)
        url_data = requests.get(url).content
        raw_data = pd.read_table(io.StringIO(url_data.decode('utf-8')))
        return(raw_data)
    
    def get_mutation_data(self, cancer_study, case_list, genetic_profile, gene_list):
        """Get mutation data with `case_list, genetic_profile and gene_list` from CGDS.

        :case_list: from GetCaseLists
        :genetic_profile: from GetGeneticProfiles
        :gene_list: from user settings
        """
        url = (self.url +  "webservice.do?cmd=getMutationData" + cancer_study +
         "&case_set_id=" + case_list + "&genetic_profile_id=" + genetic_profile + 
         "&gene_list=" + join_str(gene_list))
        url_data = requests.get(url).content
        raw_data = pd.read_table(io.StringIO(url_data.decode('utf-8')))
        return(raw_data)
    
    def get_profile_data(self, gene_list, genetic_profiles, case_list, cases = '', case_ids_key = ''):
        """Get profile data from CGDS.

        :gene_list: from user settings
        :genetic_profiles: from GetGeneticProfiles 
        :case_list:
        :cases: A vector of case IDs
        :case_ids_key: Only used by web portal
        """
        url = (self.url + "webservice.do?cmd=getProfileData" + 
              "&gene_list=" + join_str(gene_list) + "&genetic_profile_id=" + 
              join_str(genetic_profiles) + "&id_type=" + 'gene_symbol'
              )
        print(url)
        if len(cases) > 0:
            url = url + "&case_list=" + join_str(cases)
        elif (case_ids_key != ''):
            url = url + "&case_ids_key=" + case_ids_key
        else:
            url = url + "&case_set_id=" + case_list
        print(url)
        url_data = requests.get(url).content
        
        if isinstance(genetic_profiles, str):
            raw_data = pd.read_table(io.StringIO(url_data.decode('utf-8')), skiprows = 2)
            return(raw_data)  
        else:
            raw_data = pd.read_table(io.StringIO(url_data.decode('utf-8')))
            return(raw_data)  
    
    def get_clinical_data(self, case_list, cases='', case_ids_key=''):
        """Get clinical data from CGDS.
        """
        url = self.url + "webservice.do?cmd=getClinicalData"

        if len(cases) > 0:
            url = url + "&case_list=" + join_str(cases) 
        elif case_ids_key != '':
            url = url + "&case_ids_key=" + case_ids_key 
        else:
            url = url + "&case_set_id=" + case_list

        url_data = requests.get(url).content
        raw_data = pd.read_table(io.StringIO(url_data.decode('utf-8')))
        return(raw_data)
        
