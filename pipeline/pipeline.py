def getPipelineStatus(env):
    # return "Pipeline status : {} : Just perfect!".format(env)
    return

if __name__ == "__main__":
    print(getPipelineStatus("Staging"))
    print(getPipelineStatus("Development"))
    print(getPipelineStatus("Test"))
    print(getPipelineStatus("Preproduction"))
    print(getPipelineStatus("Production"))
