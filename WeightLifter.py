import os
from types import DynamicClassAttribute
from unicodedata import name
from urllib import response
import sqlite3
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lift():

    def __init__(self,
    weight,
    no_of_attempt,
    status,
    weightlifter_name,
    no_of_changes,
    type
    ) -> None:
        self.weight=weight
        self.no_of_attempt=no_of_attempt
        self.status=status
        self.weightlifter_name=weightlifter_name
        self.no_of_changes=no_of_changes
        self.type=type


class WeightLifter():

    def __init__(self,
    name:str,
    lastname:str, 
    weightcategory:str,
    weight:int,
    open_clean_and_jerk_weight:int,
    open_snatch_weight:int
    ) -> None:
        self.name=name
        self.lastname=lastname
        self.weightcategory=weightcategory
        self.weight=weight
        self.open_clean_and_jerk_weight=open_clean_and_jerk_weight
        self.open_snatch_weight=open_snatch_weight
        self.cleanandjerk_attempt=open_clean_and_jerk_weight
        self.snatch_attempt=open_snatch_weight
        self.best_lift_cleanandjerk=0
        self.best_lift_snatch=0
        self.lift_cleanandjerk=[]
        self.lift_cleanandjerk.append(Lift(open_clean_and_jerk_weight,1,"Created",name,1,"C&J"))
        self.lift_snatch=[]
        self.lift_snatch.append(Lift(open_snatch_weight,1,"Created",name,1,"S"))

    
    def get_current_attempt(self, type:str):
        if type=='CleanandJerk':
            lift_number=len(self.lift_cleanandjerk)-1
            return (
            self.lift_cleanandjerk[lift_number].weight,
            self.lift_cleanandjerk[lift_number].no_of_attempt,
            self.lift_cleanandjerk[lift_number].status,
            self.lift_cleanandjerk[lift_number].no_of_changes)
        if type=='Snatch':
            lift_number=len(self.lift_snatch)-1
            return (
            self.lift_snatch[lift_number].weight,
            self.lift_snatch[lift_number].no_of_attempt,
            self.lift_snatch[lift_number].status,
            self.lift_snatch[lift_number].no_of_changes) 

    def get_all_attempts(self, type:str):
        response=[]
        if type=='CleanandJerk':
            for lift_number in range(len(self.lift_cleanandjerk)):
                response.append((
                self.lift_cleanandjerk[lift_number].weight,
                self.lift_cleanandjerk[lift_number].no_of_attempt,
                self.lift_cleanandjerk[lift_number].status,
                self.lift_cleanandjerk[lift_number].no_of_changes))
            return response
        if type=='Snatch':
            for lift_number in range(len(self.lift_snatch)):
                response.append((
                self.lift_snatch[lift_number].weight,
                self.lift_snatch[lift_number].no_of_attempt,
                self.lift_snatch[lift_number].status,
                self.lift_snatch[lift_number].no_of_changes)) 
            return response
 

    def change_weight_attempt(self, type:str, new_weight:int):
        try:
             current_weight,current_no_attempt,lift_status, current_change_of_attempts=self.get_current_attempt(type)
        except:
            return('error changing weight')
        if type=='CleanandJerk':
            if current_weight>new_weight:
                return (f"Newt Weight should be higher than {current_weight}")
            if current_no_attempt>3 and current_change_of_attempts>1:
                return (f"Current attemp {current_no_attempt} and number of changes {current_change_of_attempts}, cannot change weight")
            lift_number=len(self.lift_cleanandjerk)-1
            self.lift_cleanandjerk[lift_number].weight=new_weight
            self.lift_cleanandjerk[lift_number].no_of_changes+=1
            return ('New weight Successfully updated')  
        if type=='Snatch':
            if current_weight>new_weight:
                return (f"Newt Weight should be higher than {current_weight}")
            if current_no_attempt>3 and current_change_of_attempts>1:
                return (f"Current attemp {current_no_attempt} and number of changes {current_change_of_attempts}, cannot change weigjt")
            lift_number=len(self.lift_snatch)-1
            self.lift_snatch[lift_number].weight=new_weight
            self.lift_snatch[lift_number].no_of_changes=+1
            return ('New weight Successfully updated')   
    
    def lift(self,type, status):
        try:
            current_weight,current_no_attempt,lift_status, current_change_of_attempts=self.get_current_attempt(type)
        except:
            return('error lifting')
        if lift_status != 'successful':
            if type=='CleanandJerk':
                lift_number=len(self.lift_cleanandjerk)-1
                self.lift_cleanandjerk[lift_number].status=status
                self.best_lift_cleanandjerk=current_weight
                if current_no_attempt<3:
                    self.__auto_create_lift('CleanandJerk', current_weight+1,current_no_attempt+1)
                return(f'Lift was successfull, current number of lift {current_no_attempt}')
            if type=='Snatch':
                lift_number=len(self.lift_snatch)-1
                self.lift_snatch[lift_number].status=status
                self.best_lift_snatch=current_weight
                if current_no_attempt<3:
                    self.__auto_create_lift('Snatch', current_weight+1,current_no_attempt+1)
                return(f'Lift was successfull, current number of lift {current_no_attempt}')
    
    def __auto_create_lift(self, type, weight, lift_no):
        if type=='CleanandJerk':
            self.lift_cleanandjerk.append(Lift(weight,lift_no,"Created",name,1,"C&J"))
        if type=='Snatch':
            self.lift_snatch.append(Lift(weight,lift_no,"Created",name,1,"S"))





