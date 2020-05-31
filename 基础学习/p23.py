#coding:utf-8

import os
import xml.etree.ElementTree as ET
os.chdir(r'e:\progect\practice')

tree=ET.parse('xmltest.xml')
root=tree.getroot()
print(root)

#遍历XML文档
for child in root:
	print(child.tag,child.attrib)
	for i in child:
		print(i.tag,i.text)#or i.attrib
		
# <Element 'data' at 0x000001AE4BD7DD18> #data

# country {'name': 'Liechtenstein'}#child.tag,child.attrib
# rank 2  #i.tag,i.text
# year 2008  #i.tag,i.text
# gdppc 141100  #i.tag,i.text
# neighbor None  #i.tag,i.text
# neighbor None  #i.tag,i.text

# country {'name': 'Singapore'}
# rank 5
# year 2011
# gdppc 59900
# neighbor None
# country {'name': 'Panama'}
# rank 69
# year 2011
# gdppc 13600
# neighbor None
# neighbor None

#只遍历year节点
for node in root.iter('year'):
	print(node.tag,node.text)
	
# year 2008
# year 2011
# year 2011

#修改
for node in root.iter('year'):
	new_year=int(node.text)+1
	node.text=str(new_year)#修改year节点时间
	node.set("updated","yes")#添加属性
tree.write('xmltest.xml')

#删除
for country in root.findall('country'):
	rank=int(country.find('rank').text)
	if rank>50:
		root.remove(country)
tree.write('outxml.xml')


#创建xml文档
new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
name.text='renchao'
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
age.text = '31'
sex.text='man'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
name2.text='zhenzhen'
age = ET.SubElement(name2,"age")
age.text = '33'
sex=ET.SubElement(name2,"sex")
sex.text='woman'
 
et = ET.ElementTree(new_xml) #生成文档对象
et.write("test2.xml", encoding="utf-8",xml_declaration=True)
 
ET.dump(new_xml) #打印生成的格式 