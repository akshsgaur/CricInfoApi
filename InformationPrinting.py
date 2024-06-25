from NDTVData import *
try:
    status = section.find_all('div', class_="scr_dt-red")[1].text

    block = section.find_all('div', class_="scr_tm-wrp")
    team1_block = block[0]
    #print(team1_block)
    team1_name = team1_block.find('div', class_= "scr_tm-nm").text
    team1_score = team1_block.find('span', class_= "scr_tm-run").text

    team2_block = block[1]
    team2_name = team2_block.find('div', class_= "scr_tm-nm").text
    team2_score = team2_block.find('span', class_= "scr_tm-run").text

    print(description)
    print(location)
    print(status)
    print(current)
    print(team1_name.strip())
    print(team1_score.strip())
    print(team2_name.strip())
    print(team2_score.strip())
    print(link)
except:
    print("There is a problem with finding the data!")

