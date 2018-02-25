
# coding: utf-8

# Imoport needed packages

# In[6]:


import csv


# Function that load data and re-shap it as list of [intent and question] 
# takes argument `fileName` wich is in our case is `NBB_intents.csv`

# In[11]:


def load_data(fileName):
    data_set = csv.reader(open(fileName), delimiter=',',quoting=csv.QUOTE_NONE,skipinitialspace=True)
    # creat new list for data after re-shaping
    main_dataset = []
    # read all questions samples 
    for row in data_set:
        curr_senten = row
        # new set ["intent",["cleaned question words"]]
        main_dataset.append([curr_senten[1],curr_senten[0]])

    return main_dataset

