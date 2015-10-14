from pandas import DataFrame
from matplotlib import pyplot

#creating a dataframe
df=DataFrame.from_csv("UIDAI-ENR-GEN-AGE-20151013.csv")

ageBandList=list(df["Age Band"])
generatedAdhaarCountList=list(df["Aadhaar generated"])

pyplot.plot(generatedAdhaarCountList,labels=ageBandList)
pyplot.show()
