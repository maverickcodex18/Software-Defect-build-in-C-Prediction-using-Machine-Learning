import numpy as np
import streamlit as st
import joblib as jb


model=jb.load('model.pkl')


#creating function for prediction

def prediction(input):
    inputNp=np.asarray(input).reshape(1,-1)
    pred=model.predict(inputNp)
    if(pred[0]==False):
        return "No Defects Found"
    else:
        return "Defects Found"



def main():

    #title
    st.title("Defect Detection in C Softwares")

    #getting input from user
    linesOfCode=st.text_input("Enter the number of lines of code in Module")
    cyclomaticComplexity=st.text_input("Enter the cyclomatic complexity of Module")
    noEdges=st.text_input("Enter the number of edges in control flow graph")
    noNodes=st.text_input("Enter the number of nodes in control flow graph")
    noFunctions=st.text_input("Enter the number of functions in Module")
    noVariables=st.text_input("Enter the number of variables in Module")
    noLoops=st.text_input("Enter the number of loops in Module")
    noDecisionPoints=st.text_input("Enter the number of decision points in Module")
    noInputVariables=st.text_input("Enter the number of input variables in Module")
    noExternalDependencies=st.text_input("Enter the number of external dependencies in Module")
    noBugs=st.text_input("Enter the number of bugs found in Module")
    noTests=st.text_input("Enter the number of tests conducted in Module")
    LOCLogic=st.text_input("Enter the number of lines of code in logic")
    LOCComments=st.text_input("Enter the number of lines of code in comments")
    LOCBlank=st.text_input("Enter the number of blank lines")
    LOCCodeComments=st.text_input("Enter the number of lines of code in code and comments combined")
    noUniqOperators=st.text_input("Enter the number of unique operators in Module")
    noUniqOperands=st.text_input("Enter the number of unique operands in Module")
    totalOperations=st.text_input("Enter the total number of operations in Module")
    totalOperands=st.text_input("Enter the total number of operands in Module")
    branchCounts=st.text_input("Enter the branch counts/decision points in Module")

    #button for prediction
    modelPrediction=''

    if(st.button("Predict")):
        modelPrediction=prediction([linesOfCode,cyclomaticComplexity,noEdges,noNodes,noFunctions,noVariables,noLoops,noDecisionPoints,noInputVariables,noExternalDependencies,noBugs,noTests,LOCLogic,LOCComments,LOCBlank,LOCCodeComments,noUniqOperators,noUniqOperands,totalOperations,totalOperands,branchCounts])

    st.success(modelPrediction)

if __name__=='__main__':
    main()
