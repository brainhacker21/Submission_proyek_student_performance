#!/usr/bin/env python
# coding: utf-8

# # Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

# - Nama: Auric
# - Email: stevenauric@gmail.com
# - Id Dicoding: auric_21

# ## Persiapan

# ### Menyiapkan library yang dibutuhkan

# In[5]:


# Library yang sering dipakai
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Library untuk fungsi database
from sqlalchemy import create_engine

# Library untuk modelling
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib


# ### Menyiapkan data yang akan digunakan

# In[7]:


df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv", delimiter=';')
df.head(5)


# ## Data Understanding

# # Employee Data
# 
# ### Marital status
# The marital status of the student. (Categorical)
# - 1 – single
# - 2 – married
# - 3 – widower
# - 4 – divorced
# - 5 – facto union
# - 6 – legally separated
# 
# ### Application mode
# The method of application used by the student. (Categorical)
# - 1 - 1st phase - general contingent
# - 2 - Ordinance No. 612/93
# - 5 - 1st phase - special contingent (Azores Island)
# - 7 - Holders of other higher courses
# - 10 - Ordinance No. 854-B/99
# - 15 - International student (bachelor)
# - 16 - 1st phase - special contingent (Madeira Island)
# - 17 - 2nd phase - general contingent
# - 18 - 3rd phase - general contingent
# - 26 - Ordinance No. 533-A/99, item b2) (Different Plan)
# - 27 - Ordinance No. 533-A/99, item b3 (Other Institution)
# - 39 - Over 23 years old
# - 42 - Transfer
# - 43 - Change of course
# - 44 - Technological specialization diploma holders
# - 51 - Change of institution/course
# - 53 - Short cycle diploma holders
# - 57 - Change of institution/course (International)
# 
# ### Application order
# The order in which the student applied. (Numerical)
# - Application order (between 0 - first choice; and 9 last choice)
# 
# ### Course
# The course taken by the student. (Categorical)
# - 33 - Biofuel Production Technologies
# - 171 - Animation and Multimedia Design
# - 8014 - Social Service (evening attendance)
# - 9003 - Agronomy
# - 9070 - Communication Design
# - 9085 - Veterinary Nursing
# - 9119 - Informatics Engineering
# - 9130 - Equinculture
# - 9147 - Management
# - 9238 - Social Service
# - 9254 - Tourism
# - 9500 - Nursing
# - 9556 - Oral Hygiene
# - 9670 - Advertising and Marketing Management
# - 9773 - Journalism and Communication
# - 9853 - Basic Education
# - 9991 - Management (evening attendance)
# 
# ### Daytime/evening attendance
# Whether the student attends classes during the day or in the evening. (Categorical)
# - 1 – daytime
# - 0 - evening
# 
# ### Previous qualification
# The qualification obtained by the student before enrolling in higher education. (Categorical)
# - 1 - Secondary education
# - 2 - Higher education - bachelor's degree
# - 3 - Higher education - degree
# - 4 - Higher education - master's
# - 5 - Higher education - doctorate
# - 6 - Frequency of higher education
# - 9 - 12th year of schooling - not completed
# - 10 - 11th year of schooling - not completed
# - 12 - Other - 11th year of schooling
# - 14 - 10th year of schooling
# - 15 - 10th year of schooling - not completed
# - 19 - Basic education 3rd cycle (9th/10th/11th year) or equiv.
# - 38 - Basic education 2nd cycle (6th/7th/8th year) or equiv.
# - 39 - Technological specialization course
# - 40 - Higher education - degree (1st cycle)
# - 42 - Professional higher technical course
# - 43 - Higher education - master (2nd cycle)
# 
# ### Previous qualification (grade)
# Grade of previous qualification (between 0 and 200)
# 
# ### Nacionality
# The nationality of the student. (Categorical)
# - 1 - Portuguese
# - 2 - German
# - 6 - Spanish
# - 11 - Italian
# - 13 - Dutch
# - 14 - English
# - 17 - Lithuanian
# - 21 - Angolan
# - 22 - Cape Verdean
# - 24 - Guinean
# - 25 - Mozambican
# - 26 - Santomean
# - 32 - Turkish
# - 41 - Brazilian
# - 62 - Romanian
# - 100 - Moldova (Republic of)
# - 101 - Mexican
# - 103 - Ukrainian
# - 105 - Russian
# - 108 - Cuban
# - 109 - Colombian
# 
# ### Mother's qualification
# The qualification of the student's mother. (Categorical)
# - 1 - Secondary Education - 12th Year of Schooling or Eq.
# - 2 - Higher Education - Bachelor's Degree
# - 3 - Higher Education - Degree
# - 4 - Higher Education - Master's
# - 5 - Higher Education - Doctorate
# - 6 - Frequency of Higher Education
# - 9 - 12th Year of Schooling - Not Completed
# - 10 - 11th Year of Schooling - Not Completed
# - 11 - 7th Year (Old)
# - 12 - Other - 11th Year of Schooling
# - 14 - 10th Year of Schooling
# - 18 - General commerce course
# - 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.
# - 22 - Technical-professional course
# - 26 - 7th year of schooling
# - 27 - 2nd cycle of the general high school course
# - 29 - 9th Year of Schooling - Not Completed
# - 30 - 8th year of schooling
# - 34 - Unknown
# - 35 - Can't read or write
# - 36 - Can read without having a 4th year of schooling
# - 37 - Basic education 1st cycle (4th/5th year) or equiv.
# - 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.
# - 39 - Technological specialization course
# - 40 - Higher education - degree (1st cycle)
# - 41 - Specialized higher studies course
# - 42 - Professional higher technical course
# - 43 - Higher Education - Master (2nd cycle)
# - 44 - Higher Education - Doctorate (3rd cycle)
# 
# ### Father's qualification
# The qualification of the student's father. (Categorical)
# - 1 - Secondary Education - 12th Year of Schooling or Eq.
# - 2 - Higher Education - Bachelor's Degree
# - 3 - Higher Education - Degree
# - 4 - Higher Education - Master's
# - 5 - Higher Education - Doctorate
# - 6 - Frequency of Higher Education
# - 9 - 12th Year of Schooling - Not Completed
# - 10 - 11th Year of Schooling - Not Completed
# - 11 - 7th Year (Old)
# - 12 - Other - 11th Year of Schooling
# - 13 - 2nd year complementary high school course
# - 14 - 10th Year of Schooling
# - 18 - General commerce course
# - 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.
# - 20 - Complementary High School Course
# - 22 - Technical-professional course
# - 25 - Complementary High School Course - not concluded
# - 26 - 7th year of schooling
# - 27 - 2nd cycle of the general high school course
# - 29 - 9th Year of Schooling - Not Completed
# - 30 - 8th year of schooling
# - 31 - General Course of Administration and Commerce
# - 33 - Supplementary Accounting and Administration
# - 34 - Unknown
# - 35 - Can't read or write
# - 36 - Can read without having a 4th year of schooling
# - 37 - Basic education 1st cycle (4th/5th year) or equiv.
# - 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.
# - 39 - Technological specialization course
# - 40 - Higher education - degree (1st cycle)
# - 41 - Specialized higher studies course
# - 42 - Professional higher technical course
# - 43 - Higher Education - Master (2nd cycle)
# - 44 - Higher Education - Doctorate (3rd cycle)
# 
# ### Mother's occupation
# The occupation of the student's mother. (Categorical)
# - 0 - Student
# - 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers
# - 2 - Specialists in Intellectual and Scientific Activities
# - 3 - Intermediate Level Technicians and Professions
# - 4 - Administrative staff
# - 5 - Personal Services, Security and Safety Workers and Sellers
# - 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry
# - 7 - Skilled Workers in Industry, Construction and Craftsmen
# - 8 - Installation and Machine Operators and Assembly Workers
# - 9 - Unskilled Workers
# - 10 - Armed Forces Professions
# - 90 - Other Situation
# - 122 - Health professionals
# - 123 - teachers
# - 125 - Specialists in information and communication technologies (ICT)
# - 131 - Intermediate level science and engineering technicians and professions
# - 132 - Technicians and professionals, of intermediate level of health
# - 134 - Intermediate level technicians from legal, social, sports, cultural and similar services
# - 141 - Office workers, secretaries in general and data processing operators
# - 143 - Data, accounting, statistical, financial services and registry-related operators
# - 144 - Other administrative support staff
# - 151 - personal service workers
# - 152 - sellers
# - 153 - Personal care workers and the like
# - 171 - Skilled construction workers and the like, except electricians
# - 173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like
# - 175 - Workers in food processing, woodworking, clothing and other industries and crafts
# - 191 - cleaning workers
# - 192 - Unskilled workers in agriculture, animal production, fisheries and forestry
# - 193 - Unskilled workers in extractive industry, construction, manufacturing and transport
# - 194 - Meal preparation assistants
# 
# ### Father's occupation
# The occupation of the student's father. (Categorical)
# - 0 - Student
# - 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers
# - 2 - Specialists in Intellectual and Scientific Activities
# - 3 - Intermediate Level Technicians and Professions
# - 4 - Administrative staff
# - 5 - Personal Services, Security and Safety Workers and Sellers
# - 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry
# - 7 - Skilled Workers in Industry, Construction and Craftsmen
# - 8 - Installation and Machine Operators and Assembly Workers
# - 9 - Unskilled Workers
# - 10 - Armed Forces Professions
# - 101 - Armed Forces Officers
# - 102 - Armed Forces Sergeants
# - 103 - Other Armed Forces personnel
# - 112 - Directors of administrative and commercial services
# - 114 - Hotel, catering, trade and other services directors
# - 121 - Specialists in the physical sciences, mathematics, engineering and related techniques
# - 122 - Health professionals
# - 123 - teachers
# - 124 - Specialists in finance, accounting, administrative organization, public and commercial relations
# - 131 - Intermediate level science and engineering technicians and professions
# - 132 - Technicians and professionals, of intermediate level of health
# - 134 - Intermediate level technicians from legal, social, sports, cultural and similar services
# - 135 - Information and communication technology technicians
# - 141 - Office workers, secretaries in general and data processing operators
# - 143 - Data, accounting, statistical, financial services and registry-related operators
# - 144 - Other administrative support staff
# - 151 - personal service workers
# - 152 - sellers
# - 153 - Personal care workers and the like
# - 154 - Protection and security services personnel
# - 161 - Market-oriented farmers and skilled agricultural and animal production workers
# - 163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence
# - 171 - Skilled construction workers and the like, except electricians
# - 172 - Skilled workers in metallurgy, metalworking and similar
# - 174 - Skilled workers in electricity and electronics
# - 175 - Workers in food processing, woodworking, clothing and other industries and crafts
# - 181 - Fixed plant and machine operators
# - 182 - assembly workers
# - 183 - Vehicle drivers and mobile equipment operators
# - 192 - Unskilled workers in agriculture, animal production, fisheries and forestry
# - 193 - Unskilled workers in extractive industry, construction, manufacturing and transport
# - 194 - Meal preparation assistants
# - 195 - Street vendors (except food) and street service providers
# 
# ### Admission grade
# Admission grade (between 0 and 200)
# 
# ### Displaced
# Whether the student is a displaced person. (Categorical)
# - 1 – yes
# - 0 – no
# 
# ### Educational special needs
# Whether the student has any special educational needs. (Categorical)
# - 1 – yes
# - 0 – no
# 
# ### Debtor
# Whether the student is a debtor. (Categorical)
# - 1 – yes
# - 0 – no
# 
# ### Tuition fees up to date
# Whether the student's tuition fees are up to date. (Categorical)
# - 1 – yes
# - 0 – no
# 
# ### Gender
# The gender of the student. (Categorical)
# - 1 – male
# - 0 – female
# 
# ### Scholarship holder
# Whether the student is a scholarship holder. (Categorical)
# - 1 – yes
# - 0 – no
# 
# ### Age at enrollment
# The age of the student at the time of enrollment. (Numerical)
# 
# ### International
# Whether the student is an international student. (Categorical)
# - 1 – yes
# - 0 – no
# 
# ### Curricular units 1st sem (credited)
# The number of curricular units credited by the student in the first semester. (Numerical)
# 
# ### Curricular units 1st sem (enrolled)
# The number of curricular units enrolled by the student in the first semester. (Numerical)
# 
# ### Curricular units 1st sem (evaluations)
# The number of curricular units evaluated by the student in the first semester. (Numerical)
# 
# ### Curricular units 1st sem (approved)
# The number of curricular units approved by the student in the first semester. (Numerical)
# 

# In[10]:


# Mengecek info dataset
df.info()


# In[11]:


# Mengecek missing value
df.isna().sum()


# In[12]:


# Mengecek duplikat data
df.duplicated().sum()


# ## Data Preparation / Preprocessing

# In[14]:


# Mengubah tipe data yang tidak sesuai pada kolom data
numerical_cols = [
    "Application_order",
    "Previous_qualification_grade",
    "Admission_grade",
    "Age_at_enrollment",
    "Curricular_units_1st_sem_credited",
    "Curricular_units_1st_sem_enrolled",
    "Curricular_units_1st_sem_evaluations",
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Curricular_units_1st_sem_without_evaluations",
    "Curricular_units_2nd_sem_credited",
    "Curricular_units_2nd_sem_enrolled",
    "Curricular_units_2nd_sem_evaluations",
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade",
    "Curricular_units_2nd_sem_without_evaluations",
    "Unemployment_rate",
    "Inflation_rate",
    "GDP"
]

categorical_cols = [
    "Marital_status",
    "Application_mode",
    "Course",
    "Daytime_evening_attendance",
    "Previous_qualification",
    "Nacionality",
    "Mothers_qualification",
    "Fathers_qualification",
    "Mothers_occupation",
    "Fathers_occupation",
    "Displaced",
    "Educational_special_needs",
    "Debtor",
    "Tuition_fees_up_to_date",
    "Gender",
    "Scholarship_holder",
    "International",
    "Status"
]
edu_df = df.copy()
edu_df[categorical_cols] = edu_df[categorical_cols].astype('object')


# In[15]:


# untuk mengecek column setelah diubah tipe date object dari categorical columns
pd.set_option('display.max_columns', None)

edu_df.head(5) 


# In[16]:


edu_df.info()


# In[17]:


# untuk ketahui categorical columns
for col in categorical_cols:
    print(edu_df[col].value_counts())


# In[18]:


# Distribusi fitur numerikal
num_features = edu_df.select_dtypes(include=[np.number])
num_plots = len(num_features.columns)
cols = 2  
rows = math.ceil(num_plots / cols) 
plt.figure(figsize=(15, 4 * rows))  
for i, column in enumerate(num_features.columns, 1):
    plt.subplot(rows, cols, i) 
    sns.histplot(edu_df[column], bins=50, kde=True, color='blue')
    plt.title(f'Distribusi {column}')
plt.tight_layout()
plt.show()


# In[19]:


# Distribusi fitur kategorikal
cat_features = edu_df.select_dtypes(include=[object])
plt.figure(figsize=(15, 50))
for i, column in enumerate(cat_features.columns, 1):
    plt.subplot(10, 2, i)
    sns.histplot(edu_df[column], bins=50, kde=True, color='blue')
    plt.title(f'Distribusi {column}')
    plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[20]:


# Heatmap korelasi untuk fitur numerik
plt.figure(figsize=(21, 14))  # Increase figure size for better readability

correlation_matrix = edu_df[numerical_cols].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, 
            annot_kws={'size': 8})

plt.title('Heatmap Korelasi', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(rotation=0, fontsize=12)

plt.tight_layout()
plt.show()


# In[21]:


# Untuk memeriksa nilai unik
edu_df.nunique()


# In[22]:


# # Buat instance LabelEncoder
# df_cat = edu_df.copy()
# label_encoder = LabelEncoder()
 
# # List kolom kategorikal yang perlu di-encode
 
# # Encode kolom kategorikal
# for column in categorical_cols:
#     df_cat[column] = label_encoder.fit_transform(df_cat[column])
 
# # Tampilkan DataFrame untuk memastikan encoding telah diterapkan
# df_cat.head()


# ## Modeling

# In[24]:


# Melakukan duplikasi dataset
df_cleaned = edu_df.copy()
print(df_cleaned.columns.tolist())


# In[25]:


from sklearn.preprocessing import StandardScaler
import pandas as pd

# Identifikasi fitur numerik dan kategorikal
categorical_columns = df_cleaned.select_dtypes(include=['object']).columns.tolist()
numerical_columns = df_cleaned.select_dtypes(include=['int64', 'float64']).columns.tolist()

# One-hot encoding untuk fitur kategorikal
df_cleaned = pd.get_dummies(df_cleaned, columns=categorical_columns, drop_first=False)

# Update numerical columns to reflect the new structure after encoding
numerical_columns = df_cleaned.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Standardisasi fitur numerik
scaler = StandardScaler()
df_cleaned[numerical_columns] = scaler.fit_transform(df_cleaned[numerical_columns])

# Mengubah nilai True dan False menjadi 1 dan 0
df_cleaned = df_cleaned.astype(int)


# In[26]:


# Simpan scaler
joblib.dump(scaler, 'model/scaler.pkl')


# In[27]:


df_cleaned.head()


# In[28]:


# Memisahkan fitur (X) dan target (y)
X = df_cleaned.drop(['Status_Dropout','Status_Enrolled','Status_Graduate'], axis=1)
X = X[['Application_order', 'Previous_qualification_grade', 'Admission_grade', 'Age_at_enrollment', 'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate', 'Inflation_rate', 'GDP']]
y = df_cleaned[['Status_Dropout','Status_Enrolled','Status_Graduate']]

# Membagi data menjadi training dan testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[29]:


from sklearn.model_selection import GridSearchCV
# Melakukan grid search
rdf_model = RandomForestClassifier(random_state=42)

# Parameter grid
param_grid = { 
    'n_estimators': [100, 200],
    'max_depth': [10, None],
    'min_samples_split': [2, 5],
    'max_features': ['sqrt']
}
 
# Grid search
CV_rdf = GridSearchCV(estimator=rdf_model, param_grid=param_grid, cv=5, n_jobs=-1)
CV_rdf.fit(X_train, y_train)


# In[30]:


# Menampilkan hasil grid search
print("best parameters: ", CV_rdf.best_params_)


# In[31]:


# Membuat model Random Forest Classifier dengan parameter terbaik
rf_model = RandomForestClassifier(
    random_state=42, 
    max_depth=10, 
    n_estimators=200, 
    max_features='sqrt', 
    min_samples_split= 2,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)


# ## Evaluation

# In[33]:


# Memprediksi pada data test
y_pred = rf_model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Classification Report:\n", report)


# In[34]:


# Menyimpan model ke dalam file
joblib.dump(rf_model, "model/rdf_model.joblib")


# In[35]:


from sqlalchemy import create_engine
 
URL = "postgresql://postgres.mcvvlagsohvgmcldxopr:hKoXydPQB9vPaF1P@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"
engine = create_engine(URL)
df.to_sql('employee', engine)

