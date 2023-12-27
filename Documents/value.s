.section .data
output:
   .ascii "The value is x\n"
values:
   .int 1,3,5,7,9
.section .text
.globl _start
_start:
   nop 
   movl $output,%esi
   movl $0,%edi
loop:
   movl values(,%edi,4),%eax
   addl $0x30,%eax
   movb %al,13(%esi)
   movl $4,%eax
   movl $1,%ebx
   movl $output,%ecx
   movl $15,%edx
   int $0x80
   inc %edi
   cmpl $5,%edi
   jne loop
   movl $0,%ebx
   movl $1,%eax
   int $0x80
