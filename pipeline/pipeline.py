import sqlite3

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


if __name__ == "__main__":
    print(getPipelineStatus("Staging"))
    print(getPipelineStatus("Development"))
    print(getPipelineStatus("Test"))
    print(getPipelineStatus("Preproduction"))
    print(getPipelineStatus("Production"))
