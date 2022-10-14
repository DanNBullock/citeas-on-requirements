# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:50:39 2022

@author: dbullock
"""

def findRequirementsTXTFile(repoDir=''):
    """
    Finds the requirements.txt file from a repository into a list which
    can be iterated through with _queryPackage_.
    
    Function intended to encapsulate adapaive search capabilities for this
    file.

    Parameters
    ----------
    repoDir : string, optional
        Location of directory, relative to current working directory, in which
        to search for the target requirements.txt file. Examples:
            
            - '' : will search the current working directory
            - os.system('git rev-parse --show-toplevel') : would search in the
            top directory of the 'current' (e.g. on current working directory
            path) repository.  Probably.
            - 'test' : would search the test directory for (e.g. when running
            unit tests)
            The default is ''.
    
    Returns
    -------
    requirementsTXTpath: string
        Path to the requirements.txt file.
        
    """
    
    
    import os
    #set target file name
    targetFileName='requirements.txt'
    
    #TODO enhance this functionality to make it more adaptive
    #append the dirstem, if necessary
    requirementsTXTpath=os.path.join(repoDir,targetFileName)
    
    
    return requirementsTXTpath

def parseRequirementsTXT(requirementsTXTpath):
    """
    Parses the requirements.txt file into a list which can be iterated through
    with _queryPackage_.

    Parameters
    ----------
    requirementsTXTpath : string
        Location of targetrequirements.txt file.

    Returns
    -------
    packagesList : list of strings
        A list of strings, each of which corresponds to a package enumerated
        in an appropriately formatted 
        [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
        file.

    """

    
    #open requirements.txt file
    with open(requirementsTXTpath) as f:
        lines = f.readlines()
    
    #iterate across lines and remove newline character
    packagesList=[iLines.replace('\n','') for iLines in lines]
    
    return packagesList

def queryPackage(packageString,citationOption=2,emailTag='githubActionTest@DanNBullock.com'):
    """
    Performs a query using the [citeas api](https://citeas.org/api), to find a
    citation for the input string, which is presumed to correspond to a
    software package.
    
    WARNING: citeas is not perfect, and will often return mangled citations.
    In cases where this software returns an undesired output, it is
    recommended that the user performs a sanity check manually with the citeas
    web interface.

    Parameters
    ----------
    packageString : string; putative software package
        The string that will be submitted to the citeas API in order to
        obtain a citation
    citationOption : int, 0 to 5
        Index of the desired citation format from the following list:
        ['APS','Harvard','Nature','MLA','Chicago','Vancouver']
        Default is currently 2, for 'Nature'.
    emailTag: string; putative email adress
        Email tag to append to the end of the API request.  For the purposes
        of usage tracking with the citeas organization.  Current default is
        'githubActionTest@DanNBullock.com', as this is presumed to be
        more informative than an actual email adress given their stated goals.
        

    Returns
    -------
    citationOut: string
        An appropriately formatted citation corresponding to the input 
        software package string and associated citation option choice.

    """
    import requests
    import json
    import warnings
    import time
    
    #set url stem for query
    apiStem='https://api.citeas.org/product/'
    
    #debug
    print('\n ' + packageString + '\n')
    
    #form the query URL
    queryURL=''.join([apiStem,packageString,'?','email=',emailTag])
    
    #use requests to perform the query
    outAPIresponse=requests.get(queryURL)
    
    #convert output string to json format
    outResponseJson=json.loads(outAPIresponse.text)
    
    #index in to the response json dictionary and extract the desired citation
    citationOut=outResponseJson['citations'][citationOption]['citation']
    
    #use the behavior of the APS citation to check for mangled authorship
    if outResponseJson['citations'][0]['citation'][0:6]=='(n.d.)':
        warnings.warn('Authorship record for requested package  ' + packageString +'  appears to be mangled')
        
    #add a wait, to ensure that we don't get rate limited by the API    
    time.sleep(5)
    
    return citationOut
    
def requirementsToCitationList(requirementsTXTpath, kwargs={}):
    """
    Iterates through the requirements.txt entries and generates citations
    for each item.

    Parameters
    ----------
    requirementsTXTpath : string
        Location of targetrequirements.txt file.
    kwargs : pass through variables for queryPackage
        e.g.: citationOption=2,emailTag='githubActionTest@DanNBullock.com'
        They don't need to be unpacked at this level.

    Returns
    -------
    citationList : list of strings
        A list of citations corresponding to the packages listed in the input
        requirementsTXTpath file.

    """
    
    #get the list of packages
    packagesList=parseRequirementsTXT(requirementsTXTpath)
    
    #iterate through them to get a citation for each
    citationList=[queryPackage(iPackage,**kwargs) for iPackage in packagesList]
    
    return citationList

def citationListTOmdOut(citationList,outFileName='ACKNOWLEDGMENTS.md'):
    """
    Takes input citationList (from requirementsToCitationList) and produces a
    markdown formatted bibliography output.

    Parameters
    ----------
    citationList : list of strings
        A list of citations, presumably from from requirementsToCitationList
    outFileName : string, optional
        The desired name of the output, markdown formatted citations. 
        The default is 'ACKNOWLEDGMENTS.md'.

    Returns
    -------
    None. Saves down output

    """
    from datetime import date
    #TODO develop and load up a boilerplate text block for citation page
    #in lieu of that, just have a header and generation date
    #headerTextBlock=<LOAD BOILERPLATE HERE>
    
    titleLine='# Cited software'
    
    #get todays date
    today = date.today()
    #generate dateString
    dateString=today.strftime("%m/%d/%y")
    
    #produce ALTERNATIVE header text block
    
    headerTextBlock='\n\n'.join([titleLine,'(Results generated on: ' + dateString+')'])
    
    #now join with list, maybe not appropriately formatted in case of Nature,
    #due to autodetect / numbering issue?
    outDocText='\n\n'.join([headerTextBlock,'\n\n'.join(citationList)])
    
    #save the output
    text_file = open(outFileName, "w")
    text_file.write(outDocText)
    text_file.close()
    
def inputToCitations(inputPath,kwargs={}):
    """
    Takes input citationList (from requirementsToCitationList) and produces a
    markdown formatted bibliography output.
    
    Future Note: future versions of this code will use this function to parse
    and handle different types of inputs, e.g. Dockerfile, pyproject-toml,
    or requirements.txt

    Parameters
    ----------
    inputPath : string
        Path to source dependancy record file
    kwargs : pass through variables for queryPackage and citationListTOmdOut
        Variables governing underlying function behaviors

    Returns
    -------
    None. Saves down output

    """
    
    #TODO create case statement here to detect and handle different types of
    #file inputs, e.g. Dockerfile, pyproject-toml, or requirements.txt
    
    #for now though...
    #assume it's a requirements.txt file and obtain the citationList
    citationList=requirementsToCitationList(inputPath, kwargs=kwargs)
    
    #generate md output file
    citationListTOmdOut(citationList,**kwargs)