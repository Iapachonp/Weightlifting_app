import os
from types import DynamicClassAttribute
from unicodedata import name

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
        self.lift_cleanandjerk[0]=Lift(open_clean_and_jerk_weight,1,"Created",name,1,"C&J")
        self.lift_snatch=[]
        self.lift_snatch[0]=Lift(open_clean_and_jerk_weight,1,"Created",name,1,"S")

    
    def get_current_attempt(self, type):
        if type=='CleanandJerk':
            lift_number=len(self.lift_cleanandjerk)
            return (
            self.lift_cleanandjerk[lift_number].weight,
            self.lift_cleanandjerk[lift_number].no_of_attempt,
            self.lift_cleanandjerk[lift_number].status,
            self.lift_cleanandjerk[lift_number].no_of_changes)
        if type=='Snatch':
            lift_number=len(self.lift_snatch)
            return (
            self.lift_snatch[lift_number].weight,
            self.lift_snatch[lift_number].no_of_attempt,
            self.lift_snatch[lift_number].status,
            self.lift_snatch[lift_number].no_of_changes) 
    

    def change_weight_attempt(self, type, new_weight):
        try:
            current_no_attempt, current_weight, current_change_of_attempts=self.get_current_attempt(type)
        except:
            return(self.get_current_attempt(type))
        if type=='CleanandJerk':
            if current_weight>new_weight:
                return (f"Newt Weight should be higher than {current_weight}")
            if current_no_attempt>3 and current_change_of_attempts>1:
                return (f"Current attemp {current_no_attempt} and number of changes {current_change_of_attempts}, cannot change weigjt")
            self.cleanandjerk_attempt=new_weight
            self.numberof_change_cleanandjerk_attempts=+1
            return (current_no_attempt, self.cleanandjerk_attempt, self.numberof_change_cleanandjerk_attempts)  
        if type=='Snatch':
            if current_weight>new_weight:
                return (f"Newt Weight should be higher than {current_weight}")
            if current_no_attempt>3 and current_change_of_attempts>1:
                return (f"Current attemp {current_no_attempt} and number of changes {current_change_of_attempts}, cannot change weigjt")
            self.snatch_attempt=new_weight
            self.numberof_change_snatch_attempts=+1
            return (current_no_attempt, self.snatch_attempt, self.numberof_change_snatch_attempts)  
    
    def lift(self,type, status):
        try:
            current_no_attempt, current_weight, current_change_of_attempts=self.get_current_attempt(type)
        except:
            return(self.get_current_attempt(type))
        if status=='successful':
            if type=='CleanandJerk':
                self.best_lift_cleanandjerk=current_weight
                self.cleanandjerk_attempt=+1
                self.numberof_cleanandjerk_attempts=+1
            if type=='Snatch':
                self.best_lift_snatch=current_weight






