#To read xml and take all data in it https://www.youtube.com/watch?v=r6dyk68gymk
import xml.etree.ElementTree as ET
def parsePDF(fileName):
    root = ET.parse(fileName).getroot()
    output = []

    for child in root:
        if "body" in str(child.tag):
            for pages in child:
                if "drawing" in str(pages.tag):
                    for page in pages:
                        for frame in page:
                            for textBox in frame:
                                for textFrame in textBox:
                                    line = ""
                                    for data in textFrame:
                                        line += data.text
                                    output.append(line)
    return output
#find diff between 2 file we can set 1 file as main and dynamic it
def findDiff(file1, file2):
    result1 = parsePDF(file1)
    result2 = parsePDF(file2)
    difference = []
    if len(result1) > len(result2):
        for i in range(len(result2)):
            if result1[i] != result2[i]:
                difference.append({"data1": result1[i], "data2": result2[i], "line": i})
    elif len(result2) > len(result1):
        for i in range(len(result1)):
            if result1[i] != result2[i]:
                difference.append({"data1": result1[i], "data2": result2[i], "line": i})
    return difference

def main():
    output = open("difResult.txt", "w")
    for i in findDiff("example1.xml", "example2.xml"):
        output.write("1: " + i["data1"] + " 2: " + i["data2"] + " at line number : " + str(i["line"]))
        output.write("\n")
    output.close()
findDiff("result.xml", "example2.xml")
main()
