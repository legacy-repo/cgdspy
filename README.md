# choppy-data-portal-cgdspy 
## table of contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#Usage)
- [Configuration Attributes](#configurationAttributes)

## Introduction

cgdspy based API for accessing the Cancer Genomics Data Server (CGDS). It's based on [cgdsr](https://github.com/cBioPortal/cgdsr). Queries the CGDS API and returns available cancer studies. Input is a CGDS object and output is a data.matrix with information regarding the different cancer studies.

## Installation

### Stable release
To install cgdspy, run this command in your terminal:
‘’‘python
pip install cgdspy
'''
This is the preferred method to install cgdspy, as it will always install the most recent stable release.

If you don’t have pip installed, this Python installation guide can guide you through the process.

### From sources
The sources for cgdspy can be downloaded from the Github repo.

You can either clone the public repository:
'''python
$ git clone git://github.com/go-choppy/cgdspy
'''
Or download the tarball:
'''py
$ curl  -OL https://github.com/go-choppy/cgdspy/tarball/master
'''
Once you have a copy of the source, you can install it with:
'''python
$ python setup.py install
'''

## Usage

To instantiate a new cgds:

```python
mycgds = CGDSPY("http://www.cbioportal.org/", token = None, verbose = False, ploterrormsg = '')
mycancerstudy = mycgds.get_cancer_studies()
mycancerstudy = mycancerstudy.iat[1, 0]
mycaselist = mycgds.get_case_lists(mycancerstudy)
mycaselist = mycaselist.iat[0, 0]
mygeneticprofile = mycgds.get_genetic_profiles(mycancerstudy)
mygeneticprofile = mygeneticprofile.iat[0, 0]


# Get data slices for a specified list of genes, genetic profile and case list
gene_list = 'HMGA2'
mycgds.get_profile_data(gene_list, mygeneticprofile, mycaselist)

gene_list = ('BRCA1','BRCA2')
mycgds.get_profile_data(gene_list, mygeneticprofile, mycaselist)

gene_list = 'HMGA2'
mygeneticprofile =  mycgds.get_genetic_profiles(mycancerstudy)
mygeneticprofile = mygeneticprofile.ix[[0, 1], [0]]
mygeneticprofile = mygeneticprofile['genetic_profile_id']
mycgds.get_profile_data(gene_list, mygeneticprofile, mycaselist)

#
mycgds.GetClinicalData(mycaselist)
```

## Configuration Attributes

### backgrounds

## Contact

Jun Shang
shangjunv@163.com

Your feedbacks are welcome. If you're struggling using the librairy, the best way to ask questions is to use the Github issues so that they are shared with everybody.
