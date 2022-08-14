player=open("player.txt",'r')
lines=player.readlines()
avatar_selector=lines[2]
lines[8]="woman2"
player=open("player.txt","w")
player.writelines(lines)
player.close()
