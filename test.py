import os
from WeightLifter import WeightLifter, Lift

if __name__ == "__main__":

    # test=[]
    # test.append(Lift(45,1,"Created",'ivan pachon',1,"C&J"))

    ivan=WeightLifter(
        'Ivan',
        'Pachon',
        '81 kg',
        80,
        115,
        90
    )
    print(ivan.get_current_attempt('CleanandJerk'))

    print(ivan.change_weight_attempt('CleanandJerk', 120))

    print(ivan.get_current_attempt('CleanandJerk'))

    print(ivan.lift('CleanandJerk', 'successful'))

    print(ivan.get_all_attempts('CleanandJerk'))

    print(ivan.change_weight_attempt('CleanandJerk', 130))

    print(ivan.get_all_attempts('CleanandJerk'))

    print(ivan.change_weight_attempt('CleanandJerk', 140))

    print(ivan.change_weight_attempt('CleanandJerk', 160))

    print(ivan.get_all_attempts('CleanandJerk'))

    print(ivan.lift('CleanandJerk', 'failed'))

    print(ivan.get_all_attempts('CleanandJerk'))

    