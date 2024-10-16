#先将将文件读取出来，在一个个赋给拥有这些成分的变量数组
import json
class Data:
    def __init__(self,date,message,money,place):
        self.date=date
        self.message=message
        self.money=money
        self.place=place
    def __str__(self):
        return f"{self.date} {self.message} {self.money} {self.place}"


#定义文件读取的相关功能
class FileReader:
    def ReadFile(self)->list[Data]:
        pass

class csvReader(FileReader):
    def __init__(self,path):
        self.path=path

    def ReadFile(self) ->list[Data]:
        f=open(self.path,'r',encoding="UTF-8")

        record_list: list[Data]= []
        for line in f.readlines():
            line = line.strip()
            data_list=line.split(",")
            record=Data(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path=path

    def ReadFile(self) ->list[Data]:
        f = open(self.path, 'r', encoding="UTF-8")
        record_list: list[Data] = []

        for line in f.readlines():
            data_dict=json.loads(line)
            record=Data(data_dict["date"],data_dict["order id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list


# csv_file_reader=csvReader("D:/python操作.txt")
# for i in csv_file_reader.ReadFile():
#     print(i)
json_file_reader=JsonFileReader("D:/python操作2.txt")
for i in json_file_reader.ReadFile():
    print(i)
# print(json_file_reader.ReadFile())
# json_file_reader.ReadFile()



