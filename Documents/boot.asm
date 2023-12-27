mov ax,3
int 0x10

xchg bx, bx

mov ax, 0xb800
mov ds, ax
 
mov byte [0], '-'
mov byte [2], '-'
mov byte [4], '-'
mov byte [6], '-'
mov byte [8], '-'
mov byte [10], '-'
mov byte [12], '-'
mov byte [14], '-'
mov byte [16], '-'
mov byte [18], '-'
mov byte [20], '-'
mov byte [22], '-'
mov byte [24], '-'
mov byte [26], '-'
mov byte [28], '-'
mov byte [30], '-'
mov byte [32], '-'
mov byte [34], '-'
mov byte [36], '-'
mov byte [38], '-'
mov byte [40], '-'
mov byte [42], '-'
mov byte [44], '-'
mov byte [46], '-'
mov byte [48], '-'
mov byte [50], '-'
mov byte [52], '-'
mov byte [54], '-'
mov byte [56], '-'
mov byte [58], '-'
mov byte [60], '-'
mov byte [62], '-'
mov byte [64], '-'
mov byte [66], '-'
mov byte [68], '-'
mov byte [70], '-'
mov byte [72], '-'
mov byte [74], '-'
mov byte [76], '-'
mov byte [78], '-'
mov byte [80], '-'
mov byte [82], '-'
mov byte [84], '-'
mov byte [86], '-'
mov byte [88], '-'
mov byte [90], '-'  
mov byte [92], '-'
mov byte [94], '-'
mov byte [96], '-'
mov byte [98], '-'
mov byte [100], '-'
mov byte [102], '-'
mov byte [104], '-'
mov byte [106], '-'
mov byte [108], '-'
mov byte [110], '-'
mov byte [112], '-'
mov byte [114], '-'
mov byte [116], '-'
mov byte [118], '-'
mov byte [120], '-'
mov byte [122], '-'
mov byte [124], '-'
mov byte [126], '-'
mov byte [128], '-'
mov byte [130], '-'
mov byte [132], '-'
mov byte [134], '-'
mov byte [136], '-'
mov byte [138], '-'
mov byte [140], '-' 
mov byte [142], '-' 
mov byte [144], '-' 
mov byte [146], '-' 
mov byte [148], '-' 
mov byte [150], '-' 
mov byte [152], '-' 
mov byte [154], '-' 
mov byte [156], '-' 
mov byte [gs:158], '1' 

mov byte [gs:160], 0xA4



mov byte [318], '2' 
mov byte [320], '|' 
   

;halt:
 ;   jmp halt

times 510 - ($ - $$) db 0
db 0x55, 0xaa 
