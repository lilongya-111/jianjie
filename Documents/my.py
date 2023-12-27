import PySimpleGUI as sg
location = (800,800)
layout = [
		[sg.Text('请输入您的信息')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Text('性别'),sg.InputText('')],
		[sg.Text('       '),sg.InputText('')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Text('性别'),sg.InputText('男')],
		[sg.Text('    '),sg.InputText('')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Text('姓名'),sg.InputText('')],
		[sg.Button('确定'),sg.Button('取消')]
	]

	
window=sg.Window('jiemian',layout)
while True:
	event,values=window.read()
	if event==None:
		break
		
	




window.close()
