
#matching:
    #__init__
    #year_extractor
    #excelGenarator






class matching:
    import difflib
    import pandas as pd

    def __init__(self,path1,path2):
        self.dataBase= pd.read_excel(path1, index_col=0)
        self.newData= pd.read_excel(path2, index_col=0)
        self.similar_name_indexes=[]

    def year_extractor(phrase):
        a= phrase.find('(')+1
        b= phrase.find(')')
        if [a,b] != [-1,-1]:
            name= phrase[:a-1]
            year= phrase[a:b]
        else:
            year= None
            name= phrase
        return [name,year]

    def normalize(self,year_check=False):
        self.newName= list(self.newData.index)
        self.org_newName= list(self.newData.index)
        self.dbName= list(self.dataBase.index)
        self.newYear= []
        self.data= []
        for i in range(len(self.dbName)):
            self.dbName[i]= str(self.dbName[i]).replace(" ","")
            self.dbName[i]= self.dbName[i].lower()


        if year_check:
            for i in range(len(self.newName)):
                [name,year]= year_extractor(str(self.newName))
                self.newYear.append(year)
                self.newName[i]= name
                self.newName[i]= str(self.newName[i]).replace(" ","")
                self.newName[i]= self.newName[i].lower()
        else:
            for i in range(len(self.newName)):
                self.newName[i]= str(self.newName[i]).replace(" ","")
                self.newName[i]= self.newName[i].lower()

    def similarityCheck(self,similarity_percentage):
        for i in range(len(self.dbName)):
            data.append([])
            temp = find_closet(self.dbName[i], self.newName)
            self.similar_name_indexes.append(self.newName.index(temp))
            original_name= self.org_newName[self.similar_name_indexes]
            self.data[i].append(original_name)
            if distance.get_jaro_distance(
            self.dbName[i],temp,winkler=True, scaling=0.1) > similarity_percentage:
                self.data[i].append(1)
            else:
                self.data[i].append(0)



    def excelGenarator(self,columns_titles,path,ExcelName):
        for i in range(len(self.dbName)):
            for title in columns_titles:
                temp= self.newData[title][self.similar_name_indexes[i]]
                data[i].append(temp)
        newExcel= pd.DataFrame(data,index= self.dataBase.index,columns= columns_titles)
        newExcel.to_excel(path + ExcelName + ".xlsx")



    def find_closet(name,name_list):
        temp = difflib.get_close_matches(name, name_list, n=1)
        return temp
