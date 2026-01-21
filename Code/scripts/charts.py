import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np


data ={
       'Daniel Aloise': ('Discovery Grant', '2023', 8, 135), 
       'Shawki Areibi': ('Discovery Grant', '2023', 5, 7), 
       'Florent Avellaneda': ('Discovery Grant', '2023', 1, 5), 
       'Diogo Barradas': ('Discovery Grant', '2023', 7, 28), 
       'Taylor Brysiewicz': ('Discovery Grant', '2023', 5, 58), 
       'Wenhu Chen': ('Discovery Grant', '2023', 19, 2152), 
       'Kazem Cheshmi': ('Discovery Grant', '2023', 2, 24), 
       'Sonia Chiasson': ('Discovery Grant', '2023', 4, 7), 
       'Martin Ester': ('Discovery Grant', '2023', 4, 14), 
       'Jim Geelen': ('Discovery Grant', '2023', 2, 35), 
       'Warren Hare': ('Discovery Grant', '2023', 11, 30), 
       'Andrew Hogue': ('Discovery Grant', '2023', 1, 0), 
       'Steven Livingstone': ('Discovery Grant', '2023', 1, 4), 
       'John Mylopoulos': ('Discovery Grant', '2023', 14, 50), 
       'Rachel Pottinger': ('Discovery Grant', '2023', 4, 26), 
       'Chanchal Roy': ('Discovery Grant', '2023', 15, 122), 
       'Kamran Sedig': ('Discovery Grant', '2023', 1, 0), 
       'Quentin Stiévenart': ('Discovery Grant', '2023', 5, 20),
       'Robert Teather': ('Discovery Grant', '2023', 2, 18), 
       'David Toman': ('Discovery Grant', '2023', 1, 1), 
       'Rina Wehbe': ('Discovery Grant', '2023', 3, 9), 
       'JingTao Yao': ('Discovery Grant', '2023', 5, 9), 
       'Tarek Abdelrahman': ('Discovery Grant', '2022', 1, 11), 
       'Matthew Amy': ('Discovery Grant', '2022', 3, 11), 
       'Yangjun Chen': ('Discovery Grant', '2022', 2, 50), 
       'Eldan Cohen': ('Discovery Grant', '2022', 2, 5), 
       'Adrien Gruson': ('Discovery Grant', '2022', 2, 6),
       'Carlos HernandezCastillo': ('Discovery Grant', '2022', 6, 102), 
       'Kangsoo Kim': ('Discovery Grant', '2022', 7, 77), 
       'Mathias Lecuyer': ('Discovery Grant', '2022', 5, 79), 
       'Timothy Lethbridge': ('Discovery Grant', '2022', 43, 849), 
       'Victoria McArthur': ('Discovery Grant', '2022', 2, 9), 
       'Shane McIntosh': ('Discovery Grant', '2022', 6, 65), 
       'Ali Mesbah': ('Discovery Grant', '2022', 3, 48), 
       'Thomas Pasquier': ('Discovery Grant', '2022', 5, 138), 
       'Cody Phillips': ('Discovery Grant', '2022', 2, 19), 
       'ClaudeGuy Quimper': ('Discovery Grant', '2022', 10, 29), 
       'Gema RodriguezPerez': ('Discovery Grant', '2022', 1, 51), 
       'Yuepeng Wang': ('Discovery Grant', '2022', 4, 52), 
       'Xiaohui Yu': ('Discovery Grant', '2022', 6, 63), 
       'Leah ZhangKennedy': ('Discovery Grant', '2022', 2, 28), 
       'Alaa Alameldeen': ('Discovery Grant', '2021', 5, 122), 
       'Ann Barcomb': ('Discovery Grant', '2021', 2, 0), 
       'Christina Christara': ('Discovery Grant', '2021', 1, 6), 
       'Maged Goubran': ('Discovery Grant', '2021', 16, 179), 
       'Eitan Grinspun': ('Discovery Grant', '2021', 2, 27), 
       'Christopher Maddison': ('Discovery Grant', '2021', 9, 94), 
       'Joseph Malloch': ('Discovery Grant', '2021', 5, 50), 
       'Rachael Mansbach': ('Discovery Grant', '2021', 8, 326), 
       'Aleksandar Nikolov': ('Discovery Grant', '2021', 2, 11), 
       'Banani Roy': ('Discovery Grant', '2021', 9, 33), 
       'Jiannan Wang': ('Discovery Grant', '2021', 4, 99), 
       'Shaowei Wang': ('Discovery Grant', '2021', 10, 329), 
       'Ryan Brinkman': ('Discovery Grant', '2020', 9, 192), 
       'Juergen Dingel': ('Discovery Grant', '2020', 6, 49), 
       'David Fleet': ('Discovery Grant', '2020', 7, 1278), 
       'Hadi Hemmati': ('Discovery Grant', '2020', 2, 15), 
       'Craig Kaplan': ('Discovery Grant', '2020', 3, 83), 
       'Naimul Khan': ('Discovery Grant', '2020', 11, 300), 
       'Shehroz Khan': ('Discovery Grant', '2020', 19, 392), 
       'Madison Klarkowski': ('Discovery Grant', '2020', 4, 121), 
       'JeanFrançois Lalonde': ('Discovery Grant', '2020', 12, 433), 
       'Ondrej Lhotak': ('Discovery Grant', '2020', 10, 90), 
       'Yan Liu': ('Discovery Grant', '2020', 65, 7551), 
       'Martin Müller': ('Discovery Grant', '2020', 42, 1695), 
       'Vladimir Okhmatovski': ('Discovery Grant', '2020', 8, 45), 
       'Nicolas Papernot': ('Discovery Grant', '2020', 21, 2826), 
       'Margo Seltzer': ('Discovery Grant', '2020', 15, 739), 
       'Kevin Stanley': ('Discovery Grant', '2020', 2, 15), 
       'Elizabeth Stobert': ('Discovery Grant', '2020', 5, 34), 
       'Michiel vandePanne': ('Discovery Grant', '2020', 6, 819), 
       'Kay Wiese': ('Discovery Grant', '2020', 6, 72), 
       'JiaHuai You': ('Discovery Grant', '2020', 1, 12), 
       'Yang Zhang': ('Discovery Grant', '2020', 22, 1394), 
       'Inanc Birol': ('Discovery Grant', '2019', 17, 239), 
       'Bingshu Chen': ('Discovery Grant', '2019', 15, 555), 
       'Kerstin Dautenhahn': ('Discovery Grant', '2019', 14, 195), 
       'Konstantinos Derpanis': ('Discovery Grant', '2019', 4, 420), 
       'Stephen Dipaola': ('Discovery Grant', '2019', 6, 76), 
       'Ihab Ilyas': ('Discovery Grant', '2019', 27, 938), 
       'Pourang Irani': ('Discovery Grant', '2019', 17, 163), 
       'Fehmi Jaafar': ('Discovery Grant', '2019', 7, 164), 
       'Christian Jacob': ('Discovery Grant', '2019', 17, 245), 
       'Kenneth Kent': ('Discovery Grant', '2019', 9, 62), 
       'Michael Monagan': ('Discovery Grant', '2019', 12, 126), 
       'Nedialko Nedialkov': ('Discovery Grant', '2019', 1, 13), 
       'Eric Paquette': ('Discovery Grant', '2019', 4, 23), 
       'Reihaneh Rabbany': ('Discovery Grant', '2019', 3, 10), 
       'Frank Rudzicz': ('Discovery Grant', '2019', 26, 1314), 
       'Kevin Schneider': ('Discovery Grant', '2019', 20, 1939), 
       'Yang Wang': ('Discovery Grant', '2019', 10, 2792), 
       'David Wishart': ('Discovery Grant', '2019', 42, 7672), 
       'Eric Aubanel': ('Discovery Grant', '2018', 1, 3), 
       'Jacques Carette': ('Discovery Grant', '2018', 7, 92), 
       'Frank Dehne': ('Discovery Grant', '2018', 2, 22), 
       'Yasutaka Furukawa': ('Discovery Grant', '2018', 6, 811), 
       'Michael Godfrey': ('Discovery Grant', '2018', 15, 234), 
       'Michael Greenspan': ('Discovery Grant', '2018', 2, 9), 
       'Vasiliki Kantere': ('Discovery Grant', '2018', 3, 6), 
       'Paul Kry': ('Discovery Grant', '2018', 5, 14), 
       'Jochen Lang': ('Discovery Grant', '2018', 4, 267), 
       'Pierre LEcuyer': ('Discovery Grant', '2018', 8, 180), 
       'Maxwell Libbrecht': ('Discovery Grant', '2018', 6, 156), 
       'Regan Mandryk': ('Discovery Grant', '2018', 12, 368), 
       'Robert McLeod': ('Discovery Grant', '2018', 10, 440), 
       'Derek Nowrouzezahrai': ('Discovery Grant', '2018', 8, 256), 
       'Keval Vora': ('Discovery Grant', '2018', 2, 4), 
       'Frank Wood': ('Discovery Grant', '2018', 10, 546), 
       'Loutfouz Zaman': ('Discovery Grant', '2018', 2, 12), 
       'Xiaodan Zhu': ('Discovery Grant', '2018', 6, 153), 
       'Luiz Capretz': ('Discovery Grant', '2017', 8, 86), 
       'Thomas Coleman': ('Discovery Grant', '2017', 1, 0), 
       'Arie Gurfinkel': ('Discovery Grant', '2017', 5, 122), 
       'Florian Kerschbaum': ('Discovery Grant', '2017', 7, 344), 
       'Daniel Lemire': ('Discovery Grant', '2017', 3, 14), 
       'Herve Lombaert': ('Discovery Grant', '2017', 2, 13), 
       'Zhaosong Lu': ('Discovery Grant', '2017', 5, 178), 
       'IScott MacKenzie': ('Discovery Grant', '2017', 1, 13), 
       'Sarah Nadi': ('Discovery Grant', '2017', 7, 263), 
       'Julia Rubin': ('Discovery Grant', '2017', 10, 209), 
       'John Rubinstein': ('Discovery Grant', '2017', 12, 8074), 
       'Bernhard Thomaszewski': ('Discovery Grant', '2017', 10, 376), 
       'David Wang': ('Discovery Grant', '2017', 29, 3114), 
       'Horst Winter': ('Discovery Grant', '2017', 14, 509), 
       'Hussein AlOsman': ('Discovery Grant', '2016', 4, 174), 
       'Leonid Chindelevitch': ('Discovery Grant', '2016', 3, 77), 
       'Wayne Enright': ('Discovery Grant', '2016', 1, 0), 
       'Mark Hancock': ('Discovery Grant', '2016', 19, 1500), 
       'Nicholas Harvey': ('Discovery Grant', '2016', 71, 3060), 
       'Colin Macdonald': ('Discovery Grant', '2016', 1, 23), 
       'James Miller': ('Discovery Grant', '2016', 20, 602), 
       'Charalambos Poullis': ('Discovery Grant', '2016', 3, 142), 
       'Gregory Reid': ('Discovery Grant', '2016', 28, 2541), 
       'Brian Ross': ('Discovery Grant', '2016', 22, 786), 
       'John Tsotsos': ('Discovery Grant', '2016', 17, 473), 
       'Jonathan Anderson': ('Discovery Grant', '2015', 27, 13892), 
       'Alex Aravind': ('Discovery Grant', '2015', 2, 21), 
       'Eric Blais': ('Discovery Grant', '2015', 7, 296), 
       'Charles Clarke': ('Discovery Grant', '2015', 24, 610), 
       'MYvonne Coady': ('Discovery Grant', '2015', 7, 79), 
       'Deborah Fels': ('Discovery Grant', '2015', 6, 3717), 
       'Thomas Hurtut': ('Discovery Grant', '2015', 5, 352), 
       'Vincent Jacquemet': ('Discovery Grant', '2015', 4, 32), 
       'Sègla Kpodjedo': ('Discovery Grant', '2015', 5, 12), 
       'Paul Lu': ('Discovery Grant', '2015', 35, 10308), 
       'Shahryar Rahnamayan': ('Discovery Grant', '2015', 6, 621), 
       'Karen Rudie': ('Discovery Grant', '2015', 3, 23), 
       'Alan Wagner': ('Discovery Grant', '2015', 3, 28), 
       'Aijun An': ('Discovery Grant', '2014', 11, 2823), 
       'Ismail BenAyed': ('Discovery Grant', '2014', 9, 239), 
       'Anne Bergeron': ('Discovery Grant', '2014', 17, 767), 
       'Vadim Bulitko': ('Discovery Grant', '2014', 10, 101), 
       'Werner Dietl': ('Discovery Grant', '2014', 1, 136), 
       'Azadeh Farzan': ('Discovery Grant', '2014', 4, 70), 
       'Yong Gao': ('Discovery Grant', '2014', 7, 1753), 
       'Howard Hamilton': ('Discovery Grant', '2014', 2, 6), 
       'Ridha Khedri': ('Discovery Grant', '2014', 6, 46), 
       'JeanFrancois Lalonde': ('Discovery Grant', '2014', 4, 76), 
       'Masoud Makrehchi': ('Discovery Grant', '2014', 2, 19), 
       'Wendy Myrvold': ('Discovery Grant', '2014', 3, 23), 
       'Philippe Pasquier': ('Discovery Grant', '2014', 7, 147), 
       'Tiberiu Popa': ('Discovery Grant', '2014', 6, 100), 
       'Ping Tan': ('Discovery Grant', '2014', 19, 3038), 
       'Jens Weber': ('Discovery Grant', '2014', 10, 382), 
       'Yu Xia': ('Discovery Grant', '2014', 8, 1709), 
       'Philippe Archambault': ('Discovery Grant', '2013', 10, 282), 
       'Robert Bridson': ('Discovery Grant', '2013', 5, 173), 
       'Vijay Ganesh': ('Discovery Grant', '2013', 4, 410), 
       'Hui Jiang': ('Discovery Grant', '2013', 16, 1449), 
       'Patrick Lam': ('Discovery Grant', '2013', 6, 169), 
       'Karen Meagher': ('Discovery Grant', '2013', 5, 166), 
       'Richard StDenis': ('Discovery Grant', '2013', 9, 1509), 
       'Allan Borodin': ('Discovery Grant', '2012', 4, 73), 
       'James Cordy': ('Discovery Grant', '2012', 13, 485), 
       'Angela DemkeBrown': ('Discovery Grant', '2012', 5, 223), 
       'Randy Ellis': ('Discovery Grant', '2012', 7, 169), 
       'Alexandra Fedorova': ('Discovery Grant', '2012', 10, 752), 
       'Liane Gabora': ('Discovery Grant', '2012', 14, 327),
       'Ronald Garcia': ('Discovery Grant', '2012', 1, 2),
       'Meng He': ('Discovery Grant', '2012', 5, 140),
       'Abram Hindle': ('Discovery Grant', '2012', 8, 523),
       'Diana Inkpen': ('Discovery Grant', '2012', 15, 252), 
       'Clement Lam': ('Discovery Grant', '2012', 1, 9), 
       'Ian Mitchell': ('Discovery Grant', '2012', 8, 349), 
       'Ian Munro': ('Discovery Grant', '2012', 6, 214), 
       'Dinesh Pai': ('Discovery Grant', '2012', 13, 550), 
       'Cenk Sahinalp': ('Discovery Grant', '2012', 12, 753), 
       'Peter Selinger': ('Discovery Grant', '2012', 7, 520), 
       'Jonathan Sillito': ('Discovery Grant', '2012', 7, 580), 
       'Clark Verbrugge': ('Discovery Grant', '2012', 7, 33), 
       'James Andrews': ('Discovery Grant', '2011', 13, 730), 
       'Vaughn Betz': ('Discovery Grant', '2011', 9, 357), 
       'Mark Green': ('Discovery Grant', '2011', 15, 289), 
       'Daniel Hoffman': ('Discovery Grant', '2011', 1, 72), 
       'Manuela Kunz': ('Discovery Grant', '2011', 4, 20), 
       'Mario Marchand': ('Discovery Grant', '2011', 3, 186), 
       'Bradford Nickerson': ('Discovery Grant', '2011', 7, 39), 
       'Arrvindh Shriraman': ('Discovery Grant', '2011', 3, 83), 
       'Eugenia Ternovska': ('Discovery Grant', '2011', 6, 71), 
       'Vassilios Tzerpos': ('Discovery Grant', '2011', 2, 15), 
       'Alasdair Urquhart': ('Discovery Grant', '2011', 4, 69), 
       'Jose Amaral': ('Discovery Grant', '2010', 24, 416), 
       'Robert Biddle': ('Discovery Grant', '2010', 11, 411), 
       'Andrei Bulatov': ('Discovery Grant', '2010', 5, 40), 
       'Jörg Denzinger': ('Discovery Grant', '2010', 9, 136), 
       'Ling Guan': ('Discovery Grant', '2010', 18, 248), 
       'Laurie Hendren': ('Discovery Grant', '2010', 5, 154), 
       'Holger Hoos': ('Discovery Grant', '2010', 10, 1016), 
       'Alan Hu': ('Discovery Grant', '2010', 3, 101), 
       'Nick Koudas': ('Discovery Grant', '2010', 16, 2099), 
       'Theodore Norvell': ('Discovery Grant', '2010', 5, 17), 
       'Hiren Patel': ('Discovery Grant', '2010', 6, 112), 
       'Karthik Pattabiraman': ('Discovery Grant', '2010', 5, 156), 
       'Derek Rayside': ('Discovery Grant', '2010', 1, 0), 
       'Nadia Tawbi': ('Discovery Grant', '2010', 1, 14), 
       'Robin Cockett': ('Discovery Grant', '2009', 8, 229), 
       'Eugene Fiume': ('Discovery Grant', '2009', 2, 15), 
       'Laks Lakshmanan': ('Discovery Grant', '2009', 14, 1161), 
       'Greg Reid': ('Discovery Grant', '2009', 3, 46), 
       'Deborah Stacey': ('Discovery Grant', '2009', 1, 13), 
       'Eleni Stroulia': ('Discovery Grant', '2009', 16, 934), 
       'Andreas Veneris': ('Discovery Grant', '2009', 11, 155), 
       'Patrice Chalin': ('Discovery Grant', '2008', 9, 461), 
       'Nicolas Moitessier': ('Discovery Grant', '2008', 13, 1320), 
       'Eric Neufeld': ('Discovery Grant', '2008', 5, 62), 
       'Jonathan Schaeffer': ('Discovery Grant', '2008', 12, 387), 
       'Magy SeifElNasr': ('Discovery Grant', '2008', 8, 157)
}


researchers = list(data.keys())
publications = [record[2] for record in data.values()]
citations = [record[3] for record in data.values()]
x = list(range(len(data)))  

with PdfPages('charts.pdf') as pdf:

    

    # Bar chart: Publications 
    plt.figure()
    plt.bar(x, publications, color="skyblue")
    average_pub = sum(publications) / len(publications)
    plt.axhline(y=average_pub, color='red', linestyle='--', label=f'Average: {average_pub:.2f}')
    plt.legend()
    plt.title("Publication Count per Researcher")
    plt.ylabel("Publications")
    plt.xlabel("Researchers")
    plt.xticks([]) 
    plt.savefig("bar_publications.pdf")
    plt.close()

    # Bar chart: Citations 
    plt.figure()
    plt.bar(x, citations, color="orange")
    average_cit = sum(citations) / len(citations)
    plt.axhline(y=average_cit, color='red', linestyle='--', label=f'Average: {average_cit:.2f}')
    plt.legend()
    plt.title("Citation Count per Researcher")
    plt.ylabel("Citations")
    plt.xlabel("Researchers")
    plt.xticks([])
    plt.savefig("bar_citations.pdf")
    plt.close()

    # Scatterplot for Citations vs Publications
    plt.figure(figsize=(8, 6))
    plt.scatter(publications, citations, color='purple')
    plt.title('Citations vs Publications')
    plt.xlabel('Publications')
    plt.ylabel('Citations')

   
    z = np.polyfit(publications, citations, 1)
    p = np.poly1d(z)
    plt.plot(publications, p(publications), "r--", label=f"Trendline")

    
    correlation = np.corrcoef(publications, citations)[0, 1]
    plt.legend(title=f"Pearson r = {correlation:.2f}")
    plt.tight_layout()
    plt.savefig("scatterplot_citation_vs_publication.pdf")
  

