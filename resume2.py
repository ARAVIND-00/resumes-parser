
import streamlit as st
import os
import pandas as pd

import nltk

import spacy
import en_core_web_sm
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')
# nltk.download('maxent_ne_chunker')
# nltk.download('wordnet')
# nltk.download('brown')
# nltk.download('stopwords')
import resume_parser

from resume_parser import resumeparse
from pyresparser import ResumeParser
def file_selector(folder_path='resumes'):
    filename=os.listdir(folder_path)
    selected_filename=st.selectbox('select a file',filename)
    return os.path.join(folder_path,selected_filename)
filename=file_selector()
if st.button("Process"):
    st.write("You selected `%s` " %filename)

    Skills_extraction=ResumeParser(filename).get_extracted_data()
    extract_for_YoE=resumeparse.read_file(filename)
    experience = resume_parser.get_experience()
    years_of_experience = experience['years']
    st.write(years_of_experience)

    st.write("Years of Experience-----",extract_for_YoE['total_exp'])

    Skills_extracted = []

    if Skills_extraction['skills'] is not None and len(Skills_extraction['skills']) > 0:
        for i in Skills_extraction['skills']:
            Skills_extracted.append(i)

    if Skills_extraction['designation'] is not None and len(Skills_extraction['designation']) > 0:
        for j in Skills_extraction['designation']:
            Skills_extracted.append(j)

    if Skills_extraction['experience'] is not None and len(Skills_extraction['experience']) > 0:
        for k in Skills_extraction['experience']:
            Skills_extracted.append(k)

    skills_reqd_DS=['machine learning','data mining','predictive modeling', 'statistical analysis', 'data visualization', 'natural language processing', 'big data', 'data warehousing', 'sql', 'python/r programming', 'deep learning', 'artificial intelligence', 'data analytics', 'a/b testing', 'feature engineering', 'etl processes', 'time series analysis', 'regression analysis', 'cluster analysis', 'decision trees','power bi']
    skills_reqd_HR=['ats','applicant tracking systems','job postings', 'sourcing','source' ,'interviewing skills', 'hiring process', 'job descriptions', 'talent acquisition', 'diversity and inclusion', 'background checks', 'onboarding','hr consulting' ,'recruiting','recruiter','shortlisting','interviewing','end to end recruitment','deadline','reporting','hire','walk-in drives','phone interviewing',' candidate management systems','decisionmaking','management','psychology','monitoring''cms','screening resumes','lateral']
    skills_reqd_sales=['sales', 'account management', 'client relationship management', 'sales forecasting', 'sales strategy', 'sales negotiations', 'pipeline management', 'territory management', 'customer acquisition', 'sales performance', 'sales reporting','website sales','cilents','metrics','inside sales','strategic content development','presales executives','cold calling','executive',' marketing','business development','crm','market research', 'website sales', 'inside sales','negotiations','customer service']

    Skills_extracted=[x.lower() for x in Skills_extracted]
    Skills_extracted=[num.strip(' ') for num in Skills_extracted]
    Skills_extracted=[num.strip(')') for num in Skills_extracted]
    Skills_extracted=[num.strip('(') for num in Skills_extracted]

    res={'skills_reqd_DataScientist':[],'skills_reqd_HR':[],'skills_reqd_sales':[]}
    for i in Skills_extracted:
        if i in skills_reqd_DS:
            res['skills_reqd_DataScientist'].append(str(i))
        if i in skills_reqd_HR:
            res['skills_reqd_HR'].append(str(i))
        if i in skills_reqd_sales:
            res['skills_reqd_sales'].append(str(i))  

    HR=0
    DS=0
    sales=0
    x=1
    b=""
    for i,j in res.items():    
        if x==1:
            DS=len(j)
        if x==2:
            HR=len(j)
        if x==3:
            sales=len(j)
        x+=1
    if (HR>DS and HR>sales):
        b="HR"    
    if (DS>HR and DS>sales):
        b="DataScientist"    
    if (sales>HR and sales>DS):
        b="Sales"

    sal_data=pd.read_csv(r"Salary Dataset.csv")
    sal_data.info()

    sal_data=pd.DataFrame(sal_data)

    def final(a,b):

        while True :
            if a<=2 and b=="DataScientist":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "0-2")]
                st.write(color_and_shape)

                break
            if a<=4 and b=="DataScientist":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "3-4")]
                st.write(color_and_shape)
                break
            if a<=10 and b=="DataScientist":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "5-10")]
                st.write(color_and_shape)
                break
            if a>=11 and b=="DataScientist":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "10+")]
                st.write(color_and_shape)
                break
            if a<=2 and b=="HR":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "0-2")]
                st.write(color_and_shape)
                break
            if a<=4 and b=="HR":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "3-4")]
                st.write(color_and_shape)
                break
            if a<=10 and b=="HR":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "5-10")]
                st.write(color_and_shape)
                break
            if a>=11 and b=="HR":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "10+")]
                st.write(color_and_shape)
                break

            if a<=2 and b=="Sales":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "Sales") & (sal_data['YoE'] == "0-2")]
                st.write(color_and_shape)
                break
            if a<=4 and b=="Sales":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "Sales") & (sal_data['YoE'] == "3-4")]
                st.write(color_and_shape)
                break
            if a<=10 and b=="Sales":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "Sales") & (sal_data['YoE'] == "5-10")]
                st.write(color_and_shape)
                break
            if a>=11 and b=="Sales":
                color_and_shape = sal_data.loc[(sal_data['Job Role'] == "Sales") & (sal_data['YoE'] == "10+")]
                st.write(color_and_shape)
                break

    #OUTPUT
    final(extract_for_YoE['total_exp'],b)

