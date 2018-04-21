import sqlite3

def connectDB():
    cur = sqlite3.connect(database="./devops_meta.db", isolation_level=None)
    res = cur.execute("SELECT date('now'), time('now');")
    return res.fetchone()

def getPipelineStatus(env):
    environments = []
    environments.append("Staging")
    environments.append("Development")
    environments.append("Test")
    environments.append("Preproduction")
    environments.append("Production")

    if env in environments:
        return "Pipeline status : {} : Just perfect!".format(env)
    
    return None

def main():
    print(connectDB())

if __name__ == "__main__":
    #print(getPipelineStatus("Staging"))
    #print(getPipelineStatus("Development"))
    #print(getPipelineStatus("Test"))
    #print(getPipelineStatus("Preproduction"))
    #print(getPipelineStatus("Production"))
    main()
