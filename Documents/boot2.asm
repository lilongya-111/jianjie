org 0x7c00
mov ah ,0x07
mov al ,'G'

mov bx ,0xb800
mov es ,bx
mov [es:0] ,ax
stop:
    hlt
jmp stop
times 510-($-$$) db 0
db 0x55,0xaa
