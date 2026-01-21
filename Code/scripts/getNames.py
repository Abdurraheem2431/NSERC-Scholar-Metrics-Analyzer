import pandas as pd 
from getCounts import getCounts

def main():
    data = pd.read_excel("NSERC_RESULTS.xlsx", skiprows= 3)
    
    researchers = {}

    for index, row in data.iterrows():
        name = formatName(row["Name"])
        award = row["Program"]  
        year = getYear(row["Fiscal Year"])
        if ("Discovery Grants Program" in award):
            pub,citation = getCounts(name,year)
            print(pub,citation)
            if (pub == 0 and citation == 0):
                continue
            researchers[name] = ("Discovery Grant", year, pub, citation)
    sorted_researchers = dict(sorted(researchers.items(), key=lambda item: item[1][1], reverse=True))
    with open("output.txt", "w") as file:
        for name, (award, year, pub, citation) in sorted_researchers.items():
            file.write(f"Name: {name} Year: {year} Publication count: {pub} Citation count: {citation}\n")
    return sorted_researchers

def formatName(name):
    LastName, firstName = name.split(", ")
    return firstName + " " + LastName


def getYear(year):
    firstYear, LastYear = year.split("-")
    return firstYear


print(main())