import PySimpleGUI as sg

User1 = {'用户名' : 'abc','密码' : '123'}
User2 = {'用户名' : 'def','密码' : '456'}
UserList = [User1,User2]

layout = [
[sg.T('用户名',size=(6)),sg.In('请输入您的用户名',key='-User-')],
[sg.T('密码',size=(6)),sg.In('',tooltip='请输入3位数密码',key='-pwd-',password_char='*')],
[sg.B('确认'),sg.B('取消')]
]

window = sg.Window('登录界面',layout)
while True:
	event,values=window.read()
	if event==None:
		break
		
window.close()

	
