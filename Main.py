#%%
from Imports import *
import CsvWriter

allPIData = None
readCount = 0

def ReadCsv():
    global allPIData

    #Setting Previous Data Directory
    previousPiDirectory = (r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1\FC1 Data')
    os.chdir(previousPiDirectory)
    #Reading All FC1 Previous Data
    previousPiData = glob.glob('*.csv')
    
    # Sort files by modification date
    previousPiData.sort(key=lambda x: os.path.getmtime(x))
    previousPiDataList = []

    #Appending All Previous Data Into List
    for f in previousPiData:
        a = pd.read_csv(f, encoding='latin1', skiprows=1)

        a.columns = [
            "DATE", 
            "TIME", 
            "MODEL CODE", 
            "S/N", 
            "PASS/NG", 
            "¶", 
            "VOLTAGE MAX (V)", 
            "WATTAGE MAX (W)", 
            "CLOSED PRESSURE_MAX (kPa)",
            "VOLTAGE Middle (V)", 
            "WATTAGE Middle (W)", 
            "AMPERAGE Middle (A)", 
            "CLOSED PRESSURE Middle (kPa)", 
            "dB(A) 1", 
            "dB(A) 2", 
            "dB(A) 3", 
            "VOLTAGE MIN (V)", 
            "WATTAGE MIN (W)", 
            "CLOSED PRESSURE MIN (kPa)", 
            "Middle züÊ", 
            "Max züÊ", 
            "INSULATION PASS/NG", 
            "WITHSTAND VOLTAGE PASS/GO", 
            "mL/min", 
            "DM01293", 
            "VOLTAGE MAX PASS/NG", 
            "WATTAGE MAX PASS/NG", 
            "CLOSED PRESSURE MAX PASS/NG",
            "Middle inhale Air volume", 
            "MAX inhale Air volume", 
            "VOLTAGE Middle PASS/NG", 
            "WATTAGE Middle PASS/NG", 
            "AMPERAGE Middle PASS/NG", 
            "CLOSED PRESSURE Middle PASS/NG", 
            "VOLTAGE MIN PASS/NG", 
            "WATTAGE MIN PASS/NG", 
            "CLOSED PRESSURE MIN PASS/NG", 
            "Ø°¸TESTÊPASS/NG", 
            "INSPECTED Q'TY", 
            "PASSED Q'TY", 
            "AMPERAGE MAX (A)", 
            "PRESSURE MAX@(kPa)", 
            "PRESSURE Middle (kPa)", 
            "PRESSURE MIN (kPa)", 
            "Min LEAK PRESSURE (kPa)", 
            "Min LEAK TIME (sec)", 
            "CLOSED VOLTAGE MAX (V)", 
            "CLOSED AMPERAGE MAX (A)", 
            "NG Q'TY", 
            "CLOSED WATTAGE MAX (W)", 
            "CLOSED VOLTAGE Middle (V)", 
            "CLOSED AMPERAGE Middle (A)", 
            "CLOSED WATTAGE Middle (W)", 
            "AMPERAGE MIN (A)", 
            "CLOSED VOLTAGE MIN (V)", 
            "CLOSED AMPERAGE MIN (A)", 
            "CLOSED WATTAGE MIN (W)", 
            "DM01800", 
            "S/N SWAP", 
            "ÄÞ×²ÊÞd³ügªèl",
        ]

        previousPiDataList.append(a)

    piDirectory = (r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1')
    os.chdir(piDirectory)

    #Appending Latest Data Into List
    allPIData = pd.read_csv('log000_FC1.csv', encoding='latin1', skiprows=1)

    allPIData.columns = [
        "DATE", 
        "TIME", 
        "MODEL CODE", 
        "S/N", 
        "PASS/NG", 
        "¶", 
        "VOLTAGE MAX (V)", 
        "WATTAGE MAX (W)", 
        "CLOSED PRESSURE_MAX (kPa)",
        "VOLTAGE Middle (V)", 
        "WATTAGE Middle (W)", 
        "AMPERAGE Middle (A)", 
        "CLOSED PRESSURE Middle (kPa)", 
        "dB(A) 1", 
        "dB(A) 2", 
        "dB(A) 3", 
        "VOLTAGE MIN (V)", 
        "WATTAGE MIN (W)", 
        "CLOSED PRESSURE MIN (kPa)", 
        "Middle züÊ", 
        "Max züÊ", 
        "INSULATION PASS/NG", 
        "WITHSTAND VOLTAGE PASS/GO", 
        "mL/min", 
        "DM01293", 
        "VOLTAGE MAX PASS/NG", 
        "WATTAGE MAX PASS/NG", 
        "CLOSED PRESSURE MAX PASS/NG",
        "Middle inhale Air volume", 
        "MAX inhale Air volume", 
        "VOLTAGE Middle PASS/NG", 
        "WATTAGE Middle PASS/NG", 
        "AMPERAGE Middle PASS/NG", 
        "CLOSED PRESSURE Middle PASS/NG", 
        "VOLTAGE MIN PASS/NG", 
        "WATTAGE MIN PASS/NG", 
        "CLOSED PRESSURE MIN PASS/NG", 
        "Ø°¸TESTÊPASS/NG", 
        "INSPECTED Q'TY", 
        "PASSED Q'TY", 
        "AMPERAGE MAX (A)", 
        "PRESSURE MAX@(kPa)", 
        "PRESSURE Middle (kPa)", 
        "PRESSURE MIN (kPa)", 
        "Min LEAK PRESSURE (kPa)", 
        "Min LEAK TIME (sec)", 
        "CLOSED VOLTAGE MAX (V)", 
        "CLOSED AMPERAGE MAX (A)", 
        "NG Q'TY", 
        "CLOSED WATTAGE MAX (W)", 
        "CLOSED VOLTAGE Middle (V)", 
        "CLOSED AMPERAGE Middle (A)", 
        "CLOSED WATTAGE Middle (W)", 
        "AMPERAGE MIN (A)", 
        "CLOSED VOLTAGE MIN (V)", 
        "CLOSED AMPERAGE MIN (A)", 
        "CLOSED WATTAGE MIN (W)", 
        "DM01800", 
        "S/N SWAP", 
        "ÄÞ×²ÊÞd³ügªèl",
    ]

    previousPiDataList.append(allPIData)

    allPIData = pd.concat(previousPiDataList, ignore_index=True)

    allPIData.iloc[:, 2] = allPIData.iloc[:, 2].replace(' ', '', regex=True)
    allPIData.iloc[:, 2] = allPIData.iloc[:, 2].replace('"', '', regex=True)


def Start():
    global readCount
    global allPIData

    fileReaded = False

    while fileReaded == False:
        try:
            origFile = os.path.getmtime(r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1\log000_FC1.csv')
            fileReaded = True
        except:
            fileReaded = False
    fileReaded = False

    while True:
        while fileReaded == False:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1\log000_FC1.csv')
                fileReaded = True
            except:
                fileReaded = False
        fileReaded = False

        if currentFile != origFile:
            print("Changes Detected")

            ReadCsv()
            CsvWriter.WriteCsv(allPIData)

            origFile = currentFile

        print("Waiting For Changes In PiCompiled")

        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0
        time.sleep(1)


Start()

# ReadCsv()
# CsvWriter.WriteCsv(allPIData)

# %%
