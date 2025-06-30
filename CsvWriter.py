from Imports import *
# %%
def WriteCsv(data):
    global dateToReadDashFormat

    fileDirectory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\CompiledPiMachine')
    os.chdir(fileDirectory)
    print(os.getcwd())

    print("Creating New File")
    newValue = pd.concat([data], axis = 0, ignore_index = True)
    wireFrame = newValue
    wireFrame.to_csv(f"CompiledPIMachine.csv", index = False, quoting=0)

    #Open Directory
    os.startfile(fileDirectory)