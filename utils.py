import pickle
import json
import numpy as np  
import warnings
warnings.simplefilter("ignore")
import config


class Home_Price_Prediction():
    def __init__(self,CRIM,ZN,INDUS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.CRIM=CRIM
        self.ZN=ZN  
        self.INDUS=INDUS 
        self.NOX=NOX 
        self.RM=RM 
        self.AGE=AGE 
        self.DIS=DIS
        self.RAD=RAD            
        self.TAX=TAX          
        self.PTRATIO=PTRATIO           
        self.B=B           
        self.LSTAT=LSTAT

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb")as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,"r")as f:
            self.json_data=json.load(f)

    def get_predicted_charges(self):
        self.load_model()
        test_array=np.zeros(len(self.json_data["columns"]))
        test_array[0]=self.CRIM
        test_array[1]=self.ZN
        test_array[2]=self.INDUS
        test_array[3]=self.NOX
        test_array[4]=self.RM
        test_array[5]=self.AGE
        test_array[6]=self.DIS
        test_array[7]=self.RAD
        test_array[8]=self.TAX
        test_array[9]=self.PTRATIO
        test_array[10]=self.B
        test_array[11]=self.LSTAT
            
        print("test array:",test_array)             
        predicted_charges=self.model.predict(test_array.reshape(1,-1))
        return predicted_charges

# if __name__=="__main__":
#     CRIM=Home_Price_Prediction.CRIM
#     ZN=Home_Price_Prediction.ZN
#     INDUS=Home_Price_Prediction.INDUS
#     NOX=Home_Price_Prediction.NOX
#     RM=Home_Price_Prediction.RM
#     AGE=Home_Price_Prediction.AGE
#     DIS=Home_Price_Prediction.DIS
#     RAD=Home_Price_Prediction.RID
#     TAX=Home_Price_Prediction.TAX
#     PTRATIO=Home_Price_Prediction.PTRATIO
#     B=Home_Price_Prediction.B
#     LSTAT=Home_Price_Prediction.LSTAT
#     home_ins=Home_Price_Prediction(CRIM,ZN,INDUS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
#     Home_Price_Prediction.get_predicted_charges()
    