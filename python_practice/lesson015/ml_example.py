import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('company.xml')
root = tree.getroot()
# print(root.attrib)
# Читання та виведення даних з елементів XML-документу
# for project in root.findA("projects"):
#     # print(type(root))
#     # print(type(child))
#     # print(child.tag, child.attrib)
#     for item in project:
#         if item.text == "AI Assistant":
#             particular_project_budget = project.find("budget")
#             print(particular_project_budget.text)
#             print(particular_project_budget.attrib)
#         # print(item.tag)
#         # print(item.attrib)
#         # print(item.text)

# for projects in root:
#     print(projects.find("department").attrib)
#     # if projects.tag == "projects":
#     for project in projects.findall("project"):
#         print(project.find("name").text)
#         # print(item.text)
#         # print(item.attrib)


print(root.find("departments").find("department").attrib)


# Створення кореневого елемента
root = ET.Element('data')

# Створення під-елементів та додавання їх до кореневого елемента
child1 = ET.SubElement(root, 'child1')
child1.text = 'Data 1'
child2 = ET.SubElement(root, 'child2')
child2.text = 'Data 2'
child2.attrib = {"atr1":"value"}

# Запис у XML-файл
tree = ET.ElementTree(root)
tree.write('output.xml')