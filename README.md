# cgdspy

import CGDSR
mycgds = CGDSR("http://www.cbioportal.org/", token = None, verbose = False, ploterrormsg = '')
mycancerstudy = mycgds.get_cancer_studies()
mycancerstudy = mycancerstudy.iat[1, 0]
mycaselist = mycgds.get_case_lists(mycancerstudy)
mycaselist = mycaselist.iat[0, 0]
mygeneticprofile = mycgds.get_genetic_profiles(mycancerstudy)
mygeneticprofile = mygeneticprofile.iat[0, 0]


### Get data slices for a specified list of genes, genetic profile and case list
gene_list = 'HMGA2'
mycgds.get_profile_data(gene_list, mygeneticprofile, mycaselist)

gene_list = ('BRCA1','BRCA2')
mycgds.get_profile_data(gene_list, mygeneticprofile, mycaselist)

gene_list = 'HMGA2'
mygeneticprofile =  mycgds.get_genetic_profiles(mycancerstudy)
mygeneticprofile = mygeneticprofile.ix[[0, 1], [0]]
mygeneticprofile = mygeneticprofile['genetic_profile_id']
mycgds.get_profile_data(gene_list, mygeneticprofile, mycaselist)

mycgds.GetClinicalData(mycaselist)
