file1 = open('b_better_start_small.in.txt', 'r')
inputInfo = file1.readline()

engCount=int(inputInfo.split()[0])
projCount=int(inputInfo.split()[1])
##print(engCount,projCount)

##Contributor Info reading
TeamSkills={}
engs={}
for i in range(engCount) :
    
    engInfo=file1.readline().split()
    name=engInfo[0]
    skillCount=int(engInfo[1])
    engs[name]=False
    
    for j in range(skillCount):
        
        skillInfo=file1.readline().split()
        skill=skillInfo[0]
        level=int(skillInfo[1])
        
        if TeamSkills.get(skill) is None:
            TeamSkills[skill]=[]
            
        TeamSkills[skill].append((name,level))


        
## Project info reading

class Proj:
  def __init__(self, name, length,maxScore,deadLine,roles):
    self.name = name
    self.length = length
    self.maxScore = maxScore
    self.deadLine = deadLine
    self.roles = roles


projects=[]

for i in range(projCount):
    projInfo=file1.readline().split()
    name=projInfo[0]
    length=int(projInfo[1])
    MaxScore=int(projInfo[2])
    DeadLine=int(projInfo[3])
    RolesCount=int(projInfo[4])
    Roles=[]
    
    for j in range(RolesCount):
        RoleInfo=file1.readline().split()
        RoleSkill=RoleInfo[0]
        RoleLevel=RoleInfo[1]
        Roles.append((RoleSkill,RoleLevel))

    projects.append(Proj(name,length,MaxScore,DeadLine,Roles))

CalculateScore(engs,skillCount,currentScore,)

##print(engs)
##print("\n\n")
##print(TeamSkills)
##print("\n\n")
##for i in projects:
##    print(i.name,i.name,i.length,i.maxScore,i.deadLine,i.roles)
##    print("\n")

memo={}

class State:
    def __init__(self, TeamSkills, eng, score):
        self.TeamSkills = TeamSkills
        self.eng = eng
        self.score = score

def combineState(state,project):
    ##calculate new state for the given project the previous state
    return newState

def calculateState(projOrder):    
    state=memo.get[''.join(projOrder)]
    
    if state is not None:
        return state
    
    if (projOrder.length==0):
        return State(TeamSkills,engs,0)

    state = combineState(calculateState(projOrder[:-1]),projectOrder[-1])
    memo[projOrder]=state

    
   
        
    

            
            
        
        
