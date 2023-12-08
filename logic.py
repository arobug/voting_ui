from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic (QMainWindow, Ui_VotingMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global candidates
        global can1
        global can2
        global can3
        global can4
        candidates = []
        with open('votes.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                candidates.append([row['F_name'], row['L_name'], row['Party'], row['Votes']])
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            can1=0
            can2=0
            can3=0
            can4=0
        for i in range(len(candidates)):
            if int(candidates[i][3]) > a:
                can4=can3
                can3=can2
                can2=can1
                can1=i
                g=f
                f=e
                e=d
                d=c
                c=b
                b=a
                a = int(candidates[i][3])
                self.Other_name_3.setText(self.Other_name_2.text())
                self.Other_name_2.setText(self.Other_name_1.text())
                self.Other_name_1.setText(self.Main_name_4.text())
                self.Main_name_4.setText(self.Main_name_3.text())
                self.Main_name_3.setText(self.Main_name_2.text())
                self.Main_name_2.setText(self.Main_name_1.text())
                self.Other_votes_3.setText(self.Other_votes_2.text())
                self.Other_votes_2.setText(self.Other_votes_1.text())
                self.Other_votes_1.setText(self.Main_votes_4.text())
                self.Main_votes_4.setText(self.Main_votes_3.text())
                self.Main_votes_3.setText(self.Main_votes_2.text())
                self.Main_votes_2.setText(self.Main_votes_1.text())
                self.Other_party_3.setText(self.Other_party_2.text())
                self.Other_party_2.setText(self.Other_party_1.text())
                self.Other_party_1.setText(self.Main_party_4.text())
                self.Main_party_4.setText(self.Main_party_3.text())
                self.Main_party_3.setText(self.Main_party_2.text())
                self.Main_party_2.setText(self.Main_party_1.text())
                self.Vote_4.setText(self.Vote_3.text())
                self.Vote_3.setText(self.Vote_2.text())
                self.Vote_2.setText(self.Vote_1.text())
                self.Main_votes_1.setText(candidates[i][3])
                self.Main_name_1.setText(candidates[i][1])
                self.Main_party_1.setText(candidates[i][2])
                self.Vote_1.setText(candidates[i][1])
            elif int(candidates[i][3]) > b:
                can4=can3
                can3=can2
                can2=i
                g=f
                f=e
                e=d
                d=c
                c=b
                b = int(candidates[i][3])
                self.Other_name_3.setText(self.Other_name_2.text())
                self.Other_name_2.setText(self.Other_name_1.text())
                self.Other_name_1.setText(self.Main_name_4.text())
                self.Main_name_4.setText(self.Main_name_3.text())
                self.Main_name_3.setText(self.Main_name_2.text())
                self.Other_votes_3.setText(self.Other_votes_2.text())
                self.Other_votes_2.setText(self.Other_votes_1.text())
                self.Other_votes_1.setText(self.Main_votes_4.text())
                self.Main_votes_4.setText(self.Main_votes_3.text())
                self.Main_votes_3.setText(self.Main_votes_2.text())
                self.Other_party_3.setText(self.Other_party_2.text())
                self.Other_party_2.setText(self.Other_party_1.text())
                self.Other_party_1.setText(self.Main_party_4.text())
                self.Main_party_4.setText(self.Main_party_3.text())
                self.Main_party_3.setText(self.Main_party_2.text())
                self.Vote_4.setText(self.Vote_3.text())
                self.Vote_3.setText(self.Vote_2.text())
                self.Main_votes_2.setText(candidates[i][3])
                self.Main_name_2.setText(candidates[i][1])
                self.Main_party_2.setText(candidates[i][2])
                self.Vote_2.setText(candidates[i][1])
            elif int(candidates[i][3]) > c:
                can4=can3
                can3=i
                g = f
                f = e
                e = d
                d = c
                c = int(candidates[i][3])
                self.Other_name_3.setText(self.Other_name_2.text())
                self.Other_name_2.setText(self.Other_name_1.text())
                self.Other_name_1.setText(self.Main_name_4.text())
                self.Main_name_4.setText(self.Main_name_3.text())
                self.Other_votes_3.setText(self.Other_votes_2.text())
                self.Other_votes_2.setText(self.Other_votes_1.text())
                self.Other_votes_1.setText(self.Main_votes_4.text())
                self.Main_votes_4.setText(self.Main_votes_3.text())
                self.Other_party_3.setText(self.Other_party_2.text())
                self.Other_party_2.setText(self.Other_party_1.text())
                self.Other_party_1.setText(self.Main_party_4.text())
                self.Main_party_4.setText(self.Main_party_3.text())
                self.Vote_4.setText(self.Vote_3.text())
                self.Main_votes_3.setText(candidates[i][3])
                self.Main_name_3.setText(candidates[i][1])
                self.Main_party_3.setText(candidates[i][2])
                self.Vote_3.setText(candidates[i][1])
            elif int(candidates[i][3]) > d:
                can4 = i
                g = f
                f = e
                e = d
                d = int(candidates[i][3])
                self.Other_name_3.setText(self.Other_name_2.text())
                self.Other_name_2.setText(self.Other_name_1.text())
                self.Other_name_1.setText(self.Main_name_4.text())
                self.Other_votes_3.setText(self.Other_votes_2.text())
                self.Other_votes_2.setText(self.Other_votes_1.text())
                self.Other_votes_1.setText(self.Main_votes_4.text())
                self.Other_party_3.setText(self.Other_party_2.text())
                self.Other_party_2.setText(self.Other_party_1.text())
                self.Other_party_1.setText(self.Main_party_4.text())
                self.Main_votes_4.setText(candidates[i][3])
                self.Main_name_4.setText(candidates[i][1])
                self.Main_party_4.setText(candidates[i][2])
                self.Vote_4.setText(candidates[i][1])
            elif int(candidates[i][3]) > e:
                g = f
                f = e
                e = int(candidates[i][3])
                self.Other_name_3.setText(self.Other_name_2.text())
                self.Other_name_2.setText(self.Other_name_1.text())
                self.Other_votes_3.setText(self.Other_votes_2.text())
                self.Other_votes_2.setText(self.Other_votes_1.text())
                self.Other_party_3.setText(self.Other_party_2.text())
                self.Other_party_2.setText(self.Other_party_1.text())
                self.Other_votes_1.setText(candidates[i][3])
                self.Other_name_1.setText(candidates[i][1])
                self.Other_party_1.setText(candidates[i][2])
            elif int(candidates[i][3]) > f:
                g = f
                f = int(candidates[i][3])
                self.Other_name_3.setText(self.Other_name_2.text())
                self.Other_votes_3.setText(self.Other_votes_2.text())
                self.Other_party_3.setText(self.Other_party_2.text())
                self.Other_votes_2.setText(candidates[i][3])
                self.Other_name_2.setText(candidates[i][1])
                self.Other_party_2.setText(candidates[i][2])
            elif int(candidates[i][3]) > g:
                g = int(candidates[i][3])
                self.Other_votes_3.setText(candidates[i][3])
                self.Other_name_3.setText(candidates[i][1])
                self.Other_party_3.setText(candidates[i][2])
        self.Confirm_button.clicked.connect(lambda: self.confirm())
        self.Close_button.clicked.connect(lambda: self.close())
    def confirm(self):
        if self.Vote_1.isChecked():
            candidates[can1][3] = int(candidates[can1][3]) + 1
            self.Confirm_button.setEnabled(False)
            self.Close_button.setEnabled(True)
            self.Info_display.setText('Your vote has been recorded, thank you')
        elif self.Vote_2.isChecked():
            candidates[can2][3] = int(candidates[can2][3]) + 1
            self.Confirm_button.setEnabled(False)
            self.Close_button.setEnabled(True)
            self.Info_display.setText('Your vote has been recorded, thank you')
        elif self.Vote_3.isChecked():
            candidates[can3][3] = int(candidates[can3][3]) + 1
            self.Confirm_button.setEnabled(False)
            self.Close_button.setEnabled(True)
            self.Info_display.setText('Your vote has been recorded, thank you')
        elif self.Vote_4.isChecked():
            candidates[can4][3] = int(candidates[can4][3]) + 1
            self.Confirm_button.setEnabled(False)
            self.Close_button.setEnabled(True)
            self.Info_display.setText('Your vote has been recorded, thank you')
        elif self.Vote_Other.isChecked():
            new_candidate = [self.Other_first_name.text(),self.Other_last_name.text(),self.Other_party.text(),'1']
            x = 0
            if new_candidate[0] == 'First Name' or new_candidate[1] == 'Last Name' or new_candidate[2] == 'Party':
                x=1
                self.Info_display.setText('Please fill out information about your candidate')
            if new_candidate[0].isalpha() == False or new_candidate[1].isalpha() == False or new_candidate[2].isalpha() == False:
                x=1
                self.Info_display.setText('At least one piece of information about your candidate is invalid. Please remove any spaces numbers or other characters for you choice')
            for i in range(len(candidates)):
                if candidates[i][0] == new_candidate[0] and candidates[i][1] == new_candidate[1] and candidates[i][2] == new_candidate[2]:
                    x=1
                    candidates[i][3] = int(candidates[i][3]) + 1
                    self.Confirm_button.setEnabled(False)
                    self.Close_button.setEnabled(True)
                    self.Info_display.setText('Your vote has been recorded, thank you')
            if x == 0:
                candidates.append(new_candidate)
                self.Confirm_button.setEnabled(False)
                self.Close_button.setEnabled(True)
                self.Info_display.setText('Your vote has been recorded, thank you')
        else:
            self.Info_display.setText('Please select a candidate')
        with open('votes.csv', 'w', newline='') as o:
            writer = csv.writer(o)
            writer.writerow(['F_name','L_name','Party','Votes'])
            writer.writerows(candidates)

