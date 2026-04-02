import streamlit as st
import pandas as pd
import numpy as np
import pickle,gzip
with gzip.open('loan_approval.pkl','rb') as f:
       model=pickle.load(f)
st.title("Check your Loan Approval Possibility")
st.info("💡 **Tip:** Check your eligibility here first. This tool provides a prediction without performing a 'Hard Inquiry' on your CIBIL record.")
st.caption("As this model is trained on employees data, " \
"it is better to use only who have proper income OR past credit history.")
st.divider()
col1,col2=st.columns(2)
with col1:
    age=st.number_input("What is your age?",min_value=19.0,max_value=100.0)
    gender=st.selectbox("What is your gender?",options=['Male','Female'])
    education=st.selectbox("What is your Highest education qualification?",
                        options=['High School','Associate','Graduation','Master','Doctorate'])
    ownership=st.selectbox("What is your ownership status with your home?",
                       options=['Own','Rent','Mortgage','Other'])
    purpose_text=st.selectbox("What is the intention of taking loan?",
                          options=['Debt_Repayment','Education','Home','Medical','Personal','Venture'])
    defaults=st.selectbox("If any loan taken previously, did you failed to pay on time?",options=['Yes','No'])
with col2:
    income=st.number_input("Whats your annual income in Indian Rupees?",min_value=1.0)
    experiance=st.number_input("No.Of years from your first job upto now?")
    def max_amount(income):
        if income<100000:
            if purpose_text=="Education":
                return 1000000
            if purpose_text=="Personal":
                return 10000
        else:
            return income*5
    amount=st.number_input("How much you want as loan in rupees?",max_value=max_amount(income))

    intrest=st.number_input("At what percent of intrest you are comfirtable to take loan?")
    loanpercentIncome=(amount/income)*100
    cibilScore=st.number_input("What is your cibil score?",min_value=300,max_value=900)
    creditAge=st.number_input("No of years from your first loan?(If loans not taken, remain it as 0)",min_value=0.0)

st.divider()
mortgage=own=rent=other=0
if ownership=='Own':
    own=1
elif ownership=='Rent':
    rent=1
if ownership=='Mortgage':
    mortgage=1
if ownership=='Other':
    other=1 
       

edu=debt=home=medical=personal=venture=0

if purpose_text=='Debt_Repayment':
    debt=1
elif purpose_text=='Education':
    edu=1
elif purpose_text=='Home':
    home=1
elif purpose_text=='Medical':
    medical=1
elif purpose_text=='Personal':
    personal=1
else:
    venture=1
gender_map={"Male":0,"Female":1}
education_map={"High School":0,"Associate":1,"Graduation":2,"Master":3,"Doctorate":4}
default_map={"Yes":1,"No":0}
inputs=np.array([[age,gender_map[gender],education_map[education]
,income/90,experiance,amount/90,intrest,loanpercentIncome,creditAge,cibilScore,default_map[defaults],
         mortgage,other,own,rent,debt,edu,home,medical,personal,venture]])


pred=model.predict(inputs)

if st.button("Check",type='secondary'):
    if cibilScore<600 or intrest<8:
        st.error('Sorry at present we cant provide you a loan!')
    elif pred[0]==1:
        st.success("Yahoo! You are eligible for this loan")
    else:
        st.error("Sorry at present we cant provide you a loan!")
