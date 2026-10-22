#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->

# This issue I would like to adress is how artifical intelligence is affecting job opportunities for recent college grads. AI is becoming more common in every industry and is changing the way companies operate. Some tasks can now be completed faster using AI, which would reduce the need for some entry level roles while creating demand for new skills. The topic is important becuase recent college grads are already entering a competitive job marker. Understanding how AI is changing employment opportunities could help students make better decisions about their careers and identify skills they need to develop before graduattion. 

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->

# 1. How have unemployment rates among recent college grads changed as AI has become more common?
# 2. Which career fields have highest levels of AI use, and how are employment opportunities in that field?
# 3. Are entry-level job opportunities decreasing in occupations with higher AI use?
# 4. What tech and AI-related skills are employers looking for?

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->

# I would use line graphs, bar charts, and scatter plots to compare unployment trends, AI use, and job opportunities across diffrent career fields. I could also create a scatter plot comparing AI use with changes in the job opportunities for different occupations. Finally, a bar chart of commonly requested tech skills would help show what employers are looking for. The goal would be to identify patterns between AI adoption and employment trends. 

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->

# https://www.newyorkfed.org/research/college-labor-market#--:explore:unemployment
# This datasset provides information about unemployment, underemployment, and wages for recent college grads. I would use it examine how unemployment has changed over time. 
# 
# https://huggingface.co/datasets/Anthropic/EconomicIndex
# This dataset provides information about how AI is being used for different occupation tasks. It also includes occupational AI-exposure data.  I would use it to idenity which career fields have higher levels of observed AI use. 
# 
# https://www.onetcenter.org/database.html
# I will use O*Net to identify the skills and technologies required for different occupations. I will connect this information with the Anthropic dataset to compare the skills associated with jobs that have higher AI use. This will help me understand which technical skills may be useful for recent college grads. 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# My apporach is to compare unemployment trends among recent college grads with AI adoption across different fields. I want to see if industries with higher AI use are experiecing changes in employment opportunities and what skills employers are looking for. I will use 3 datasets mentioned above. I plan to use python and sql to clean and organize data. I will connect the datasset using occupation codes and create visualization in tableau. My goal is to identify patterns that could help recent college grads understand how AI is chaning the job market and which skills they should focus on developing. However, a relationship between AI adoption and unemployment does not mean AI is directly causing unemployment. 

# In[1]:


# Start your code here


# ## Exploratory Data Analysis 
# 

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[1]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

