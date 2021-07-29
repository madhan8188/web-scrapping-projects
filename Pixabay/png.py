# import pandas as pd 
# df = pd.read_csv('/home/stemland/Desktop/pixabay/pixabay_samples.csv')
# df.drop(["img_url_480","img_url_960_720","img_url_1280"], axis = 1, inplace = True)
# df.to_csv('pix.csv')   
list=[10,20,22,10,39,45,34,10,20,22,22,10,39,10,39,45,34,10]
list1=[]
for x in list:
    if x not in list1:
        list1.append(x)
print(list1)