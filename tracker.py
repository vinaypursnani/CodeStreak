# from email.policy import default
# from typing import Text
# from numpy import size
import pandas as pd
import PySimpleGUI as sg
from datetime import date

# Excel File Path
EXCEL_FILE = 'TestSheet.xlsx'

# initializing dataframe
df = pd.read_excel(EXCEL_FILE)

# fetching date
today = date.today()
d1 = today.strftime("%m/%d/%Y")
d1 = "New Entry, Today's Date: " + str(d1)

# adding theme to our window
sg.theme('DarkTeal9')

# adding fields
layout = [
    [sg.Text(d1)],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')], # size means text is 15 characters wide and 1 character tall
    [sg.Text('Employee Id', size=(15,1)), sg.InputText(default='N/A', key='EmployeeId')],
    [sg.Text('Department', size=(15,1)), sg.Combo(['Accounting','Alcohol LO', 'Electical', 'Elivator', 'Engineering', 'Environmental', 
    'Feed LO/Elevator', 'Feedhouse', 'Human Resources', 'Lab', 'Maintainance', 'Mill', 'Mill/Feedhouse', 'Plant Coordinator', 'Plant Manager',
    'Powerhouse', 'Production', 'Production ALO', 'Receiving (Maximo)', 'Safety', 'Sales', 'Stills'], default='N/A', key='Department')],
    [sg.Text('Pay Type Code', size=(15,1)), sg.Radio('Hourly', 'Radio1', default=True, key='Hourly'), sg.Radio('Salaried','Radio1', default=False, key='Salaried')],
    [sg.Text('Entry Type', size=(15,1)), sg.Radio('CallIn', 'Radio2', default=True, key='CallIn'), sg.Radio('Notice','Radio2', default=False, key = 'Notice')],
    [sg.Text('Call In Response', size=(15,1)), sg.Combo(['No Response','Call received but employee is unable to report to work',
    'Call received but employee reports later than 2 hours after call'], default='N/A', key='CallInResponse')],
    #[sg.Text('Occurrence Type', size=(15,1)), sg.Spin([i for i in range (1, 10)], initial_value=0, key='CallInOccurence')],
    [sg.Text('Notice Type', size=(15,1)), sg.Combo(['Prior to Shift','During the Shift','None (No Call No Show)'], default='N/A',  key='NoticeType')],
    [sg.Text('Notice Information', size=(15,1)), sg.Combo(['Late Arrival During First HR','Late More Than 1 HR & Up to 4 HRs','Leave Up to 4 HRs Early','1st Day of Absence (in 12-week period)',
    '2nd or More Consecutive Day of Absence with doctor excuse', '2nd or More Consecutive Day of Absence Without doctor note'], default='N/A', key='NoticeInformation')],
    #[sg.Text('Occurrence Type', size=(15,1)), sg.Spin([i for i in range (1, 10)], initial_value=0, key='NoticeOccurence')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('BioUrja Renwables Attendance Tracker', layout) # passing layout to instance of window, aditionally passing the window title.

Points = 0.0
# checking for events
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        # NewEntry = values
        # print(NewEntry)
        # Getting Form Response in Excel

        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Entry Submitted!')

        # for key, value in NewEntry.items():
        #     if key == 'CallIn' and value == True:
        #         match NewEntry['CallInResponse']:
        #             case 'No Response': # Yet to add updation of more than 1 occurrence
        #                 Points += 1
        #             case 'Call received but employee is unable to report to work':
        #                 Points += 0.5
        #             case 'Call received but employee reports later than 2 hours after call':
        #                 Points += 0.5
        #         print(Points)
        #     elif key == 'Notice' and value == True:
        #         match NewEntry['NoticeType']:
        #             case 'Prior to Shift': # Yet to add updation of more than 1 occurrence
        #                 if NewEntry['NoticeInformation'] == 'Late Arrival During First HR':
        #                     Points += 0.5
        #                 elif NewEntry['NoticeInformation'] == 'Late More Than 1 HR & Up to 4 HRs':
        #                     Points += 0.5
        #                 elif NewEntry['NoticeInformation'] == 'Leave Up to 4 HRs Early':
        #                     Points += 0.5
        #                 elif NewEntry['NoticeInformation'] == '1st Day of Absence (in 12-week period)':
        #                     Points += 1
        #                 elif NewEntry['NoticeInformation'] == '2nd or More Consecutive Day of Absence with doctor excuse':
        #                     Points += 0
        #                 elif NewEntry['NoticeInformation'] == '2nd or More Consecutive Day of Absence Without doctor note':
        #                     Points += 1
        #             case 'During the Shift':
        #                 if NewEntry['NoticeInformation'] == 'Late Arrival During First HR':
        #                     Points += 0.5
        #                 elif NewEntry['NoticeInformation'] == 'Late More Than 1 HR & Up to 4 HRs':
        #                     Points += 1
        #                 elif NewEntry['NoticeInformation'] == 'Leave Up to 4 HRs Early':
        #                     Points += 0.5
        #                 elif NewEntry['NoticeInformation'] == '1st Day of Absence (in 12-week period)':
        #                     Points += 2
        #                 elif NewEntry['NoticeInformation'] == '2nd or More Consecutive Day of Absence with doctor excuse':
        #                     Points += 2
        #                 elif NewEntry['NoticeInformation'] == '2nd or More Consecutive Day of Absence Without doctor note':
        #                     Points += 2
        #             case 'None (No Call No Show)':
        #                 if NewEntry['NoticeInformation'] == 'Late Arrival During First HR':
        #                     Points += 0.5
        #                 if NewEntry['NoticeInformation'] == '1st Day of Absence (in 12-week period)':
        #                     Points += 3
        #                 elif NewEntry['NoticeInformation'] == '2nd or More Consecutive Day of Absence with doctor excuse':
        #                     Points += 3
        #                 elif NewEntry['NoticeInformation'] == '2nd or More Consecutive Day of Absence Without doctor note':
        #                     Points += 3              
        #         print(Points)

        
# Output Type
# Submit {'Name': 'Aman', 'EmployeeId': '122058', 'Department': 'Elivator', 'Hourly': True, 'Salaried': False, 'CallIn': False, 'Notice': True, 'CallInResponse': '', 'NoticeType': 'During the Shift', 'NoticeInformation': '1st Day of Absence (in 12-week period)'}


# closing the window
window.close()

#--------------- Call In Points ---------------#
#---------------- No Response -----------------#
# if occurrence == 1:
#   Point +=1
# elif occurence > 1:
#   Point =+2
#------- Received but unable to showup --------#
# Point +=1
#---- Call Received but arrival after 2 hr ----#
# Point +=0.5

#------------------- Notice -------------------#
# if notice == Prior_To_Shift:
#   if Late_Arrival_During_FirstHR == True:
#       if occurrence == 1 and occurrence <= 3:
#           Point += 0.5
#       if occurrence >= 4:
#           Points += 1
#   if Late_More_Than_OneHR_Upto_FourHr == True:
#       if occurrence == 1 and occurrence <= 3:
#           Point += 0.5
#       if occurrence >= 4:
#           Points += 1
#   if Leave_Upto_FourHR_Early == True:
#       if occurrence == 1 and occurrence <= 3:
#           Point += 0.5
#       if occurrence >= 4:
#           Points += 1
#   if One_Day_Absence == True: # implement 12 week logic
#       Point += 1
#   if Two_Or_More_Consecutive_Day:
#       if doctor_note = True:
#           Point += 0
#       else:
#           Point += 1
#
# if notice == During_Shift:
#   if Late_Arrival_During_FirstHR == True:
#       if occurrence == 1 and occurrence <= 3:
#           Point += 0.5
#       if occurrence >= 4:
#           Points += 1
#   if Late_More_Than_OneHR_Upto_FourHr == True:
#       if occurrence == 1 and occurrence <= 3:
#           Point += 1
#       if occurrence >= 4:
#           Points += 1
#   if Leave_Upto_FourHR_Early == True:
#       if occurrence == 1 and occurrence <= 3:
#           Point += 0.5
#       if occurrence >= 4:
#           Points += 1
#   if One_Day_Absence == True: # implement 12 week logic
#       Point += 2
#   if Two_Or_More_Consecutive_Day:
#       if doctor_note = True:
#           Point += 2
#       else:
#           Point += 2
#
# if notice == None:
# if notice == Prior_To_Shift:
#   if Late_Arrival_During_FirstHR == True:
#       if occurrence == 1 and occurrence <= 3:
#           Point += 0.5
#       if occurrence >= 4:
#           Points += 1
#   if One_Day_Absence == True: # implement 12 week logic
#       Point += 3
#   if Two_Or_More_Consecutive_Day:
#       if doctor_note = True:
#           Point += 3
#       else:
#           Point += 3


#-------------- Discipline Steps --------------#
# if individual_points == 4:
#   print("Verbal Warning From Supervisor")
# if individual_points == 5:
#   print("Written Warning From Superintendent")
# if individual_points == 7:
#   print("Meet with plant manager or alternate Designee")
# if individiual_points == 8:
#   print("Termination")

