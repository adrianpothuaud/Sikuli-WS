Sources Folder
==============

**Sources modules are intended for delivering sikuli advanced features and custom functions.**

Write new sources
-----------------

##### *Follow below instructions*

### Script template

**Use this template and write your code.**

    # -*- coding:utf-8 -*-

    """

        The '''srcsample''' module
        ===========================

        Use it as a template for new sources.

        Module content
        --------------

        - SAMPLEDICTIONNARY1
        - sample_function_1

        Module state
        ------------
        status: ? (date)
        test: run specs/specsample.sikuli
        unit tests:
            - run tests/srcsample_tests.sikuli
            - results: out/test_reports/srcsample_tests

        .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

    """

    from sikuli import *

    # import python modules here
    import datetime

    # import other source modules here
    import path_utils

    DEBUG = True # set to False to disable logs


    # define lists and dictionnaries here if necessary
    SAMPLEDICTIONNARY1 = {
        "sample1": "iamsample"
    }


    # define fonctions here
    def sample_function_1(arg1, arg2=None):
        """
        A sample fonction.

        Describe the fonction here...
        Describe parameters.
        Describe behavior.

        :param arg1: sample parameter
        :type arg1: str
        :param arg2: sample parameter, default: None
        :type arg2: list
        :return: A dictionary
        :rtype: dictionary

        """
        if DEBUG:
            print("this is a sample fonction")
        return {"sample": "this is useless"}



**Comment and document your code !**

**Create unit tests for any sources.**

**Optionaly create specs module for on-the-go testing this source.**

:sunglasses:
