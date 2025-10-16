import datetime #import library datetime
import pandas as pd #import library pandas
import matplotlib.pyplot as plt
from matplotlib.patches import Patch




def bmi_calculator(height,weight):#function to calculate bmi and category
    bmi=weight/(height**2)              
    if bmi<18.5:
        category="Underweight"
    elif 18.5<=bmi<=24.9:
        category="Normalweight"
    elif 25<=bmi<=29.9:
        category="Overweight"
    else:
        category="Obese"
    return bmi,category


number=int(input("Enter the number of entries required: "))#user input for number of entries
users_data=[] #list to store user data

for i in range(0,number): #loop to take user input for each entry
    name=input("Enter the first name: ").capitalize()#capitalize the first letter of name
    while not name.isalpha():
        print("Invalid name. Only letters are allowed")
        name=input("Enter the first name: ").capitalize()
    
    age=int(input("Enter the age: "))
    while age<=0 or age>120: #validation for age
        print("Invalid age. Please enter a valid age between 1 and 120.")
        age=int(input("Enter the age: "))
    
    height=float(input("Enter the height in metre: "))
    while height<=0.5 or height>2.5: #validation for height
        print("Invalid height. Please enter a valid height between 0.5 and 2.5 metres.")
        height=float(input("Enter the height in metre: "))
    
    weight=float(input("Enter the weight in kg: "))
    while weight<=10 or weight>300: #validation for weight
        print("Invalid weight. Please enter a valid weight between 10 and 300 kgs.")
        weight=float(input("Enter the weight in kg: "))
    
    bmi,category=bmi_calculator(height,weight)
    users_dict={"Name":name,"Age":age,"Height(m)":height,"Weight(Kg)":weight,"BMI":round(bmi,2),"Status":category}
    users_data.append(users_dict)#append the user data to the list
print(f"\n\nDICTIONARY")
print("="*60)
print(users_data)

data_frame=pd.DataFrame(users_data)#convert to table/dataframe
data_frame=data_frame.sort_values(by="Name") #sort the table by name
data_frame.insert(0,"S.No.",[i+1 for i in range(len(data_frame))])#to add sl.no. column in the range of the length
current_time=datetime.datetime.now()
print(f"\n\n\nBMI USER DATA- {current_time.strftime('%Y-%m-%d %H:%M')}")#format the date and time
print("="*60)
print(data_frame.to_string(index=False))#print the table without index

data_frame.to_csv("BMI_data.csv",index=False)# storing the table to csv file
# Assign colors based on BMI category
colors = []
for status in data_frame['Status']:
    if status == "Underweight":
        colors.append('#ff9999')  # red-ish
    elif status == "Normalweight":
        colors.append('#66b3ff')  # blue
    elif status == "Overweight":
        colors.append('#ffcc99')  # orange
    else:  # Obese
        colors.append('#99ff99')  # green

# Plot BMI bar chart
plt.figure(figsize=(10,5))
bars = plt.bar(data_frame['Name'], data_frame['BMI'], color=colors)
plt.xlabel('Name')
plt.ylabel('BMI')
plt.title('BMI of Users')
plt.xticks(rotation=45)
plt.ylim(0, max(data_frame['BMI']) + 5)

# Create legend manually

legend_elements = [
    Patch(facecolor='#ff9999', label='Underweight'),
    Patch(facecolor='#66b3ff', label='Normalweight'),
    Patch(facecolor='#ffcc99', label='Overweight'),
    Patch(facecolor='#99ff99', label='Obese')
]
plt.legend(handles=legend_elements, title='BMI Category')
plt.show()


